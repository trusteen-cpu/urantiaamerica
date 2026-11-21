# -*- coding: utf-8 -*-
# 우주론 메뉴: 인용 자동 맞추기 + 번역 도우미 작업 파일 만들기
#   python prep.py            (src/ 가 바뀌면 다시 돌린다; <l>/ 번역본은 건드리지 않음)
# 결과
#   auto_<l>.json            블록 인용 중 자동으로 잘라 온 것 {"w03.045": "공식 번역 인용"}
#   work/src_cNN.json         번역할 단위(블록 인용 제외: 문자열·표 행) — 세 언어 공용, 읽기 전용
#   work/todo_<l>_cNN.json    손으로 잘라야 할 블록 인용 {"키": {"cit", "en", "why"}}
#   work/inline_<l>_cNN.json  산문 속 ⟦Q⟧ 인용 {"키": [{"cit", "en", "verse"}]} — 번역할 때 참고
# 블록 인용 맞추기: 절 전체 인용 → 공식 절 전체(여러 절이면 공백으로 이음).
#   그 밖은 영어 인용을 ' … ' 토막으로 나누어 영어 절(들)의 몇 번째 문장들인지 찾고, 공식 절의 문장 수가 같으면 같은 번째 문장을 가져온다.
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
KEYS = list(EN); IDX = {k: i for i, k in enumerate(KEYS)}
SK = json.load(open(os.path.join(H, "src", "skeleton.json"), encoding="utf-8"))
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
W = lambda s: re.sub(r"\W+", "", s).lower()
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧")


def cit_keys(cit):
    out = []
    for tok in re.split(r"\s*[,;]\s*", cit.strip()):
        m = re.fullmatch(r"(\d+):(\d+)\.(\d+)(?:[–\-](\d+)(?::(\d+)\.(\d+))?)?", tok)
        if not m: return None
        a = f"{m.group(1)}:{m.group(2)}.{m.group(3)}"
        b = f"{m.group(4)}:{m.group(5)}.{m.group(6)}" if m.group(5) else (f"{m.group(1)}:{m.group(2)}.{m.group(4)}" if m.group(4) else a)
        if a not in IDX or b not in IDX: return None
        out += KEYS[IDX[a]:IDX[b] + 1]
    return out


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
    es, ts = [], []
    for k in ks:
        a, b = sents(EN[k]), sents(amq.text(l, k))
        if len(a) != len(b): return None, f"sentence count en {len(a)} vs {l} {len(b)} in {k}"
        es += a; ts += b
    out = []
    for seg in re.split(r"\s*(?:…|\.\.\.)\s*", q):
        if not W(seg): continue
        sp = span(seg.strip(), es)
        if not sp: return None, "partial sentence"
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


def main():
    langs = ("es", "fr", "pt")
    stats = {l: [0, 0] for l in langs}
    auto = {l: {} for l in langs}
    for c in SK["chunks"]:
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        P = {k: v for k, v in S.items() if not isinstance(v, dict)}
        json.dump(P, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        for l in langs:
            todo, inl = {}, {}
            for k, v in S.items():
                if isinstance(v, dict):
                    r, why = align(l, v["q"], v["cit"])
                    if r is not None and qcheck(l, r, v["cit"]):
                        auto[l][k] = r; stats[l][0] += 1
                    else:
                        todo[k] = {"cit": v["cit"], "en": v["q"], "why": why or "check failed"}; stats[l][1] += 1
                else:
                    for s in (v if isinstance(v, list) else [v]):
                        for m in MARK.finditer(s):
                            ks = cit_keys(m.group(1)) or []
                            inl.setdefault(k, []).append({"cit": m.group(1), "en": m.group(2),
                                                          "verse": " ".join(amq.text(l, x) for x in ks)})
            json.dump(todo, open(os.path.join(H, "work", f"todo_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            json.dump(inl, open(os.path.join(H, "work", f"inline_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(c, "prose units", len(P), "words", sum(len((" ".join(v) if isinstance(v, list) else v).split()) for v in P.values()),
              " ".join(f"{l} todo {len(json.load(open(os.path.join(H, 'work', f'todo_{l}_{c}.json'), encoding='utf-8')))}" for l in langs))
    for l in langs:
        json.dump(auto[l], open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(l, "block quotations auto", stats[l][0], "by hand", stats[l][1])


main()
