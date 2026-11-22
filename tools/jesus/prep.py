# -*- coding: utf-8 -*-
# 예수 연구 메뉴: 유란시아서 인용 자동 맞추기 + 번역 도우미 작업 파일 만들기
#   python prep.py            (src/ 가 바뀌면 다시 돌린다; <l>/ 번역본은 건드리지 않음)
# 결과
#   auto_<l>.json            자동으로 잘라 온 인용 {"키": 문자열 또는 [토막,…]}
#   work/src_cNN.json         번역할 단위(인용 dict 제외) — 세 언어 공용, 읽기 전용
#   work/todo_<l>_cNN.json    손으로 잘라야 할 인용 {"키": {"cit", "en", "verse", "why"}}
#   work/inline_<l>_cNN.json  산문 속 ⟦Q⟧ 인용 {"키": [{"cit", "en", "auto"?, "verse"}]} — 번역할 때 참고
# 인용 종류
#   speech (담화의 예수 말씀): 영어 문단을 따옴표로 자른 토막 중 고른 것 → 공식 문단을 « »(es·fr) / “ ”(pt)로 같은 수로 자르고
#                            같은 번째 토막을 가져온다(목록으로 저장, 화면에서는 공백으로 잇는다). 토막 수가 다르면 todo.
#   run (가르침의 유란시아서 인용 문단): 문단 전체면 공식 문단 전체. 몇 문장만이면 공식 문단의 문장 수가 같을 때 같은 번째 문장
#                            (앞뒤 생략은 …), 다르면 공식 문단 전체(극동판 한국어판과 같은 규칙). todo 없음.
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, ".."))
import amq  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
SK = json.load(open(os.path.join(H, "src", "skeleton.json"), encoding="utf-8"))
SPLIT = re.compile(r"(?<=[.!?;:])[\"”’»)]*\s+(?=[\"“‘«(¿¡—–-]?\s?[A-ZÀ-ÖØ-Þ0-9])")
RSPLIT = re.compile(r"(?<=[.?!])[\"”’»\)]*\s+(?=[\"“‘«(¿¡—–]*\s?[A-ZÀ-ÖØ-Þ0-9])")   # sentence split for 'run' cuts
W = lambda s: re.sub(r"\W+", "", s).lower()
N = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧")
OPEN = {"es": "«", "fr": "«", "pt": "“"}; CLOSE = {"es": "»", "fr": "»", "pt": "”"}
LANGS = ("es", "fr", "pt")


def sents(t, rx=SPLIT):
    out, pos = [], 0
    for m in rx.finditer(t):
        out.append(t[pos:m.end()].strip()); pos = m.end()
    out.append(t[pos:].strip())
    return [s for s in out if s]


def pieces_en(t):
    t = t.replace("“", '"').replace("”", '"')
    out, last, ins = [], 0, False
    for m in re.finditer('"', t):
        out.append(t[last:m.start()]); ins = not ins; last = m.end()
    out.append(t[last:]); return out


def pieces_l(l, t):
    out, last = [], 0
    for m in re.finditer("[%s%s]" % (OPEN[l], CLOSE[l]), t):
        out.append(t[last:m.start()]); last = m.end()
    out.append(t[last:]); return out


def speech(l, q, cit):
    ps = pieces_en(EN[cit]); target = N(q); pos = 0; sel = []
    for i, p in enumerate(ps):
        n = N(p)
        if n and target.startswith(n, pos): sel.append(i); pos += len(n)
    if pos != len(target): return None, "speech not found in the English paragraph"
    lp = pieces_l(l, amq.text(l, cit))
    if len(lp) != len(ps): return None, f"quotation marks: English {len(ps) - 1} vs {l} {len(lp) - 1}"
    out = [lp[i].strip() for i in sel if lp[i].strip()]
    return out, None


def run(l, v):
    t = amq.text(l, v["cit"])
    if not v["rng"]: return t
    a, b, n = v["rng"]
    ss = sents(t, RSPLIT)
    if len(ss) != n: return t                    # sentence counts differ → whole official paragraph
    r = " ".join(ss[a:b + 1])
    return ("… " if a > 0 else "") + r + (" …" if b < n - 1 else "")


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


def inline_auto(l, en, cit):
    a, b = sents(EN[cit]), sents(amq.text(l, cit))
    if len(a) != len(b): return None
    sp = span(en, a)
    return " ".join(b[sp[0]:sp[1] + 1]) if sp else None


def qcheck(l, text, cit):
    hay = re.sub(r"\s+", "", amq.text(l, cit))
    parts = text if isinstance(text, list) else re.split(r"…", text)
    return all(re.sub(r"\s+", "", p) in hay for p in parts if p.strip())


def main():
    stats = {l: dict(speech=[0, 0], run=[0, 0], inline=[0, 0]) for l in LANGS}
    auto = {l: {} for l in LANGS}
    os.makedirs(os.path.join(H, "work"), exist_ok=True)
    for c in SK["chunks"]:
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        P = {k: v for k, v in S.items() if not isinstance(v, dict)}
        json.dump(P, open(os.path.join(H, "work", f"src_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        line = []
        for l in LANGS:
            todo, inl = {}, {}
            for k, v in S.items():
                if isinstance(v, dict):
                    if v["kind"] == "speech":
                        r, why = speech(l, v["q"], v["cit"])
                        if r is not None and not qcheck(l, r, v["cit"]): r, why = None, "check failed"
                        if r is not None: auto[l][k] = r; stats[l]["speech"][0] += 1
                        else:
                            todo[k] = {"cit": v["cit"], "en": v["q"], "verse": amq.text(l, v["cit"]), "why": why}
                            stats[l]["speech"][1] += 1
                    else:
                        r = run(l, v)
                        assert qcheck(l, r, v["cit"]), (k, r)
                        auto[l][k] = r; stats[l]["run"][0 if (not v["rng"] or r != amq.text(l, v["cit"])) else 1] += 1
                    continue
                for m in MARK.finditer(v):
                    e = {"cit": m.group(1), "en": m.group(2)}
                    a = inline_auto(l, m.group(2), m.group(1))
                    if a and qcheck(l, a, m.group(1)): e["auto"] = a; stats[l]["inline"][0] += 1
                    else: stats[l]["inline"][1] += 1
                    e["verse"] = amq.text(l, m.group(1))
                    inl.setdefault(k, []).append(e)
            json.dump(todo, open(os.path.join(H, "work", f"todo_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            json.dump(inl, open(os.path.join(H, "work", f"inline_{l}_{c}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
            line.append(f"{l} todo {len(todo)}")
        words = sum(len(re.sub(r"⟦/?Q[^⟧]*⟧", "", v).split()) for v in P.values())
        print(c, "prose units", len(P), "words", words, "quotations", len(S) - len(P), " ".join(line))
    for l in LANGS:
        json.dump(auto[l], open(os.path.join(H, f"auto_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        s = stats[l]
        print(f"{l}: speech auto {s['speech'][0]} / by hand {s['speech'][1]} · runs {s['run'][0]} exact + {s['run'][1]} "
              f"whole paragraph instead of a partial cut · inline quotations with an automatic suggestion {s['inline'][0]}, "
              f"to cut by the translator {s['inline'][1]}")


main()
