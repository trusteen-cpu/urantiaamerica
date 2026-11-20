# -*- coding: utf-8 -*-
# 「Theology of The Urantia Book」 스페인어·프랑스어·포르투갈어판 → site/<es|fr|pt>/theology/
#   (차례 index.html + 장마다 ch01~ch37.html, 영어판 urantiafareast site/en/theology/ 와 같은 짜임)
#   틀(CSS·head·chapter·index)은 극동판 tools/build_theology.py 를 exec 로 빌려 쓴다(읽기만, main() 실행 안 함).
#   원고:  src/cNN.json            영어 단위 (extract_src.py 가 theology-book 에서 뽑음; 극동판 zh 원고와 같음)
#          <l>/cNN.json            같은 키의 번역 (글 단위만; ui.* 와 인용은 없음)
#          인용 = 공식 번역에서 글자 그대로:  <l>/quotes_cNN.json (손으로 자른 것) > auto_<l>.json (align_quotes.py)
#   검사(하나라도 걸리면 쓰지 않음): 키 같음·빈 값 없음·한글 없음·영어 그대로 남은 값 없음·모든 인용 amq.check(절 전체는 완전히 같음)
#          · 장·절·단위·인용·질문 수 영어와 같음 · 쪽마다 lang·/home-button.js·/en/ 링크 없음
#   실행: python build_theology_am.py [es fr pt]          (모두 검사 후 site 에 씀)
#         python build_theology_am.py es --chunk c03       (그 묶음만 검사, 쓰지 않음 — 도우미용)
import glob, json, os, re, sys, types

sys.dont_write_bytecode = True
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.normpath(os.path.join(H, ".."))
SITE = os.path.normpath(os.path.join(TOOLS, "..", "site"))
FE_BUILDER = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\tools\build_theology.py"
sys.path.insert(0, TOOLS)
import amq  # noqa: E402

HANGUL = re.compile(r"[\u1100-\u11ff\u3130-\u318f\uac00-\ud7af]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their)\b")
ELL = " … "
ROMAN = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI", 7: "VII", 8: "VIII"}
FONT = "Georgia,'Times New Roman',serif"
SANS = "'Segoe UI',system-ui,sans-serif"

UI = {
    "es": dict(ch="Capítulo {}", part="Parte {}:", summ="EN ESTE CAPÍTULO", qs="Preguntas para la reflexión", toc="Índice",
               preface="Prefacio", prev="← Anterior", next="Siguiente →", contents="Índice", eyebrow_index="EL LIBRO DE URANTIA",
               note="Las citas se reproducen textualmente de la traducción oficial al español de El libro de Urantia (Urantia Foundation). "
                    "Haga clic en una referencia para abrir el texto."),
    "fr": dict(ch="Chapitre {}", part="Partie {} :", summ="DANS CE CHAPITRE", qs="Questions pour la réflexion", toc="Table des matières",
               preface="Préface", prev="← Précédent", next="Suivant →", contents="Table des matières", eyebrow_index="LE LIVRE D’URANTIA",
               note="Les citations sont reprises mot pour mot de la traduction française officielle du Livre d’Urantia (Fondation Urantia). "
                    "Cliquez sur une référence pour ouvrir le texte."),
    "pt": dict(ch="Capítulo {}", part="Parte {}:", summ="NESTE CAPÍTULO", qs="Perguntas para reflexão", toc="Sumário",
               preface="Prefácio", prev="← Anterior", next="Próximo →", contents="Sumário", eyebrow_index="O LIVRO DE URÂNTIA",
               note="As citações são reproduzidas literalmente da tradução oficial em português de O Livro de Urântia (Urantia Foundation). "
                    "Clique em uma referência para abrir o texto."),
}

# ── 영어 빌더 빌려 오기 ─────────────────────────────────
_code = open(FE_BUILDER, encoding="utf-8").read()
NS = {"__file__": FE_BUILDER, "__name__": "theology_en_builder"}
exec(_code.split("\ndef main():")[0], NS)          # CSS, head, chapter, index, TS, FR … (쓰기 없음)
TS0 = NS["TS"]
esc = NS["esc"]

