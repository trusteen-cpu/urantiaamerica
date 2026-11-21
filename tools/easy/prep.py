# -*- coding: utf-8 -*-
# 읽기 쉬운 해설판: ⟦Q⟧ 인용 자동 맞추기 + 번역 도우미 작업 파일 만들기
#   python prep.py            (src/ 가 바뀌면 다시 돌린다; <l>/ 번역본은 건드리지 않음)
# 결과
#   auto_<l>.json             {"009:33": [["9:3.5", "공식 번역 인용" 또는 null], …]}  단위 안 ⟦Q⟧ 표시 차례대로(영어 순서)
#   work/src_cNN.json          번역할 단위(영어) — 세 언어 공용, 읽기 전용 (src/cNN.json 과 같음)
#   work/todo_<l>_cNN.json     손으로 잘라야 할 인용 {"키": [{"cit", "en", "why", "verse"}]}
#   work/quotes_<l>_cNN.json   그 묶음의 모든 ⟦Q⟧ 인용 {"키": [{"cit", "en", "auto", "verse"}]} — 문장을 짤 때 참고
# 자동 맞추기: 절 전체 인용 → 공식 절 전체. 그 밖은 영어 인용을 ' … ' 토막으로 나누어 영어 절의 몇 번째 문장들인지 찾고,
#   공식 절의 문장 수가 같으면 같은 번째 문장을 가져온다(tools/cosmology/prep.py 와 같은 방법). 구절(문장의 일부)은 손으로.
# 번역자는 자동으로 맞춘 인용을 빈 표시 ⟦Q 9:3.5⟧⟦/Q⟧ 로 두고, 빌더가 auto_<l>.json 에서 채운다.
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
# en.json 의 121:8.12~14 밀림을 표준 번호로 바로잡는다(extract_src.py 와 같음)
EN["121:8.12"], EN["121:8.13"], EN["121:8.14"] = EN["121:8.14"], EN["121:8.12"], EN["121:8.13"]
KEYS = list(EN); IDX = {k: i for i, k in enumerate(KEYS)}
CHUNKS = [c["id"] for c in json.load(open(os.path.join(H, "src", "chunks.json"), encoding="utf-8"))]
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
W = lambda s: re.sub(r"\W+", "", s).lower()
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧", re.S)
LANGS = ("es", "fr", "pt")


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
    q = q.replace("**", "").strip()
    if not all(W(p) in W(" ".join(EN[k] for k in ks)) for p in re.split(r"…|\.\.\.", q) if W(p)):
        return None, "English is not verbatim in the verse (paraphrase): cut the closest official words"
    if W(q) == W(" ".join(EN[k] for k in ks)):
        return " ".join(amq.text(l, k) for k in ks), None
    es, ts = [], []
    for k in ks:
        a, b = sents(EN[k]), sents(amq.text(l, k))
        if len(a) != len(b): return None, f"sentence count en {len(a)} vs {l} {len(b)}"
        es += a; ts += b
    out = []
    for seg in re.split(r"\s*(?:…|\.\.\.)\s*", q):
        if not W(seg): continue
        sp = span(seg.strip(), es)
        if not sp: return None, "part of a sentence"
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
    os.makedirs(os.path.join(H, "work"), exist_ok=True)
    auto = {l: {} for l in LANGS}
    tot = {l: [0, 0] for l in LANGS}
    rows = []
    for c in CHUNKS:
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        json.dump(S, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        row = {"id": c, "quotes": sum(len(MARK.findall(v)) for v in S.values())}
        for l in LANGS:
            todo, allq, n_auto = {}, {}, 0
            for k, v in S.items():
                ms = MARK.findall(v)
                if not ms: continue
                lst = []
                for cit, q in ms:
                    ks = cit_keys(cit) or []
                    verse = " ".join(amq.text(l, x) for x in ks)
                    r, why = align(l, q, cit)
                    if r is not None and not qcheck(l, r, cit): r, why = None, "check failed"
                    lst.append([cit, r])
                    allq.setdefault(k, []).append({"cit": cit, "en": q, "auto": r, "verse": verse})
                    if r is None: todo.setdefault(k, []).append({"cit": cit, "en": q, "why": why, "verse": verse})
                    else: n_auto += 1
                auto[l][k] = lst
            json.dump(todo, open(os.path.join(H, "work", f"todo_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            json.dump(allq, open(os.path.join(H, "work", f"quotes_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            row[l] = (n_auto, sum(len(x) for x in todo.values()))
            tot[l][0] += n_auto; tot[l][1] += row[l][1]
        rows.append(row)
        print(c, "units", len(S), "quotations", row["quotes"], " ".join(f"{l} auto {row[l][0]} todo {row[l][1]}" for l in LANGS))
    for l in LANGS:
        json.dump(auto[l], open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(l, "quotations auto", tot[l][0], "by hand", tot[l][1])


main()
