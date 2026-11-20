# -*- coding: utf-8 -*-
# 용어집 표제어의 공식 번역어 후보 찾기 (보조 도구, 사이트에는 쓰지 않음)
#   1) 극동판 영어 용어집(site/en/glossary/index.html)의 G 를 glossary_en.json 으로 저장
#   2) 각 영어 표제어가 나오는 영어 절(en.json)을 찾고, 같은 절의 es/fr/pt 공식 번역에서
#      자주 함께 나오면서 책 전체에서는 드문 낱말 묶음(1~4 낱말)을 후보로 뽑아 candidates.json 에 저장
#   결과: candidates.json = {영어 표제어: {"n": 절 수, "refs": [...], "es": [[후보, 점수], …], "fr": …, "pt": …}}
import json, math, os, re, sys, unicodedata
from collections import Counter

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(H)
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\glossary\index.html"
ENJ = r"E:\OneDrive\유란시아 작업\theology-book\en.json"

t = open(FE, encoding="utf-8").read()
i = t.index("var G="); j = t.index("];", i) + 2
G = json.loads(t[i + 6:j - 1])
json.dump(G, open(os.path.join(H, "glossary_en.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
EN = json.load(open(ENJ, encoding="utf-8"))
KEYS = list(EN)

WORD = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿŒœ]+(?:[’'-][A-Za-zÀ-ÖØ-öø-ÿŒœ]+)*")
STOP = set("""a o os as e é de do da dos das em no na nos nas um uma uns umas que se por para com ao aos à às pelo pela pelos pelas seu sua seus suas
el la los las lo y en del al un una unos unas que se por para con su sus es son fue
le la les l d de du des et en un une au aux à que qui se par pour avec son sa ses est sont dans sur ce cette ces
""".split())


def fold(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn").lower()


def grams(text):
    w = [m.group(0) for m in WORD.finditer(text)]
    out = set()
    for n in range(1, 5):
        for k in range(len(w) - n + 1):
            g = w[k:k + n]
            if g[0].lower() in STOP or g[-1].lower() in STOP: continue
            out.add(" ".join(g))
    return out


def en_pat(term):
    base = re.sub(r"\s*\(.*?\)\s*", " ", term).strip()
    base = re.split(r"\s*[,;/]\s*", base)[0].strip()
    if not base: return None
    e = re.escape(base).replace(r"\ ", r"\s+")
    flags = 0 if base[:1].isupper() else re.I
    return re.compile(r"(?<![A-Za-z])" + e + r"(?:s|es|’s|'s)?(?![A-Za-z])", flags)


def main():
    cands = {}
    pats = [(g[0], en_pat(g[0])) for g in G]
    refs = {}
    for term, p in pats:
        r = []
        if p:
            for k in KEYS:
                if p.search(EN[k]):
                    r.append(k)
        refs[term] = r
        cands[term] = {"n": len(r), "refs": r[:4]}
    for l in ("es", "fr", "pt"):
        D = json.load(open(os.path.join(TOOLS, "data", f"{l}.json"), encoding="utf-8"))
        VG = {k: grams(v) for k, v in D.items()}
        df = Counter()
        for s in VG.values(): df.update(s)
        N = len(VG)
        for term, _ in pats:
            r = [k for k in refs[term] if k in VG][:40]
            if not r:
                cands[term][l] = []; continue
            c = Counter()
            for k in r: c.update(VG[k])
            ft = fold(re.sub(r"\(.*?\)", "", term))
            sc = []
            for g, k in c.items():
                if k < max(1, 0.5 * len(r)): continue
                idf = math.log((N + 1) / df[g])
                sim = 0
                fg = fold(g)
                if ft[:3] and fg[:3] == ft[:3]: sim = 1.5
                s = (k / len(r)) * idf * (1 + sim) * (1 + 0.15 * min(g.count(" "), 2))
                sc.append((round(s, 2), g))
            sc.sort(reverse=True)
            cands[term][l] = [[g, s] for s, g in sc[:4]]
        print(l, "done")
    json.dump(cands, open(os.path.join(H, "candidates.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=0)
    print("terms:", len(G), "with refs:", sum(1 for v in cands.values() if v["n"]))


if __name__ == "__main__":
    main()
