# -*- coding: utf-8 -*-
# 역주 해설(commentary) 메뉴: 인용 자동 맞추기 + 번역 도우미 작업 파일 만들기 (모형: ../cosmology/prep.py)
#   python prep.py            (src/ 가 바뀌면 다시 돌린다; <l>/ 번역본은 건드리지 않음)
# 결과
#   auto_<l>.json             블록 인용 중 자동으로 잘라 온 것 {"p001.s0.b1": "공식 번역 인용"}
#   work/src_cNN.json         번역할 단위(블록 인용 제외: 문자열·표·foot) — 세 언어 공용, 읽기 전용
#   work/todo_<l>_cNN.json    손으로 잘라야 할 블록 인용 {"키": {"cit", "en", "verse", "why"}}
#   work/inline_<l>_cNN.json  산문 속 ⟦Q⟧ 인용 {"키": [{"cit", "en", "verse", "auto"?}]} — auto 는 문장 단위로 맞춘 후보
#   work/papers_<l>_cNN.json  편마다 공식 편 제목·장 제목, foot(서명) 원문 절 {"p001": {"title", "sec", "foot_ref", "foot_verse"}}
# 블록 인용 맞추기: 절 전체 인용 → 공식 절 전체.
#   그 밖은 영어 인용을 ' … ' 토막으로 나누어 영어 절의 몇 번째 문장들인지 찾고, 공식 절의 문장 수가 같으면 같은 번째 문장을 가져온다.
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
SK = json.load(open(os.path.join(H, "src", "skeleton.json"), encoding="utf-8"))
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
W = lambda s: re.sub(r"\W+", "", s).lower()
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧")
LANGS = ("es", "fr", "pt")


def alias(l, cit):
    """공식 번역 data 는 121:8.12–14 의 번호가 영어(en.json)와 돌아가 있다(번역 8.12 = 영어 8.14 [Acknowledgment…],
       번역 8.13 = 영어 8.12, 번역 8.14 = 영어 8.13). 영어 번호 → 번역 data 키."""
    if cit in ("121:8.12", "121:8.13", "121:8.14") and amq.text(l, "121:8.12").lstrip().startswith("["):
        return {"121:8.12": "121:8.13", "121:8.13": "121:8.14", "121:8.14": "121:8.12"}[cit]
    return cit


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
    if cit not in EN: return None, "bad citation"
    tv = amq.text(l, alias(l, cit))
    if W(q) == W(EN[cit]): return tv, None
    es, ts = sents(EN[cit]), sents(tv)
    if len(es) != len(ts): return None, f"sentence count en {len(es)} vs {l} {len(ts)}"
    out = []
    for seg in re.split(r"\s*(?:…|\.\.\.)\s*", q):
        if not W(seg): continue
        sp = span(seg.strip(), es)
        if not sp: return None, "partial sentence"
        out.append(" ".join(ts[sp[0]:sp[1] + 1]))
    r = " … ".join(out)
    x = (len(r) / len(q)) / (len(tv) / len(EN[cit]))
    if not 0.7 <= x <= 1.4: return None, f"length mismatch {x:.2f}"
    return r, None


def main():
    stats = {l: [0, 0, 0, 0] for l in LANGS}   # block auto, block by hand, inline total, inline with auto candidate
    auto = {l: {} for l in LANGS}
    rows = []
    for c, papers in SK["chunks"].items():
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        P = {k: v for k, v in S.items() if not (isinstance(v, dict) and "q" in v)}
        json.dump(P, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        row = [c, len(P), sum(1 for v in S.values() if isinstance(v, dict) and "q" in v)]
        for l in LANGS:
            todo, inl, pap = {}, {}, {}
            for k, v in S.items():
                if isinstance(v, dict) and "q" in v:
                    r, why = align(l, v["q"], v["cit"])
                    if r is not None and amq.check(l, alias(l, v["cit"]), r):
                        auto[l][k] = r; stats[l][0] += 1
                    else:
                        todo[k] = {"cit": v["cit"], "en": v["q"], "verse": amq.text(l, alias(l, v["cit"])) if v["cit"] in EN else "",
                                   "why": why or "check failed"}
                        stats[l][1] += 1
                elif isinstance(v, str):
                    for m in MARK.finditer(v):
                        e = {"cit": m.group(1), "en": m.group(2), "verse": amq.text(l, alias(l, m.group(1)))}
                        stats[l][2] += 1
                        r, _ = align(l, m.group(2), m.group(1))
                        if r is not None and amq.check(l, alias(l, m.group(1)), r):
                            e["auto"] = r; stats[l][3] += 1
                        inl.setdefault(k, []).append(e)
            for p in papers:
                n = int(p[1:])
                ref = SK["papers"][p].get("foot_ref") or ""
                pap[p] = {"title": amq.title(l, n), "sec": {s: t for s, t in amq._TT[l][str(n)]["sec"].items() if t},
                          "foot_ref": ref, "foot_verse": amq.text(l, alias(l, ref)) if ref else ""}
            json.dump(todo, open(os.path.join(H, "work", f"todo_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            json.dump(inl, open(os.path.join(H, "work", f"inline_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            json.dump(pap, open(os.path.join(H, "work", f"papers_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            row += [row[2] - len(todo), len(todo)]
        rows.append(row)
        print(c, f"{papers[0]}-{papers[-1]}", "units to translate", len(P), "block quotations", row[2],
              " ".join(f"{l} auto {row[3 + 2 * i]} todo {row[4 + 2 * i]}" for i, l in enumerate(LANGS)))
    for l in LANGS:
        json.dump(auto[l], open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(l, "block quotations auto", stats[l][0], "by hand", stats[l][1],
              "· inline quotations", stats[l][2], "(auto candidate for", stats[l][3], ")")


main()
