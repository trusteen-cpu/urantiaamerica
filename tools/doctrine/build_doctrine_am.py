# -*- coding: utf-8 -*-
# 「Core Doctrines of The Urantia Book」 스페인어·프랑스어·포르투갈어판 → site/<es|fr|pt>/doctrine/
#   (index.html · preface.html · ch01~ch32.html · afterword.html, 영어판 urantiafareast site/en/doctrine/ 와 같은 짜임)
#   틀(CSS·head·body·build)은 극동판 tools/build_doctrine.py 를 exec 로 빌려 쓴다(읽기만; 한국어·영어판 만들기와 patch_players 는 실행 안 함).
#   원고:  src/cNN.json             영어 단위 (extract_src.py 가 doctrine-book\en 에서 뽑음; 극동판 zh 원고와 같은 키)
#          <l>/cNN.json             같은 키의 번역 (글·표·질문 상자·part·audio; 인용은 없음)
#          인용 = 공식 번역에서 글자 그대로:  <l>/quotes_cNN.json (손으로 자른 것) > auto_<l>.json (align_quotes.py)
#   검사(하나라도 걸리면 쓰지 않음): 키·모양 같음 · 빈 값 없음 · 한글 없음 · 영어 그대로 남은 값 없음 · 본문 속 절 번호 그대로
#          · 모든 인용 amq.check (절 전체 인용은 절 전체와 같음) · 장·소제목·문단·인용·표·질문 수 영어 쪽과 같음
#          · 쪽마다 lang · /home-button.js · /en/ 링크 없음 · 링크는 /<l>/doctrine/ 안, /<l>/book/#, 영어 오디오북(극동판)만
#   경고: 문단 길이 비율, 인용 길이 비율(자동으로 자른 인용 감사), 줄임표 수.
#   오디오북: 영어 쪽은 /mirror/audiobook-en/NN/ (극동판 사이트에만 있음) → https://fareast.urantiareaders.com/mirror/audiobook-en/NN/ 로 바꾸고
#            "(영어)" 라고 밝힌다. 스페인어·프랑스어·포르투갈어 음성은 없다.
#   실행: python build_doctrine_am.py [es fr pt]                     (모두 검사 후 site 에 씀)
#         python build_doctrine_am.py es --chunk c03 [--report 300]  (그 묶음만 검사, 쓰지 않음 — 도우미용)
#         python build_doctrine_am.py --audit [es]                   (자동 인용 길이 비율 목록)
import glob, json, os, re, shutil, sys

sys.dont_write_bytecode = True
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.normpath(os.path.join(H, ".."))
SITE = os.path.normpath(os.path.join(TOOLS, "..", "site"))
FE_BUILDER = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\tools\build_doctrine.py"
EN_DIR = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\doctrine"
AUDIO_DIR = "https://fareast.urantiareaders.com/mirror/audiobook-en/"
sys.path.insert(0, TOOLS); sys.path.insert(0, H)
import amq  # noqa: E402
import extract_src as X  # noqa: E402

EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
HANGUL = re.compile(r"[\u1100-\u11ff\u3130-\u318f\uac00-\ud7af]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their)\b")
REF = re.compile(r"\d+:\d+\.\d+")
FONT = "Georgia,'Times New Roman',serif"
SANS = "'Segoe UI',system-ui,sans-serif"