# ── 영어 원고 ───────────────────────────────────────────
CHUNKS = sorted(os.path.basename(f)[:-5] for f in glob.glob(os.path.join(H, "src", "c[0-9][0-9].json")))
SRCC = {c: json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8")) for c in CHUNKS}
SRC = {k: v for c in CHUNKS for k, v in SRCC[c].items()}
PARTNO = {int(k): v for k, v in json.load(open(os.path.join(H, "src", "parts.json"), encoding="utf-8")).items()}


def qitems(k, v):
    refs = v["cit"] if isinstance(v["cit"], list) else [v["cit"]]
    return [(f"{k}#{i}", r, t) for i, (r, t) in enumerate(zip(refs, v["text"]))]


def fr_nb(s):
    """프랑스어 문장부호: ; : ! ? » 앞과 « 뒤 공백을 줄바꿈 없는 공백으로 (번역 글에만; 인용문은 공식 그대로)."""
    s = re.sub(r" ([;:!?»])", "\u00a0\\1", s)
    return s.replace("« ", "«\u00a0")


def check(l, chunks):
    """chunks 의 번역·인용을 검사. (T 글 단위 사전, Q 인용 사전, 오류 목록, 경고 목록)"""
    err, warn, T, Q = [], [], {}, {}
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    for c in chunks:
        S = SRCC[c]
        p = os.path.join(H, l, c + ".json")
        D = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
        if not D: err.append(f"{l}/{c}.json missing or empty")
        mp = os.path.join(H, l, f"quotes_{c}.json")
        M = json.load(open(mp, encoding="utf-8")) if os.path.exists(mp) else {}
        want = [k for k, v in S.items() if isinstance(v, str) and not k.startswith("ui.")]
        miss = [k for k in want if k not in D]
        extra = [k for k in D if k not in want]
        if miss: err.append(f"{c}: missing {len(miss)} units, e.g. {miss[:6]}")
        if extra: err.append(f"{c}: extra keys {extra[:6]}")
        for k in want:
            z = D.get(k)
            if z is None: continue
            e = S[k]
            if not isinstance(z, str) or not z.strip(): err.append(f"{k}: empty / not a string"); continue
            if HANGUL.search(z): err.append(f"{k}: Hangul")
            if z.strip() == e.strip() and len(e.split()) >= 3: err.append(f"{k}: identical to English")
            n_en = len(ENGW.findall(z))
            if n_en >= 3: err.append(f"{k}: looks English ({n_en} English function words)")
            if "\n" in e or "\n" in z:
                if e.count("\n") != z.count("\n"): warn.append(f"{k}: line breaks differ")
            r = len(z) / max(1, len(e))
            if len(e) > 80 and not 0.75 <= r <= 1.9: warn.append(f"{k}: length ratio {r:.2f}")
            T[k] = z
        mk = set()
        for k, v in S.items():
            if not isinstance(v, dict): continue
            for key, r, t in qitems(k, v):
                mk.add(key)
                q = M.get(key, auto.get(key))
                if q is None: err.append(f"quote {key} [{r}]: not cut yet"); continue
                if v["whole"]:
                    if re.sub(r"\s+", "", q) != re.sub(r"\s+", "", amq.text(l, r)): err.append(f"quote {key} [{r}]: whole verse expected")
                elif not amq.check(l, r, q):
                    err.append(f"quote {key} [{r}]: NOT verbatim in {l}.json")
                if HANGUL.search(q): err.append(f"quote {key}: Hangul")
                if not v["whole"] and q.count("…") != t.count("…"):
                    warn.append(f"quote {key}: {t.count('…')} omissions in English, {q.count('…')} in {l}")
                Q[key] = q
        bad = [k for k in M if k not in mk]
        if bad: err.append(f"{l}/quotes_{c}.json: unknown keys {bad[:5]}")
    return T, Q, err, warn


def build(l):
    T, Q, err, warn = check(l, CHUNKS)
    nq = len(Q)
    print(f"[{l}] units {len(T)}, quotation items {nq}, errors {len(err)}, warnings {len(warn)}")
    for x in err[:40]: print("   ·", x)
    if err: return False
    U = UI[l]
    if l == "fr": T = {k: fr_nb(v) for k, v in T.items()}
    g = lambda k: T[k]

    class PartFmt(str):
        def format(self, n): return str.replace(self, "{}", ROMAN[n])

    L = dict(lang=l, ch=U["ch"], part=PartFmt(U["part"]), summ=U["summ"], qs=U["qs"], toc=U["toc"], preface=U["preface"],
             prev=U["prev"], next=U["next"], contents=U["contents"], font=FONT, sans=SANS,
             fonts="family=Source+Serif+4:wght@400;700", cite=lambda r: amq.link(l, r), note=U["note"])
    NS["UI"] = {"ko": L}                          # 영어 빌더의 'ko' 갈래(부·장 표시 틀)를 이 언어로 쓴다
    npre = sum(1 for k in SRC if k.startswith("front.preface"))
    parts = {n: (g(f"part.{n}"), SRC[f"part.{n}"]) for n in range(1, 9)}
    NS["FR"] = types.SimpleNamespace(TITLE={"ko": g("front.title")}, SUB={"ko": g("front.sub")}, AUTHOR={"ko": g("front.author")},
                                     PREFACE={"ko": [g(f"front.preface{i}") for i in range(1, npre + 1)]}, PARTS=parts)
    NS["TS"] = types.SimpleNamespace(ACC=TS0.ACC, NUMW=TS0.NUMW, ref_label=TS0.ref_label,
                                     quote_text=lambda lang, ref, txt: list(txt))   # 인용은 이미 잘라 온 공식 번역

    def build_ch(no):
        p = f"ch{no:02d}"; secs = []; si = 1
        while f"{p}.s{si}" in SRC:
            units = []; ui = 1
            while f"{p}.s{si}.u{ui}.k" in SRC:
                b = f"{p}.s{si}.u{ui}"; qs = []; qi = 1
                while f"{b}.q{qi}" in SRC:
                    v = SRC[f"{b}.q{qi}"]
                    qs.append((v["cit"], [Q[key] for key, _, _ in qitems(f"{b}.q{qi}", v)], None)); qi += 1
                units.append({"ko_k": g(b + ".k"), "ko_p": g(b + ".p"), "q": qs}); ui += 1
            secs.append({"ko": g(f"{p}.s{si}"), "units": units}); si += 1
        qs = []; qi = 1
        while f"{p}.qs{qi}" in SRC: qs.append(g(f"{p}.qs{qi}")); qi += 1
        pn = PARTNO[no]
        return {"no": no, "ko_t": g(p + ".t"), "ko_sub": g(p + ".sub"), "ko_sum": g(p + ".sum"), "secs": secs, "ko_qs": qs,
                "part": {"no": pn, "ko": parts[pn][0], "en": parts[pn][1]}}

    nos = sorted(int(k[2:4]) for k in SRC if re.fullmatch(r"ch\d\d\.t", k))
    chs = [build_ch(n) for n in nos]

    def fix(t):
        t = t.replace('<div class="eb">유란시아서</div>', f'<div class="eb">{esc(U["eyebrow_index"])}</div>')
        t = t.replace("word-break:keep-all", "word-break:normal;hyphens:auto")
        return t

    pages = {}
    for i, ch in enumerate(chs):
        pages[f"ch{ch['no']:02d}.html"] = fix(NS["chapter"]("ko", ch, chs[i - 1] if i else None, chs[i + 1] if i + 1 < len(chs) else None))
    pages["index.html"] = fix(NS["index"]("ko", chs))

    # ── 영어판과 짜임 비교 + 쪽 검사 ───────────────────────
    en_dir = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\theology"
    en_pages = sorted(os.path.basename(f) for f in glob.glob(os.path.join(en_dir, "*.html")))
    if sorted(pages) != en_pages: err.append(f"page list differs from English: {sorted(set(pages) ^ set(en_pages))}")
    for fn, t in pages.items():
        e = open(os.path.join(en_dir, fn), encoding="utf-8").read()
        for tag in ('<h2 class="sec">', '<div class="k">', '<div class="q">', '<div class="u">', "<li>", '<div class="part">', "<a href=\"ch"):
            if e.count(tag) != t.count(tag): err.append(f"{fn}: count of {tag} {t.count(tag)} vs English {e.count(tag)}")
        if HANGUL.search(t): err.append(f"{fn}: Hangul {''.join(HANGUL.findall(t)[:10])}")
        if "/en/" in t: err.append(f"{fn}: /en/ link")
        if f'<html lang="{l}">' not in t or "/home-button.js" not in t: err.append(f"{fn}: lang / home button")
        for h in re.findall(r'href="([^"]+)"', t):
            if not (h == "./" or re.fullmatch(r"ch\d\d\.html", h) or h.startswith(f"/{l}/book/#") or h.startswith("https://fonts.")):
                err.append(f"{fn}: unexpected link {h}")
    nqbox = sum(t.count('<div class="q">') for t in pages.values())
    print(f"     chapters {len(chs)}, sections {sum(len(c['secs']) for c in chs)}, units {sum(len(s['units']) for c in chs for s in c['secs'])}, "
          f"quotation boxes {nqbox}, reflection questions {sum(len(c['ko_qs']) for c in chs)}")
    for x in err[:40]: print("   ·", x)
    if err: return False
    out = os.path.join(SITE, l, "theology")
    os.makedirs(out, exist_ok=True)
    for fn, t in pages.items():
        open(os.path.join(out, fn), "w", encoding="utf-8").write(t)
    print(f"     → {out} ({len(pages)} pages)")
    return True


def main():
    args = [a for a in sys.argv[1:] if a in UI]
    if "--chunk" in sys.argv:
        c = sys.argv[sys.argv.index("--chunk") + 1]
        langs = args or ["es", "fr", "pt"]
        rep = int(sys.argv[sys.argv.index("--report") + 1]) if "--report" in sys.argv else 40
        for l in langs:
            T, Q, err, warn = check(l, [c])
            print(f"[{l} {c}] units {len(T)}, quotation items {len(Q)}, errors {len(err)}, warnings {len(warn)}")
            for x in err[:rep]: print("   ERR ", x)
            for x in warn[:rep]: print("   warn", x)
        return
    ok = all([build(l) for l in (args or ["es", "fr", "pt"])])
    if not ok: raise SystemExit("CHECKS FAILED")
    print("ALL CHECKS PASSED")


main()
