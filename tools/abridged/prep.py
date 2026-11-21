# -*- coding: utf-8 -*-
# 요약본(abridged) 메뉴: 인용 자동 맞추기 + 번역 도우미 작업 파일 만들기
#   python prep.py            (src/ 가 바뀌거나 tools/data/<l>.json 을 새로 만들면 다시 돌린다; <l>/ 번역본은 건드리지 않음)
# 결과
#   auto_<l>.json             인용 상자(.q) 중 자동으로 잘라 온 것 {"1.b6.q": "공식 번역 인용(표시·바깥 따옴표 없음)"}
#   work/src_cNN.json         번역할 단위(인용 상자 .q 제외) — 세 언어 공용, 읽기 전용
#   work/todo_<l>_cNN.json    손으로 잘라야 할 인용 상자 {"키": {"cit", "en", "why", "verses": {절: 공식 절 전체}}}
#   work/inline_<l>_cNN.json  산문·표 속 ⟦Q⟧ 인용 {"키": [{"cit", "en", "auto"(자동으로 자른 것, 없으면 ""), "verses"}]}
#   work/title_hints_<l>.json 편 제목·번호 붙은 장 제목의 공식 번역 {"1.title": "…", "1.b8.h": "1. …", "0.b7.h": "I. …"}
# 맞추기: 절 전체 인용 → 공식 절 전체. 그 밖은 영어 인용을 ' … ' 토막으로 나누어 영어 절의 몇 번째 문장들인지 찾고,
#   공식 절의 문장 수가 같으면 같은 번째 문장을 가져온다. ⟦Q a|b|c⟧ 의 후보 절을 차례로 해 본다.
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

LANGS = ("es", "fr", "pt")
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
CHUNKS = [c["id"] for c in json.load(open(os.path.join(H, "src", "chunks.json"), encoding="utf-8"))]
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
W = lambda s: re.sub(r"\W+", "", s).lower()
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧", re.S)
ELL = re.compile(r"\s*(?:…|\.\.\.)\s*")


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


def align1(l, q, k):
    if k not in EN: return None, "unknown verse"
    if W(q) == W(EN[k]): return amq.text(l, k), None
    a, b = sents(EN[k]), sents(amq.text(l, k))
    if len(a) != len(b): return None, f"sentence count en {len(a)} vs {l} {len(b)} in {k}"
    out = []
    for seg in ELL.split(q):
        if not W(seg): continue
        sp = span(seg.strip(), a)
        if not sp: return None, "partial sentence"
        out.append(" ".join(b[sp[0]:sp[1] + 1]))
    r = " … ".join(out)
    x = (len(r) / max(1, len(q))) / (len(amq.text(l, k)) / len(EN[k]))
    if not 0.7 <= x <= 1.4: return None, f"length mismatch {x:.2f}"
    if not amq.check(l, k, r): return None, "check failed"
    return r, None


def align(l, q, cits):
    why = []
    for k in cits.split("|"):
        r, w = align1(l, q, k)
        if r is not None: return r, k, None
        why.append(f"{k}: {w}")
    return None, None, "; ".join(why)


def box_inner(v):
    m = MARK.search(v)
    return m.group(1), m.group(2)


def main():
    stats = {l: [0, 0, 0, 0] for l in LANGS}     # box auto, box todo, inline auto, inline total
    auto = {l: {} for l in LANGS}
    os.makedirs(os.path.join(H, "work"), exist_ok=True)
    rows = []
    for c in CHUNKS:
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        P = {k: v for k, v in S.items() if not k.endswith(".q")}
        json.dump(P, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        words = sum(len(re.sub(r"⟦/?Q[^⟧]*⟧", "", s).split()) for v in P.values()
                    for s in ([x for r in v for x in r] if isinstance(v, list) else [v]))
        nbox = sum(1 for k in S if k.endswith(".q"))
        ninl = sum(len(MARK.findall(s)) for v in P.values() for s in ([x for r in v for x in r] if isinstance(v, list) else [v]))
        row = {"c": c, "papers": None, "words": words, "box": nbox, "inline": ninl}
        for l in LANGS:
            todo, inl, ba, ia = {}, {}, 0, 0
            for k, v in S.items():
                if k.endswith(".q"):
                    cits, q = box_inner(v)
                    r, used, why = align(l, q, cits)
                    if r is not None:
                        auto[l][k] = r; ba += 1
                    else:
                        todo[k] = {"cit": cits, "en": q, "why": why,
                                   "verses": {x: amq.text(l, x) for x in cits.split("|") if x in EN}}
                    continue
                for s in ([x for r_ in v for x in r_] if isinstance(v, list) else [v]):
                    for m in MARK.finditer(s):
                        r, used, why = align(l, m.group(2), m.group(1))
                        ia += r is not None
                        inl.setdefault(k, []).append({"cit": m.group(1), "en": m.group(2), "auto": r or "",
                                                      "verses": {x: amq.text(l, x) for x in m.group(1).split("|") if x in EN}})
            json.dump(todo, open(os.path.join(H, "work", f"todo_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            json.dump(inl, open(os.path.join(H, "work", f"inline_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            stats[l][0] += ba; stats[l][1] += len(todo); stats[l][2] += ia; stats[l][3] += ninl
            row[l] = (ba, len(todo), ia)
        rows.append(row)
    for l in LANGS:
        json.dump(auto[l], open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    # 제목 힌트
    ROM = {r: i for i, r in enumerate("I II III IV V VI VII VIII IX X XI XII".split(), 1)}
    for l in LANGS:
        T = json.load(open(os.path.join(H, "..", "data", f"{l}_titles.json"), encoding="utf-8"))
        hints = {}
        for c in CHUNKS:
            S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
            for k, v in S.items():
                no = k.split(".")[0]
                if no not in T: continue
                if k.endswith(".title"): hints[k] = T[no]["title"]
                elif k.endswith(".h"):
                    m = re.match(r"^(\d+|[IVX]+)\.\s+", v)
                    if not m: continue
                    s = str(int(m.group(1)) if m.group(1).isdigit() else ROM.get(m.group(1), 0))
                    z = T[no]["sec"].get(s)
                    if z: hints[k] = f"{m.group(1)}. {z}"
        json.dump(hints, open(os.path.join(H, "work", f"title_hints_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    ch = {x["id"]: x["papers"] for x in json.load(open(os.path.join(H, "src", "chunks.json"), encoding="utf-8"))}
    print("chunk | papers | words | boxes | inline | es box auto/todo, inline auto | fr | pt")
    for r in rows:
        print(f"{r['c']} | {ch[r['c']]} | {r['words']} | {r['box']} | {r['inline']} | "
              + " | ".join(f"{r[l][0]}/{r[l][1]}, {r[l][2]}" for l in LANGS))
    for l in LANGS:
        s = stats[l]
        print(f"{l}: quotation boxes auto {s[0]} · by hand {s[1]} · inline quotations auto-suggested {s[2]}/{s[3]}")


main()
