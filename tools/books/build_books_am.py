# -*- coding: utf-8 -*-
# 「예수의 삶과 가르침」·「예수의 열두 사도」 스페인어·프랑스어·포르투갈어판 → site/<l>/jesus-book/, site/<l>/apostles-book/
#   틀: 극동판 site/en/<book>/index.html (고치지 않음; 화면 글자만 바꿔 씀). 그림: site/books-img/<book>/ (세 언어 공용, 한 번 복사)
#   원고: src/<book>/skeleton.json + src/<book>/cNN.json (영어 단위)
#        + <l>/<book>/cNN.json (번역: 인용 dict 를 뺀 모든 단위, 같은 키)
#        + 인용: auto_<l>.json (자동, 키 "<book>:<key>") 또는 <l>/<book>/quotes_cNN.json (손으로 자른 것, 이쪽이 우선)
#   검사: 키 누락·남는 키·자리표시·*기울임*·한글·영어 잔재·⟦Q⟧ 표지·인용(tools/data/<l>.json 원문 그대로, 절 순서대로)
#   python build_books_am.py es [fr pt] [--book jesus|apostles]   검사 + 통과 시 빌드
#   python build_books_am.py es --book jesus --chunk c03         그 묶음만 검사 (쓰지 않음)
#   python build_books_am.py es --draft                          빠진 단위는 영어로 채워 _draft_<l>/<book>/ 에 미리보기
import hashlib, html, json, os, re, shutil, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
sys.path.insert(0, os.path.join(H, ".."))
import pt_old_spelling  # noqa: E402

FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
FEEN = os.path.join(FE, "site", "en")
args = sys.argv[1:]
DRAFT = "--draft" in args
CHUNK = args[args.index("--chunk") + 1] if "--chunk" in args else None
BOOKSEL = [args[args.index("--book") + 1]] if "--book" in args else ["jesus", "apostles"]
OUTROOT = args[args.index("--out") + 1] if "--out" in args else None   # test builds: write <dir>/<l>/<book>/ instead of site/
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]
if CHUNK and "--book" not in args: raise SystemExit("--chunk needs --book jesus|apostles (chunk numbers are per book)")
for b in BOOKSEL:
    if b not in ("jesus", "apostles"): raise SystemExit(f"unknown book {b!r} (jesus | apostles)")
esc = lambda s: html.escape(s, quote=True)

HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their|would|had|said)\b")
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧")
nows = lambda s: re.sub(r"\s+", "", s)
strip_marks = lambda s: re.sub(r"⟦/?Q[^⟧]*⟧", "", s)
QCH = "“”\"'‘’«» \u00a0"
WRAP = {"es": ("«", "»"), "fr": ("«\u00a0", "\u00a0»"), "pt": ("“", "”")}
PAPERW = {  # src lines ("Paper 122, sections 0–6") written per language
    "es": [("Papers", "Documentos"), ("Paper", "Documento"), ("sections", "secciones"), ("section", "sección")],
    "fr": [("Papers", "Fascicules"), ("Paper", "Fascicule"), ("sections", "sections"), ("section", "section")],
    "pt": [("Papers", "Documentos"), ("Paper", "Documento"), ("sections", "seções"), ("section", "seção")],
}


def fr_nb(s):
    s = re.sub(r" ([;:!?»])", "\u00a0\\1", s)
    return s.replace("« ", "«\u00a0")


def src_line(l, s):
    for a, b in PAPERW[l]: s = re.sub(r"\b%s\b" % a, b, s)
    return s


