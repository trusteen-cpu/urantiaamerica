# -*- coding: utf-8 -*-
# 청소년판 메뉴: 산문 속 인용(⟦Q P:S.p⟧…⟦/Q⟧) 자동 맞추기 + 번역 도우미 작업 파일 만들기
#   python prep.py            (src/ 가 바뀌면 다시 돌린다; <l>/ 번역본은 건드리지 않음)
# 결과
#   auto_<l>.json               자동으로 잘라 온 인용 {"p1.005#0": "공식 번역 인용"}  (#0 = 그 단위의 몇 번째 인용)
#   work/src_cNN.json            번역할 단위 (ui.* + 편 단위) — 세 언어 공용, 읽기 전용
#   work/quotes_<l>_cNN.json     그 묶음의 모든 인용 {"키": [{"n", "cit", "en", "auto"(없으면 null), "how", "why", "verse"}]}
#                                how: whole(절 전체) · sentence(문장 수 같음) · positional(문장 수가 달라 위치 비율로 맞춤 — 번역자가 눈으로 확인)
#   work/todo_<l>_cNN.json       손으로 잘라야 할 인용만 {"키#n": {"cit", "en", "why"}}
#   work/headings_<l>_cNN.json   소제목 단위와 같은 번호의 공식 장 제목 {"키": {"en", "official": ["장 번호: 제목", …]}}
# 맞추기: 절 전체 인용 → 공식 절 전체. 그 밖은 영어 인용을 ' … ' 토막으로 나누어 영어 절의 몇 번째 문장들인지 찾고,
#   공식 절의 문장 수가 같으면 같은 번째 문장을 가져온다. 문장 수가 다르면 문장 경계의 위치 비율(±4%)이 맞을 때만 가져온다.
#   문장 중간을 자른 인용은 손으로.
#   영어 인용이 문장부호로 끝나지 않으면 공식 문장 끝의 . ; : , 를 떼고, 앞뒤 따옴표(« » “ ” ")는 뗀다(글자 그대로 남음).
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
ST = json.load(open(os.path.join(H, "src", "_structure.json"), encoding="utf-8"))
CHUNKS = sorted(ST["_chunks"])
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
W = lambda s: re.sub(r"\W+", "", s).lower()
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧")
QCH = "«»“”\"‘’'\u00a0 "
LANGS = ("es", "fr", "pt")


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


def tidy(piece, en_piece):
    p = piece.strip(QCH)
    p = re.sub(r"[»”\"’]+[.;:,]*$", "", p).strip(QCH)      # 인용 속 대화의 닫는 따옴표(+마침표)는 뗀다
    if not re.search(r"[.!?;:,]['’”\"]?\s*$", en_piece.strip()):
        p = re.sub(r"[.;:,]+$", "", p).strip(QCH)
    return p


PAIRS = (("«", "»"), ("“", "”"))


def balanced(r):
    """짝 없는 따옴표를 앞뒤에서만 뗀다. 가운데에 짝 없는 따옴표가 남으면 None(손으로)."""
    for o, c in PAIRS:
        if r.count(o) > r.count(c) and r.startswith(o): r = r[1:].lstrip()
        if r.count(c) > r.count(o) and re.search(re.escape(c) + r"[.;:,]*$", r): r = re.sub(re.escape(c) + r"[.;:,]*$", "", r).rstrip()
    return r if all(r.count(o) == r.count(c) for o, c in PAIRS) else None


def bounds(ss):
    """문장마다 (시작 비율, 끝 비율) — 절 전체 글자 수에 대한 위치."""
    tot = sum(len(s) for s in ss); out, a = [], 0
    for s in ss:
        out.append((a / tot, (a + len(s)) / tot)); a += len(s)
    return out


def positional(i, j, es, ts, tol=0.04):
    """문장 수가 다를 때: 영어 문장 i..j 의 시작·끝 위치 비율과 가장 가까운 공식 문장 경계를 찾는다(문장 수가 같고 시작·끝 모두 tol 안일 때만)."""
    be, bt = bounds(es), bounds(ts)
    fs, fe = be[i][0], be[j][1]
    i2 = min(range(len(ts)), key=lambda x: abs(bt[x][0] - fs))
    j2 = min(range(len(ts)), key=lambda x: abs(bt[x][1] - fe))
    if j2 - i2 != j - i or abs(bt[i2][0] - fs) > tol or abs(bt[j2][1] - fe) > tol: return None
    return i2, j2