UI = {
    "es": dict(title="Doctrinas fundamentales de El libro de Urantia", sub="Su lógica esencial en las palabras del texto",
               by="Jay Han", eb="EL LIBRO DE URANTIA", contents="Índice", prev="← Anterior", next="Siguiente →",
               part="Parte {} —", audio_h="Escuchar el audiolibro (en inglés)",
               audio_series="Audiolibro de las verdades esenciales de El libro de Urantia",
               all_audio="Todos los audiolibros (en inglés)",
               all_audio_note="Audiolibros narrados en inglés que acompañan a este libro. Cada capítulo termina también con un enlace a su audiolibro."),
    "fr": dict(title="Doctrines essentielles du Livre d’Urantia", sub="Leur logique fondamentale dans les mots du texte",
               by="Jay Han", eb="LE LIVRE D’URANTIA", contents="Table des matières", prev="← Précédent", next="Suivant →",
               part="Partie {} —", audio_h="Écouter le livre audio (en anglais)",
               audio_series="Livre audio des vérités essentielles du Livre d’Urantia",
               all_audio="Tous les livres audio (en anglais)",
               all_audio_note="Livres audio lus en anglais qui accompagnent ce livre. Chaque chapitre se termine aussi par un lien vers son livre audio."),
    "pt": dict(title="Doutrinas fundamentais de O Livro de Urântia", sub="Sua lógica essencial nas palavras do texto",
               by="Jay Han", eb="O LIVRO DE URÂNTIA", contents="Sumário", prev="← Anterior", next="Próximo →",
               part="Parte {} —", audio_h="Ouvir o audiolivro (em inglês)",
               audio_series="Audiolivro das verdades essenciais de O Livro de Urântia",
               all_audio="Todos os audiolivros (em inglês)",
               all_audio_note="Audiolivros narrados em inglês que acompanham este livro. Cada capítulo também termina com um link para o seu audiolivro."),
}

