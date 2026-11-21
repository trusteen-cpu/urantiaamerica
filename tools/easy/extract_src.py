# -*- coding: utf-8 -*-
# 읽기 쉬운 해설판(Easy-Reading Commentary Edition) 스페인어·프랑스어·포르투갈어판 — 번역 단위 뽑기
#   극동판 tools/zh/easy/ 를 옮긴 것. 극동판 파일은 읽기만 한다.
#   python extract_src.py
#   원고: 극동판 tools/zh/easy/src/cNN.json (영어 단위, ⟦Q⟧ 인용 표시·절 번호 고침 반영됨 — 그대로 쓴다)
#         극동판 tools/easy_en/data/NNN.json · src/NNN.json (문단 전체, 절 제목) → 번역하지 않는 칸 가려내기
#   결과: src/cNN.json  영어 단위, 편 범위로 약 12,000~16,000 낱말씩 다시 나눔 (키는 그대로 "NNN:문단번호", 화면 글자 "ui.*" 는 c01)
#         src/chunks.json  조각 목록
#         fixed_<l>.json   번역하지 않고 자동으로 채우는 칸: 편 제목, 고정 제목(Introduction 등), 공식 절 제목(tools/data/<l>_titles.json),
#                          숫자·기호만 있는 칸
#   검사: 단위 + 고정 칸 = 영어 docx 의 모든 글 문단 / ⟦Q⟧ 인용의 영어가 en.json[절] 에 있는지(대소문자·따옴표 무시)
import glob, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
EASY_EN = os.path.join(FE, "tools", "easy_en")
ZH_SRC = os.path.join(FE, "tools", "zh", "easy", "src")
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
# en.json 은 121:8.12~14 가 밀려 있다(12=표준 13, 13=표준 14, 14=표준 12). tools/data/<l>.json 은 표준 번호이므로 여기서 바로잡는다.
EN["121:8.12"], EN["121:8.13"], EN["121:8.14"] = EN["121:8.14"], EN["121:8.12"], EN["121:8.13"]
LANGS = ("es", "fr", "pt")
TITLES = {l: json.load(open(os.path.join(ROOT, "tools", "data", f"{l}_titles.json"), encoding="utf-8")) for l in LANGS}
LO, HI, TARGET = 12000, 16000, 14000

# 고정 제목 (번역자가 아니라 이 표가 정한다 — 바꾸려면 여기서 고치고 다시 돌린다)
#   fr·pt 는 머리말(Foreword)이 공식 번역에서 Introduction / Introdução 이므로, 각 편 첫머리 "Introduction" 은 Présentation / Apresentação 로 구별한다.
PAPER = {"es": "Documento {n}: {t}", "fr": "Fascicule {n} : {t}", "pt": "Documento {n}: {t}"}
GLANCE = {"es": "El documento {n} de un vistazo", "fr": "Le fascicule {n} en un coup d’œil", "pt": "O documento {n} em resumo"}
FIXED_WORDS = {
    "Introduction": {"es": "Introducción", "fr": "Présentation", "pt": "Apresentação"},
    "Main Text": {"es": "Texto principal", "fr": "Texte principal", "pt": "Texto principal"},
    "Conclusion": {"es": "Conclusión", "fr": "Conclusion", "pt": "Conclusão"},
    "Section": {"es": "Sección", "fr": "Section", "pt": "Seção"},
    "Key message": {"es": "Mensaje clave", "fr": "Message clé", "pt": "Mensagem central"},
    "The Foreword at a Glance": {"es": "El Prólogo de un vistazo", "fr": "L’Introduction en un coup d’œil", "pt": "A Introdução em resumo"},
}


# 극동판 src 의 인용 표시가 잘못 걸린 곳(두 따옴표 사이의 산문을 감쌌음) — 바로잡는다
MARKER_FIX = {
    "073:49": ('these are the "four heads"⟦Q 73:3.4⟧ of the river that⟦/Q⟧ "went out" of Eden',
               'these are the "⟦Q 73:3.4⟧four heads⟦/Q⟧" of the river that "went out" of Eden'),
    "137:33": ('"Can any good thing come out of Nazareth?"⟦Q 137:2.6⟧ but Philip said⟦/Q⟧, "Come and see"',
               '"Can any good thing come out of Nazareth?" but Philip said, "⟦Q 137:2.6⟧Come and see⟦/Q⟧"'),
}


def title(l, no):
    t = TITLES[l][str(no)]["title"]
    return t if no == 0 else PAPER[l].format(n=no, t=t)


