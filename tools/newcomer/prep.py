# -*- coding: utf-8 -*-
# 새 독자 안내서(newcomer) 메뉴: 인용 자동 맞추기 + 번역 도우미 작업 파일 만들기 (tools/cosmology/prep.py 를 옮김)
#   python prep.py            (src/ 가 바뀌면 다시 돌린다; <l>/ 번역본은 건드리지 않음)
# 결과
#   auto_<l>.json            블록 인용 중 자동으로 잘라 온 것 {"w03:45": "공식 번역 인용"}
#   work/src_cNN.json         번역할 단위(블록 인용 제외: 문자열·표 행·[부 제목, 부제]·부록 낱말 {"term","def"}) — 세 언어 공용, 읽기 전용
#   work/todo_<l>_cNN.json    손으로 잘라야 할 블록 인용 {"키": {"cit", "en", "why", "verse"}} — verse = 공식 번역 절(들) 전문
# 인용 맞추기: 절 전체 인용 → 공식 절 전체(여러 절이면 공백으로 이음).
#   그 밖은 영어 인용을 ' … ' 토막으로 나누어 영어 절(들)의 몇 번째 문장들인지 찾고, 공식 절의 문장 수가 같으면 같은 번째 문장을 가져온다.
#   문장 수가 다른 절은 통째로만 맞춘다(토막이 그 절 전체일 때).
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
CHUNKS = ("c01", "c02", "c03")
LANGS = ("es", "fr", "pt")
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
W = lambda s: re.sub(r"\W+", "", s).lower()


def cit_keys(cit):
    """'1:0.3' · '1:2.4-6' · '15:2.3–9' · '101:2.15, 17' · '1:2.3, 3:4.5' → 절 키 목록 (극동판 newcomer 빌더와 같은 규칙)."""
    keys, cur = [], None
    for part in re.split(r"\s*,\s*", cit.strip()):
        m = re.fullmatch(r"(?:(\d+):(\d+)\.)?(\d+)(?:\s*[-–]\s*(\d+))?", part)
        if not m: return None
        if m.group(1): cur = (m.group(1), m.group(2))
        if cur is None: return None
        for p in range(int(m.group(3)), int(m.group(4) or m.group(3)) + 1):
            k = f"{cur[0]}:{cur[1]}.{p}"
            if k not in EN: return None
            keys.append(k)
    return keys


def sents(t):
    out, pos = [], 0
    for m in SPLIT.finditer(t):
        out.append(t[pos:m.end()].strip()); pos = m.end()
    out.append(t[pos:].strip())
    return [s for s in out if s]


def span(q, ss):
    wq = W(q)
    if not wq: return None
    for i in range(len(ss)):
        acc = ""
        for j in range(i, len(ss)):
            acc += W(ss[j])
            if acc == wq: return i, j
            if len(acc) > len(wq): break
    return None


def align(l, q, cit):
    ks = cit_keys(cit)
    if not ks: return None, "bad citation"
    if W(q) == W(" ".join(EN[k] for k in ks)):
        return " ".join(amq.text(l, k) for k in ks), None
    es, ts, odd = [], [], []
    for k in ks:
        a, b = sents(EN[k]), sents(amq.text(l, k))
        if len(a) != len(b):   # 문장 나눔이 다르면 이 절은 통째로만 쓸 수 있다
            a, b = [EN[k]], [amq.text(l, k)]; odd.append(k)
        es += a; ts += b
    out = []
    for seg in re.split(r"\s*(?:…|\.\.\.)\s*", q):
        if not W(seg): continue
        sp = span(seg.strip(), es)
        if not sp:
            return None, (f"sentence count differs in {', '.join(odd)}" if odd else "partial sentence")
        out.append(" ".join(ts[sp[0]:sp[1] + 1]))
    r = " … ".join(out)
    whole_en = sum(len(EN[k]) for k in ks); whole_t = sum(len(amq.text(l, k)) for k in ks)
    x = (len(r) / len(q)) / (whole_t / whole_en)
    if not 0.7 <= x <= 1.4: return None, f"length mismatch {x:.2f}"
    return r, None


def qcheck(l, text, cit):
    ks = cit_keys(cit)
    if not ks: return False
    hay = re.sub(r"\s+", "", "".join(amq.text(l, k) for k in ks))
    return all(re.sub(r"\s+", "", p) in hay for p in re.split(r"…|\.\.\.", text) if p.strip())


def selftest():
    """영어 원고 인용이 en.json 에 그대로 있는지 — 어긋나면 자동 맞추기가 실패하므로 알려 준다."""
    norm = lambda s: re.sub(r"[\W_]+", "", s).lower()
    bad = []
    for c in CHUNKS:
        for k, v in json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8")).items():
            if isinstance(v, dict) and "q" in v:
                ks = cit_keys(v["cit"])
                hay = norm("".join(EN[x] for x in ks)) if ks else ""
                if not ks or any(norm(p) not in hay for p in re.split(r"…|\.\.\.", v["q"]) if norm(p)):
                    bad.append(f"{k} [{v['cit']}]")
    print("English quotations not verbatim in en.json:", bad or "none")


def main():
    os.makedirs(os.path.join(H, "work"), exist_ok=True)
    selftest()
    stats = {l: {} for l in LANGS}
    auto = {l: {} for l in LANGS}
    for c in CHUNKS:
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        P = {k: v for k, v in S.items() if not (isinstance(v, dict) and "q" in v)}
        json.dump(P, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        nq = len(S) - len(P)
        for l in LANGS:
            todo = {}
            for k, v in S.items():
                if not (isinstance(v, dict) and "q" in v): continue
                r, why = align(l, v["q"], v["cit"])
                if r is not None and qcheck(l, r, v["cit"]):
                    auto[l][k] = r
                else:
                    todo[k] = {"cit": v["cit"], "en": v["q"], "why": why or "check failed",
                               "verse": " ".join(amq.text(l, x) for x in (cit_keys(v["cit"]) or []))}
            json.dump(todo, open(os.path.join(H, "work", f"todo_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            stats[l][c] = (nq - len(todo), len(todo))
        print(c, "prose units", len(P), "quotations", nq,
              "  ".join(f"{l} auto {stats[l][c][0]} todo {stats[l][c][1]}" for l in LANGS))
    for l in LANGS:
        json.dump(auto[l], open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(l, "quotations auto", sum(a for a, _ in stats[l].values()), "by hand", sum(b for _, b in stats[l].values()))


main()