def align(l, q, cit):
    """돌려줌: (공식 인용 또는 None, 실패 이유 또는 None, 방식 'whole'|'sentence'|'positional')"""
    if cit not in EN: return None, "citation not in book", None
    if W(q) == W(EN[cit]):
        r = balanced(amq.text(l, cit).strip())
        return (r, None, "whole") if r else (None, "unbalanced quotation marks", None)
    es, ts = sents(EN[cit]), sents(amq.text(l, cit))
    how = "sentence" if len(es) == len(ts) else "positional"
    out = []
    for seg in re.split(r"\s*(?:…|\.\.\.)\s*", q):
        if not W(seg): continue
        sp = span(seg.strip().strip(QCH), es)
        if not sp: return None, "partial sentence", None
        if how == "positional":
            sp = positional(sp[0], sp[1], es, ts)
            if not sp: return None, f"sentence count en {len(es)} vs {l} {len(ts)}", None
        out.append(tidy(" ".join(ts[sp[0]:sp[1] + 1]), seg))
    r = balanced(" … ".join(out))
    if r is None: return None, "unbalanced quotation marks", None
    x = (len(r) / max(1, len(q))) / (len(amq.text(l, cit)) / len(EN[cit]))
    if not 0.6 <= x <= 1.6: return None, f"length mismatch {x:.2f}", None
    if not amq.check(l, cit, r): return None, "check failed", None
    return r, None, how


def main():
    os.makedirs(os.path.join(H, "work"), exist_ok=True)
    auto = {l: {} for l in LANGS}
    rows = []
    for c in CHUNKS:
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        json.dump(S, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        kinds = {k: kd for n in ST if n.isdigit() for k, kd in ST[n]["items"]}
        nq = sum(len(MARK.findall(v)) for v in S.values())
        wc = sum(len(re.sub(r"⟦/?Q[^⟧]*⟧", "", v).split()) for v in S.values())
        row = [c, ST["_chunks"][c], wc, nq]
        for l in LANGS:
            qs, todo, hd = {}, {}, {}
            for k, v in S.items():
                for i, m in enumerate(MARK.finditer(v)):
                    cit, en = m.group(1), m.group(2)
                    r, why, how = align(l, en, cit)
                    qs.setdefault(k, []).append({"n": i, "cit": cit, "en": en, "auto": r, "how": how, "why": why,
                                                 "verse": amq.text(l, cit) if cit in EN else None})
                    if r is not None: auto[l][f"{k}#{i}"] = r
                    else: todo[f"{k}#{i}"] = {"cit": cit, "en": en, "why": why}
                if kinds.get(k) == "h":
                    p = int(k[1:].split(".")[0])
                    m = re.match(r"^(\d+(?:,\s*\d+)*)\.", v)
                    off = []
                    for s in (re.split(r",\s*", m.group(1)) if m else []):
                        try: off.append(f"{s}: {amq.title(l, p, int(s))}")
                        except KeyError: pass
                    hd[k] = {"en": v, "official": off}
            json.dump(qs, open(os.path.join(H, "work", f"quotes_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            json.dump(todo, open(os.path.join(H, "work", f"todo_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            json.dump(hd, open(os.path.join(H, "work", f"headings_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            row += [nq - len(todo), len(todo)]
        rows.append(row)
    for l in LANGS:
        json.dump(auto[l], open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("chunk\tcontents\twords\tquotes\tes auto/todo\tfr auto/todo\tpt auto/todo")
    for r in rows:
        print(f"{r[0]}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}/{r[5]}\t{r[6]}/{r[7]}\t{r[8]}/{r[9]}")
    t = [sum(r[i] for r in rows) for i in range(2, 10)]
    print(f"total\t\t{t[0]}\t{t[1]}\t{t[2]}/{t[3]}\t{t[4]}/{t[5]}\t{t[6]}/{t[7]}")


main()