def sec(l, no, num): return TITLES[l][str(no)]["sec"][num]


def plain(s): return re.sub(r"⟦/?Q[^⟧]*⟧", "", s)
def words(s): return len(plain(s).replace("**", "").split())


def main():
    src = {}
    for f in sorted(glob.glob(os.path.join(ZH_SRC, "c*.json"))): src.update(json.load(open(f, encoding="utf-8")))
    for k, (a, b) in MARKER_FIX.items():
        assert a in src[k], k
        src[k] = src[k].replace(a, b)
    ui = {k: v for k, v in src.items() if k.startswith("ui.")}
    fixed = {l: {} for l in LANGS}
    papers, problems = [], []
    for no in range(197):
        s = json.load(open(os.path.join(EASY_EN, "src", f"{no:03d}.json"), encoding="utf-8"))
        d = json.load(open(os.path.join(EASY_EN, "data", f"{no:03d}.json"), encoding="utf-8"))
        secs = s["sections_en"]
        full = {v.strip(): k for k, v in secs.items()}
        bare = {re.sub(r"^\S+\.\s*", "", v).strip(): k for k, v in secs.items()}
        t0 = "Foreword" if no == 0 else f"Paper {no}: {s['title_en']}"
        units = {}
        for i in sorted(d, key=int):
            v = d[i]; key = f"{no:03d}:{i}"; p = v.replace("**", "").strip()
            # 극동판 extract_easy_zh.py 와 같은 순서로 가려낸다
            for l in LANGS:
                if p == t0: x = title(l, no)
                elif p in FIXED_WORDS: x = FIXED_WORDS[p][l]
                elif re.fullmatch(r"Paper %d at a Glance" % no, p): x = GLANCE[l].format(n=no)
                elif p in full: x = (p.split(" ", 1)[0] + " " + sec(l, no, full[p]))
                elif p in bare and len(p) > 3: x = sec(l, no, bare[p])
                elif not re.search(r"[A-Za-z]", v): x = v
                else: x = None
                if x is not None: fixed[l][key] = x
            if key in fixed["es"]:
                if key in src: problems.append(f"{key}: fixed but also in zh src")
            elif key in src: units[key] = src[key]
            else: problems.append(f"{key}: not in zh src")
        papers.append((no, units))
    # 인용 표시 검사: 영어 인용이 그 절 영어에 있는지
    QM = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧", re.S)
    W = lambda x: re.sub(r"[^a-z0-9]+", "", x.lower())
    nq, badq = 0, []
    for no, u in papers:
        for k, v in u.items():
            for c, q in QM.findall(v):
                nq += 1
                if c not in EN: badq.append(f"{k} [{c}] citation not in en.json"); continue
                if not all(W(p) in W(EN[c]) for p in re.split(r"…|\.\.\.", q.replace("**", "")) if W(p)):
                    badq.append(f"{k} [{c}] {q[:70]}")
    # 조각 나누기: 편 단위, 약 TARGET 낱말
    chunks, cur, w = [], [], 0
    for no, u in papers:
        pw = sum(words(x) for x in u.values())
        if cur and w + pw > HI and w >= LO: chunks.append(cur); cur, w = [], 0
        cur.append((no, u)); w += pw
        if w >= TARGET: chunks.append(cur); cur, w = [], 0
    if cur:
        if chunks and w < LO * 0.5: chunks[-1] += cur
        else: chunks.append(cur)
    for f in glob.glob(os.path.join(H, "src", "c*.json")): os.remove(f)
    rep = []
    for n, ch in enumerate(chunks, 1):
        cid = "c%02d" % n
        D = dict(ui) if n == 1 else {}
        for no, u in ch: D.update(u)
        json.dump(D, open(os.path.join(H, "src", cid + ".json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        rep.append({"id": cid, "papers": f"{ch[0][0]:03d}–{ch[-1][0]:03d}", "words": sum(words(x) for x in D.values()),
                    "units": len(D), "quotes": sum(x.count("⟦Q ") for x in D.values())})
    json.dump(rep, open(os.path.join(H, "src", "chunks.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for l in LANGS:
        json.dump(fixed[l], open(os.path.join(H, f"fixed_{l}.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    for r in rep: print(r)
    print("units", sum(r["units"] for r in rep), "· fixed", len(fixed["es"]), "· words", sum(r["words"] for r in rep), "· quotations", nq)
    for p in problems[:20]: print("  PROBLEM", p)
    print("quotation markers whose English is not in en.json:", len(badq))
    for b in badq: print("  ", b)


main()