CHUNKS = list(X.CHUNKS)
SRCC = {c: json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8")) for c in CHUNKS}
SRC = {k: v for c in CHUNKS for k, v in SRCC[c].items()}
isq = lambda v: isinstance(v, dict) and "cit" in v


def shape(v):
    if isinstance(v, str): return "s"
    if isinstance(v, list): return ["L", [shape(x) for x in v]]
    if isinstance(v, dict): return {k: shape(x) for k, x in v.items()}
    return type(v).__name__


def strings(v):
    if isinstance(v, str): yield v
    elif isinstance(v, list):
        for x in v: yield from strings(x)
    elif isinstance(v, dict):
        for k, x in v.items():
            if k != "cit": yield from strings(x)


def fr_nb(s):
    """프랑스어 문장부호: ; : ! ? » 앞과 « 뒤 공백을 줄바꿈 없는 공백으로 (번역 글에만; 인용문은 공식 그대로)."""
    s = re.sub(r" ([;:!?»])", "\u00a0\\1", s)
    return s.replace("« ", "«\u00a0")


def map_strings(v, f):
    if isinstance(v, str): return f(v)
    if isinstance(v, list): return [map_strings(x, f) for x in v]
    if isinstance(v, dict): return {k: map_strings(x, f) for k, x in v.items()}
    return v


def qratio(l, r, en_q, q):
    """인용 길이 비율 ÷ 절 길이 비율 (1 근처가 정상)."""
    return (len(q) / max(1, len(en_q))) / (len(amq.text(l, r)) / max(1, len(EN[r])))


def check(l, chunks):
    err, warn, T, Q = [], [], {}, {}
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    for c in chunks:
        S = SRCC[c]
        p = os.path.join(H, l, c + ".json")
        D = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
        if not D: err.append(f"{l}/{c}.json missing or empty")
        mp = os.path.join(H, l, f"quotes_{c}.json")
        M = json.load(open(mp, encoding="utf-8")) if os.path.exists(mp) else {}
        want = [k for k, v in S.items() if not isq(v)]
        miss = [k for k in want if k not in D]
        extra = [k for k in D if k not in want]
        if miss: err.append(f"{c}: missing {len(miss)} units, e.g. {miss[:6]}")
        if extra: err.append(f"{c}: extra keys {extra[:6]}")
        for k in want:
            if k not in D: continue
            e, z = S[k], D[k]
            if shape(z) != shape(e): err.append(f"{k}: structure differs from English"); continue
            es_, zs = list(strings(e)), list(strings(z))
            if any(a.strip() and not b.strip() for a, b in zip(es_, zs)): err.append(f"{k}: empty value")
            for a, b in zip(es_, zs):
                if HANGUL.search(b): err.append(f"{k}: Hangul")
                if a.strip() == b.strip() and (len(a.split()) >= 3 or ENGW.search(a)) and not k.startswith("ui:"):
                    err.append(f"{k}: identical to English: {a[:50]!r}")
                n_en = len(ENGW.findall(b))
                if n_en >= 3: err.append(f"{k}: looks English ({n_en} English function words): {b[:60]!r}")
            if sorted(REF.findall(" ".join(es_))) != sorted(REF.findall(" ".join(zs))):
                err.append(f"{k}: references changed {sorted(set(REF.findall(' '.join(es_))) ^ set(REF.findall(' '.join(zs))))}")
            if isinstance(e, str):
                r = len(z) / max(1, len(e))
                if len(e) > 80 and not 0.8 <= r <= 1.8: warn.append(f"{k}: length ratio {r:.2f}")
            T[k] = z
        for k, v in S.items():
            if not isq(v): continue
            r, t = v["cit"], v["q"]
            q = M.get(k, auto.get(k))
            if q is None: err.append(f"quote {k} [{r}]: not cut yet"); continue
            whole = re.sub(r"\W+", "", t).lower() == re.sub(r"\W+", "", EN[r]).lower()
            if whole:
                if re.sub(r"\s+", "", q) != re.sub(r"\s+", "", amq.text(l, r)): err.append(f"quote {k} [{r}]: whole verse expected")
            elif not amq.check(l, r, q):
                err.append(f"quote {k} [{r}]: NOT verbatim in {l}.json")
            if HANGUL.search(q): err.append(f"quote {k}: Hangul")
            if not whole and q.count("…") != t.count("…"):
                warn.append(f"quote {k}: {t.count('…')} omissions in English, {q.count('…')} in {l}")
            x = qratio(l, r, t, q)
            if not 0.8 <= x <= 1.25: warn.append(f"quote {k} [{r}]: length ratio {x:.2f} ({'cut by hand' if k in M else 'auto'})")
            Q[k] = q
        bad = [k for k in M if k not in S or not isq(S[k])]
        if bad: err.append(f"{l}/quotes_{c}.json: unknown keys {bad[:5]}")
    return T, Q, err, warn


# ── 영어 빌더 빌려 오기 ─────────────────────────────────
def load_builder(langs):
    src = open(FE_BUILDER, encoding="utf-8").read()
    src = src.split('for lang in ("ko", "en"):')[0]                  # 한국어·영어판을 다시 만들지 않는다
    src = src.replace('lang == "ko"', 'lang in ("ko", "es", "fr", "pt")')   # 부 번호 서식은 한국어판 갈래(대문자 없음)
    ns = {"__file__": FE_BUILDER, "__name__": "doctrine_en_builder"}
    exec(compile(src, FE_BUILDER, "exec"), ns)
    ns["CSS"] = ns["CSS"].replace("word-break:keep-all", "word-break:normal;hyphens:auto")
    return ns


def build(l, NS):
    T, Q, err, warn = check(l, CHUNKS)
    print(f"[{l}] units {len(T)}, quotations {len(Q)}, errors {len(err)}, warnings {len(warn)}")
    for x in err[:40]: print("   ·", x)
    if err: return False
    if l == "fr": T = {k: map_strings(v, fr_nb) for k, v in T.items()}
    U = UI[l]

    def chapters(_lang):
        out = []
        for n in range(34):
            d = X.load(n); k = f"ch{n:02d}"; C = []
            for i, b in enumerate(d["C"]):
                u = f"{k}:{i}"
                if b[0] in ("h", "p"): C.append([b[0], T[u]])
                elif b[0] == "q": C.append(["q", Q[u], b[2]])
                elif b[0] == "tt": C.append(["tt", T[u]["cap"], T[u]["rows"]])
                elif b[0] == "box": C.append(["box", T[u]["title"], T[u]["items"]])
                else: C.append(b)                                   # audio
            pn = d["part"][0]
            out.append(dict(n=n, label=T[k + ":label"], title=T[k + ":title"], sub=T[k + ":sub"] if (k + ":sub") in SRC else "",
                            part=(pn, T[f"part:{pn}"] if pn else ""), C=C))
        return out

    out = os.path.join(H, "work", f"out_{l}")             # 먼저 여기 만들고 검사가 통과하면 site 로 복사
    if os.path.isdir(out): shutil.rmtree(out)
    NS["L"][l] = dict(lang=l, out=out, title=U["title"], sub=U["sub"], by=U["by"], eb=U["eb"], contents=U["contents"],
                      prev=U["prev"], next=U["next"], audio_h=U["audio_h"], audio_series=U["audio_series"], audio_dir=AUDIO_DIR,
                      titles={a: T[f"audio:{a}"] for a in X.AUDIO_TITLE}, all_audio=U["all_audio"], all_audio_note=U["all_audio_note"],
                      cite=lambda r: amq.link(l, r), part=U["part"], font=FONT, sans=SANS, fonts="family=Source+Serif+4:wght@400;700")
    NS["chapters"] = chapters
    NS["build"](l)

    # ── 쪽 검사 (영어 쪽과 짜임 비교) ─────────────────────
    pages = {os.path.basename(f): open(f, encoding="utf-8").read() for f in glob.glob(os.path.join(out, "*.html"))}
    en_pages = sorted(os.path.basename(f) for f in glob.glob(os.path.join(EN_DIR, "*.html")))
    perr = []
    if sorted(pages) != en_pages: perr.append(f"page list differs from English: {sorted(set(pages) ^ set(en_pages))}")
    tags = ("<h2>", "<h2 ", "<p>", "<p ", "<blockquote>", "<table>", "<tr>", "<td>", "<th>", 'class="box"', 'class="listen"',
            'class="part"', '<a href="ch', '<a href="preface', '<a href="afterword', 'class="sub"')
    for fn, t in pages.items():
        e = open(os.path.join(EN_DIR, fn), encoding="utf-8").read()
        for tag in tags:
            if e.count(tag) != t.count(tag): perr.append(f"{fn}: count of {tag} {t.count(tag)} vs English {e.count(tag)}")
        if HANGUL.search(t): perr.append(f"{fn}: Hangul {''.join(HANGUL.findall(t)[:10])}")
        if "/en/" in t or "/textapp/" in t: perr.append(f"{fn}: /en/ or /textapp/ link")
        if f'<html lang="{l}">' not in t or "/home-button.js" not in t: perr.append(f"{fn}: lang / home button")
        for h in re.findall(r'href="([^"]+)"', t):
            if not (h == "./" or re.fullmatch(r"(ch\d\d|preface|afterword)\.html", h) or h.startswith(f"/{l}/book/#")
                    or h.startswith("https://fonts.") or re.fullmatch(re.escape(AUDIO_DIR) + r"\d\d/", h)):
                perr.append(f"{fn}: unexpected link {h}")
    nq = sum(t.count("<blockquote>") for t in pages.values())
    nt = sum(t.count("<table>") for t in pages.values())
    nh = sum(t.count("<h2>") for t in pages.values())
    print(f"     pages {len(pages)}, section headings {nh}, quotations {nq}, tables {nt}")
    for x in perr[:40]: print("   ·", x)
    if perr:
        print("     PAGE CHECK FAILED — site not written (preview in", out + ")")
        return False
    dst = os.path.join(SITE, l, "doctrine")
    os.makedirs(dst, exist_ok=True)
    for fn, t in pages.items():
        open(os.path.join(dst, fn), "w", encoding="utf-8").write(t)
    print(f"     → {dst} ({len(pages)} pages)")
    return True


def main():
    args = [a for a in sys.argv[1:] if a in UI]
    langs = args or ["es", "fr", "pt"]
    if "--chunk" in sys.argv:
        c = sys.argv[sys.argv.index("--chunk") + 1]
        rep = int(sys.argv[sys.argv.index("--report") + 1]) if "--report" in sys.argv else 40
        for l in langs:
            T, Q, err, warn = check(l, [c])
            print(f"[{l} {c}] units {len(T)}, quotations {len(Q)}, errors {len(err)}, warnings {len(warn)}")
            for x in err[:rep]: print("   ERR ", x)
            for x in warn[:rep]: print("   warn", x)
        return
    if "--audit" in sys.argv:
        for l in langs:
            auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
            rows = sorted((qratio(l, SRC[k]["cit"], SRC[k]["q"], q), k) for k, q in auto.items())
            out = [f"{x:.2f} {k}" for x, k in rows if not 0.8 <= x <= 1.25]
            print(f"[{l}] auto {len(auto)}, outside 0.80–1.25: {len(out)}")
            for s in out: print("   ", s)
        return
    NS = load_builder(langs)
    ok = all([build(l, NS) for l in langs])
    if not ok: raise SystemExit("CHECKS FAILED")
    print("ALL CHECKS PASSED")


if __name__ == "__main__":
    main()