# ---------------------------------------------------------------- load + check
class Book:
    def __init__(self, book, l):
        self.book, self.l = book, l
        sd = os.path.join(H, "src", book)
        self.SK = json.load(open(os.path.join(sd, "skeleton.json"), encoding="utf-8"))
        self.folder = self.SK["folder"]
        self.EN, self.CH = {}, {}
        for c in self.SK["chunks"]:
            d = json.load(open(os.path.join(sd, c + ".json"), encoding="utf-8"))
            self.EN.update(d); self.CH.update({k: c for k in d})
        self.BOOK = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
        auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
        self.T, self.missing_files, self.hand_src, self.wrong = {}, [], {}, []
        for c in self.SK["chunks"]:
            if CHUNK and c != CHUNK: continue
            p = os.path.join(H, l, book, c + ".json")
            if os.path.exists(p):
                try: d = json.load(open(p, encoding="utf-8"))
                except json.JSONDecodeError as e: raise SystemExit(f"{l}/{book}/{c}.json is not valid JSON: {e}")
                for k in d:
                    if k in self.EN and self.CH[k] != c: self.wrong.append(f"{k} is in {l}/{book}/{c}.json but belongs to {self.CH[k]}")
                self.T.update(d)
            else: self.missing_files.append(f"{l}/{book}/{c}.json")
            hand = {}
            p = os.path.join(H, l, book, f"quotes_{c}.json")
            if os.path.exists(p): hand = json.load(open(p, encoding="utf-8"))
            for k in hand: self.hand_src[k] = f"{l}/{book}/quotes_{c}.json"
            for k, v in self.EN.items():
                if self.CH[k] != c or not isinstance(v, dict): continue
                q = hand.get(k, auto.get(f"{book}:{k}"))
                if q is not None: self.T[k] = {"q": q}
            for k in hand:
                if k not in self.EN or not isinstance(self.EN[k], dict): self.T["(quotes) " + k] = hand[k]

    def quote_ok(self, text, cits):
        if not isinstance(text, str): return False, "not a string"
        if any(c not in self.BOOK for c in cits): return False, "citation not in book"
        hay = nows("".join(self.BOOK[c] for c in cits)); pos = 0
        for piece in re.split(r"…|\.\.\.", text):
            piece = nows(piece).strip(QCH)
            if not piece: continue
            k = hay.find(piece, pos)
            if k < 0:
                return False, ("out of verse order: " if hay.find(piece) >= 0 else "not verbatim: ") + piece[:60]
            pos = k + len(piece)
        return True, ""

    def check(self):
        l, EN, T, SK = self.l, self.EN, self.T, self.SK
        errs, warns, badq, nq, miss_u, miss_q = [], [], [], 0, [], []
        errs += [f"wrong chunk: {x}" for x in self.wrong]
        for f in self.missing_files:
            if not DRAFT: errs.append(f"file not found: {f}")
        for k, ev in EN.items():
            if CHUNK and self.CH[k] != CHUNK: continue
            if k not in T:
                (miss_q if isinstance(ev, dict) else miss_u).append(k); continue
            tv = T[k]
            if isinstance(ev, dict):
                nq += 1
                ok, why = self.quote_ok(tv["q"], SK["quotes"][k]["cits"])
                if not ok: badq.append(f"{k} [{','.join(SK['quotes'][k]['cits'])}] {why}"
                                       + (f" (from {self.hand_src[k]})" if k in self.hand_src else " (automatic)"))
                continue
            if not isinstance(tv, str): errs.append(f"not a string: {k}"); continue
            if HANGUL.search(tv): errs.append(f"hangul: {k}")
            if [m.group(1) for m in MARK.finditer(ev)] != [m.group(1) for m in MARK.finditer(tv)]:
                errs.append(f"⟦Q⟧ quotation markers lost, added or changed: {k}")
            if tv.count("⟦") != tv.count("⟧") or len(MARK.findall(tv)) * 2 != tv.count("⟦"):
                errs.append(f"broken ⟦Q⟧ marker: {k}")
            for m in MARK.finditer(tv):
                nq += 1
                ok, why = self.quote_ok(m.group(2), m.group(1).split(","))
                if not ok: badq.append(f"{k} inline [{m.group(1)}] {why}")
            ph = set(re.findall(r"\{\w+\}", ev))
            if ph != set(re.findall(r"\{\w+\}", tv)): errs.append(f"placeholders {sorted(ph)} changed: {k}")
            if strip_marks(ev).count("*") != strip_marks(tv).count("*"): errs.append(f"*italic* markers changed: {k}")
            if not tv.strip() and ev.strip(): errs.append(f"empty: {k}")
            plain = re.sub(r"“[^”]*”|\"[^\"]*\"|«[^»]*»|⟦Q[^⟧]*⟧.*?⟦/Q⟧|\([^)]*\)", "", tv)
            hits = ENGW.findall(plain)
            if ev.strip() and nows(tv) == nows(ev) and len(ev.split()) > 3: warns.append(f"untranslated? {k}")
            elif len(hits) >= 2: warns.append(f"English words {hits[:4]}: {k}")
            if l == "pt" and pt_old_spelling.fix(tv) != tv:
                warns.append(f"post-2009 spelling (run python ..\\pt_old_spelling.py on the file): {k}")
            if l == "fr" and re.search(r"[“”]", strip_marks(MARK.sub("", tv))) and "«" not in tv:
                warns.append(f"English quotation marks “ ” (use « »): {k}")
        for k in T:
            if k.startswith("(quotes) "): errs.append(f"quotes file has a key that is not a quotation unit: {k[9:]}")
            elif k not in EN: errs.append(f"extra key (not in the English source): {k}")
        if miss_u and not DRAFT:
            errs.append(f"missing {len(miss_u)} prose units: {', '.join(miss_u[:20])}{' …' if len(miss_u) > 20 else ''}"
                        + ("" if CHUNK else f" (chunks: {', '.join(sorted({self.CH[k] for k in miss_u}))})"))
        if miss_q:
            msg = (f"missing {len(miss_q)} quotations (hand-cut them: work/{self.book}/todo_{l}_<chunk>.json → "
                   f"{l}/{self.book}/quotes_<chunk>.json): " + ", ".join(f"{k} [{self.CH[k]}]" for k in miss_q[:8]))
            (warns if DRAFT else errs).append(msg)
        scope = f" chunk {CHUNK}" if CHUNK else ""
        sel = [k for k in EN if not CHUNK or self.CH[k] == CHUNK]
        print(f"[{l} {self.book}{scope}] translated: {sum(1 for k in sel if k in T and not isinstance(EN[k], dict))}/"
              f"{sum(1 for k in sel if not isinstance(EN[k], dict))} · quotations checked: {nq} · bad: {len(badq)} · "
              f"errors {len(errs)} · warnings {len(warns)}")
        for e in errs[:40]: print("  ERR", e)
        if len(errs) > 40: print(f"  … {len(errs) - 40} more errors")
        for b in badq[:40]: print("  BADQ", b)
        if len(badq) > 40: print(f"  … {len(badq) - 40} more bad quotations")
        for w in warns[:30]: print("  WARN", w)
        if len(warns) > 30: print(f"  … {len(warns) - 30} more warnings")
        return bool(errs or badq)

    # ------------------------------------------------------------ build
    def V(self, k):
        """display text of a unit (markers removed; quotation units wrapped in the language's quotation marks)."""
        l, ev = self.l, self.EN[k]
        if isinstance(ev, dict):
            q = self.T[k]["q"] if k in self.T else None
            if q is None: return ev["en"] + ev.get("tail", "")          # draft: English
            q = q.strip(QCH)
            if ev.get("wrap"): q = WRAP[l][0] + q + WRAP[l][1]
            return q + ev.get("tail", "")
        v = self.T.get(k, ev) if DRAFT else self.T[k]
        if l == "fr" and k in self.T:
            parts = re.split(r"(⟦Q [^⟧]+⟧.*?⟦/Q⟧)", v)
            v = "".join(p if p.startswith("⟦Q ") else fr_nb(p) for p in parts)
        return strip_marks(v)

    def build(self):
        l, SK, V = self.l, self.SK, self.V
        site = OUTROOT or os.path.join(ROOT, "site")
        out = os.path.join(H, f"_draft_{l}", self.folder) if DRAFT else os.path.join(site, l, self.folder)
        if os.path.isdir(out):                       # OneDrive may lock folders: delete files, keep folders
            for dp, _, fs in os.walk(out):
                for f in fs: os.remove(os.path.join(dp, f))
        os.makedirs(os.path.join(out, "data"), exist_ok=True)
        img = f"/books-img/{self.folder}/"
        UI = lambda n: V("ui." + n)
        jsd = lambda o: json.dumps(o, ensure_ascii=False)
        w = lambda name, s: open(os.path.join(out, name), "w", encoding="utf-8", newline="\n").write(s)

        # images (shared by the three languages)
        if not DRAFT:
            src_img = os.path.join(FEEN, self.folder, "img") if os.path.isdir(os.path.join(FEEN, self.folder, "img")) else None
            dst = os.path.join(site, "books-img", self.folder); os.makedirs(dst, exist_ok=True)
            names = [ch["img"] for ch in SK["chapters"] if ch["img"]] + [SK["intro"]["img"][1]]
            for nm in names:
                cands = [os.path.join(FE, "site", self.folder, "img", nm)] + ([os.path.join(src_img, nm)] if src_img else [])
                s = next((p for p in cands if os.path.exists(p)), None)
                if not s: raise SystemExit(f"image not found: {nm}")
                d = os.path.join(dst, nm)
                if not os.path.exists(d) or os.path.getsize(d) != os.path.getsize(s): shutil.copy2(s, d)

        # chapters + toc
        label = lambda ch: UI(ch["kind"]).replace("{n}", str(ch["n"])) if ch["kind"] == "chapter" else UI(ch["kind"])
        part = lambda ch: V(f"part{ch['part']}") if ch["part"] else ""
        toc = []
        for ch in SK["chapters"]:
            p = f"ch{ch['n']:02d}"
            b = [[ty, V(k)] for ty, k in ch["blocks"]]
            src = src_line(l, ch["src"]) if ch["src"] else V(p + ".src")
            d = {"n": ch["n"], "label": label(ch), "title": V(p + ".title"), "part": part(ch), "src": src,
                 "img": img + ch["img"] if ch["img"] else "", "b": b}
            w(os.path.join("data", ch["file"]), "CH(" + jsd(d) + ");\n")
            toc.append([ch["n"], d["label"], d["title"], d["part"], [t for ty, t in b if ty == "h"]])
        w(os.path.join("data", "toc.js"), "TOC(" + jsd(toc) + ");\n")

        # intro
        I, ik = {}, SK["intro"]
        for f in ik["keys"]:
            if f in ("title", "sub", "kick", "one"): I[f] = V("intro." + f)
            elif f == ik.get("alt"): I[f] = V("intro.alt")
            elif f in ("cover", "hero"): I[f] = img + ik["img"][1]
            elif f == "meta": I[f] = [V(f"intro.meta{i + 1}") for i in range(ik["meta"])]
            elif f == "about": I[f] = [V(f"intro.about{i + 1}") for i in range(ik["about"])]
            elif f == "lists": I[f] = [[V(f"intro.list{i + 1}.title"), [V(f"intro.list{i + 1}.{j + 1}") for j in range(n)]]
                                       for i, n in enumerate(ik["lists"])]
            elif f == "preface": I[f] = [[ty, V(k) if k else lit] for ty, k, lit in ik["preface"]]
            else: raise SystemExit(f"intro field not handled: {f}")
        w(os.path.join("data", "intro.js"), "INTRO(" + jsd(I) + ");\n")

        # index.html
        s = open(os.path.join(FEEN, self.folder, "index.html"), encoding="utf-8").read()
        en_title = re.search(r"<title>(.*?)</title>", s).group(1)
        L10N = {k: UI(k) for k in ("toc_about", "toc_about_long", "about_book", "and_preface", "preface", "illustration", "ub")}
        pairs = [
            ('<html lang="en">', f'<html lang="{l}">'),
            (f"<title>{en_title}</title>", f"<title>{esc(UI('title'))}</title>"),
            (re.search(r'<meta name="description" content=".*?">', s).group(0), f'<meta name="description" content="{esc(UI("desc"))}">'),
            (re.search(r'<meta property="og:title" content=".*?">', s).group(0), f'<meta property="og:title" content="{esc(UI("og_title"))}">'),
            (re.search(r'<meta property="og:image" content=".*?">', s).group(0), f'<meta property="og:image" content="{img}{ik["img"][1]}">'),
            ('<link rel="icon" href="/favicon.ico" sizes="any">',
             '<link rel="icon" href="/favicon.ico" sizes="any">\n<script src="/home-button.js" data-into=".top" defer></script>'),
            (".ur-home-btn{display:inline-flex;", ".bk-home{display:inline-flex;"),
            ("background:#ff5a1f;color:#fff!important;border:2px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,.25);font:700 13.5px/1.1 \"Malgun Gothic\",\"Apple SD Gothic Neo\",system-ui,sans-serif;text-decoration:none!important;white-space:nowrap}.ur-home-btn:hover{background:#e64a10}.ur-home-btn:focus-visible{outline:3px solid #ffd23f;outline-offset:2px}@media print{.ur-home-btn{display:none}}",
             "background:rgba(255,255,255,.14);color:#fff!important;border:1px solid rgba(255,255,255,.55);font:700 13.5px/1.1 system-ui,\"Segoe UI\",Arial,sans-serif;text-decoration:none!important;white-space:nowrap}.bk-home:hover{background:rgba(255,255,255,.26)}.bk-home:focus-visible{outline:3px solid #ffd23f;outline-offset:2px}@media print{.bk-home{display:none}}"),
            (re.search(r'<a class="ur-home-btn" href="/en/jesus/" target="_top" title="[^"]*">[^<]*</a>', s).group(0),
             f'<a class="bk-home" href="/{l}/jesus/" target="_top" title="{esc(UI("hub"))}">← {esc(UI("hub"))}</a>'),
            (f"<b>{en_title}</b>", f"<b>{esc(UI('title'))}</b>"),
            ('<button id="tg">☰ Contents</button>', f'<button id="tg">{esc(UI("contents"))}</button>'),
            ('title="Smaller text" aria-label="Smaller text"', f'title="{esc(UI("smaller"))}" aria-label="{esc(UI("smaller"))}"'),
            ('title="Larger text" aria-label="Larger text"', f'title="{esc(UI("larger"))}" aria-label="{esc(UI("larger"))}"'),
            ('title="Night mode" aria-label="Night mode"', f'title="{esc(UI("night"))}" aria-label="{esc(UI("night"))}"'),
            ('<div class="empty">Loading…</div>', f'<div class="empty">{esc(UI("loading"))}</div>'),
            (re.search(r'var BOOK=\{"title": "[^"]*", "key": "(\w+)"\};', s).group(0),
             "var BOOK=" + jsd({"title": UI("title"), "key": re.search(r'"key": "(\w+)"', s).group(1) + l}) + ";\nvar L10N=" + jsd(L10N) + ";"),
            ("<i>About</i><span>About the Book &amp; Preface</span>", "<i>'+esc(L10N.toc_about)+'</i><span>'+esc(L10N.toc_about_long)+'</span>"),
            ("['intro','About the Book','& Preface']", "['intro',L10N.about_book,L10N.and_preface]"),
            ("s+='<h3>About the Book</h3>'", "s+='<h3>'+esc(L10N.about_book)+'</h3>'"),
            ("s+='<h3 id=\"pre\">Preface</h3>'", "s+='<h3 id=\"pre\">'+esc(L10N.preface)+'</h3>'"),
            ("else if(/^[“\"]/.test(t))", "else if(/^[“\"«]/.test(t))"),
            ("'<div class=\"src\"><em>The Urantia Book</em>, '", "'<div class=\"src\"><em>'+esc(L10N.ub)+'</em>, '"),
            ("alt=\"Illustration: '+esc(c.title)+'\"", "alt=\"'+esc(L10N.illustration.replace('{title}',c.title))+'\""),
        ]
        for a, b in pairs:
            if a not in s: raise SystemExit(f"template changed ({self.folder}/index.html): {a[:80]!r}")
            s = s.replace(a, b)
        for left in ("/en/", "fareast"):
            if left in s and not DRAFT: raise SystemExit(f"English left in index.html: {left!r}")
        ver = hashlib.md5(json.dumps([toc, I], ensure_ascii=False).encode("utf-8")).hexdigest()[:8]
        s = s.replace("V=Math.floor(Date.now()/36e5)", f"V='{ver}'+Math.floor(Date.now()/36e5)")
        if DRAFT:
            s = re.sub(r"(<body[^>]*>)", r'\1\n<div style="background:#c00;color:#fff;text-align:center;padding:4px;font:13px sans-serif">DRAFT — not for publication</div>', s, count=1)
        w("index.html", s)

        bad = [f for dp, _, fs in os.walk(out) for f in fs
               if f.endswith((".html", ".js")) and HANGUL.search(open(os.path.join(dp, f), encoding="utf-8").read())]
        if bad: raise SystemExit(f"CHECK FAILED: hangul in output {bad}")
        n = sum(len(fs) for _, _, fs in os.walk(out))
        print(f"[{l} {self.book}{' DRAFT' if DRAFT else ''}] {n} files → {out}")


fail_any, built = False, []
for l in LANGS:
    for book in BOOKSEL:
        B = Book(book, l)
        failed = B.check()
        fail_any |= failed
        if CHUNK: continue
        if failed and not DRAFT:
            print(f"CHECK FAILED [{l} {book}] — site/{l}/{B.folder}/ not written (use --draft for a preview)"); continue
        B.build(); built.append((l, book))
if built and not DRAFT and not OUTROOT:
    print("now rebuild the Jesus Study hub so it links to the local books:  python ..\\jesus\\build_jesus_am.py "
          + " ".join(sorted({l for l, _ in built})))
if fail_any and not DRAFT: print("errors 1"); sys.exit(1)
if fail_any: print("draft written, but the final build would fail: errors 1 (see above)"); sys.exit(1)
print("errors 0")
