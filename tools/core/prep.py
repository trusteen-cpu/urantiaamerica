# -*- coding: utf-8 -*-
# 핵심 진리(core) 메뉴: 인용 자동 맞추기 + 번역 도우미 작업 파일 만들기
#   python prep.py            (src/ 가 바뀌면 다시 돌린다; <l>/ 번역본은 건드리지 않음)
# 이 메뉴의 인용은 모두 산문 속에 있다: “⟦Q 1:0.3⟧Be you perfect, even as I am perfect⟦/Q⟧”[1:0.3]  (블록 인용 없음)
# 결과
#   auto_<l>.json             자동으로 잘라 온 ⟦Q⟧ 인용 {"01.013.p#0": "공식 번역 글자 그대로"}
#                             번역자가 ⟦Q ref⟧⟦/Q⟧ 를 비워 두면 빌더가 이 글로 채운다(직접 적어도 됨).
#   work/src_cNN.json         번역할 단위(세 언어 공용, 읽기 전용) — src/cNN.json 과 같음
#   work/todo_<l>_cNN.json    손으로 잘라야 할 ⟦Q⟧ 인용 {"키#i": {"cit", "en", "verse", "why"}}
#   work/inline_<l>_cNN.json  모든 ⟦Q⟧ 인용 {"키": [{"cit", "en", "verse", "auto"}]}  (auto 가 null 이면 todo 에 있음)
#   work/phrases_<l>_cNN.json 표시 없는 “따옴표 말”(이름·느슨한 인용) {"키": [{"en", "cit", "verse"}]} — 공식 말씨 참고용
# 맞추기: 절 전체 → 공식 절 전체 / 영어 절의 몇 번째 문장들 → 공식 절의 같은 번째 문장(문장 수가 같을 때)
#        / 영어 절 속 따옴표 구절 전체 → 공식 절의 같은 번째 따옴표 구절(따옴표 구절 수가 같을 때)
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

LANGS = ("es", "fr", "pt")
CHUNKS = ["c01", "c02", "c03", "c04", "c05"]
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
W = lambda s: re.sub(r"\W+", "", s).lower()
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧")
REF = re.compile(r"\[(\d+:\d+\.\d+)\]")
LOOSE = re.compile(r"“([^“”⟦]{2,}?)”")
QSEG = {"en": re.compile(r"[\"“]([^\"“”]+)[\"”]"),
        "es": re.compile(r"«([^«»]+)»|“([^“”]+)”"), "fr": re.compile(r"«\s?([^«»]+?)\s?»|“([^“”]+)”"),
        "pt": re.compile(r"“([^“”]+)”|«([^«»]+)»")}


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


def qsegs(l, t):
    return [next(g for g in m.groups() if g is not None).strip() for m in QSEG[l].finditer(t)]


def align(l, q, ref):
    if ref not in EN: return None, "bad citation"
    en, tr = EN[ref], amq.text(l, ref)
    if W(q) == W(en): return tr, None
    # 따옴표 구절 전체
    eq, tq = qsegs("en", en), qsegs(l, tr)
    hits = [i for i, x in enumerate(eq) if W(x) == W(q) or W(x).rstrip() == W(q)]
    if hits:
        if len(eq) != len(tq): return None, f"quoted phrases en {len(eq)} vs {l} {len(tq)}"
        return tq[hits[0]].strip(" ,.;:"), None
    a, b = sents(en), sents(tr)
    if len(a) != len(b): return None, f"partial sentence (sentence count en {len(a)} vs {l} {len(b)})"
    out = []
    for seg in re.split(r"\s*(?:…|\.\.\.)\s*", q):
        if not W(seg): continue
        sp = span(seg.strip(), a)
        if not sp: return None, "partial sentence"
        out.append(" ".join(b[sp[0]:sp[1] + 1]))
    return " … ".join(out), None


def main():
    os.makedirs(os.path.join(H, "work"), exist_ok=True)
    auto = {l: {} for l in LANGS}
    rows = []
    for c in CHUNKS:
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        json.dump(S, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        nq = sum(len(MARK.findall(v)) for v in S.values())
        row = {"c": c, "q": nq}
        for l in LANGS:
            todo, inl, phr = {}, {}, {}
            for k, v in S.items():
                for i, m in enumerate(MARK.finditer(v)):
                    ref, q = m.group(1), m.group(2)
                    r, why = align(l, q, ref)
                    if r is not None and not amq.check(l, ref, r): r, why = None, "check failed"
                    verse = amq.text(l, ref) if ref in EN else ""
                    inl.setdefault(k, []).append({"cit": ref, "en": q, "verse": verse, "auto": r})
                    if r is not None: auto[l][f"{k}#{i}"] = r
                    else: todo[f"{k}#{i}"] = {"cit": ref, "en": q, "verse": verse, "why": why}
                for m in LOOSE.finditer(v):
                    nxt = REF.search(v, m.end())
                    ref = nxt.group(1) if nxt else None
                    phr.setdefault(k, []).append({"en": m.group(1), "cit": ref,
                                                  "verse": amq.text(l, ref) if ref and ref in EN else ""})
            for name, d in (("todo", todo), ("inline", inl), ("phrases", phr)):
                json.dump(d, open(os.path.join(H, "work", f"{name}_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            row[l] = (nq - len(todo), len(todo))
            row["phr"] = sum(len(x) for x in phr.values())
        rows.append(row)
    for l in LANGS:
        json.dump(auto[l], open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("chunk | ⟦Q⟧ quotations | " + " | ".join(f"{l} auto/todo" for l in LANGS) + " | loose “phrases”")
    for r in rows:
        print(f"{r['c']} | {r['q']} | " + " | ".join(f"{r[l][0]}/{r[l][1]}" for l in LANGS) + f" | {r['phr']}")


main()
