# -*- coding: utf-8 -*-
# 예수 연구(Jesus Study) 스페인어·프랑스어·포르투갈어판 → site/<l>/jesus/
#   첫 화면(왼쪽 메뉴 + iframe) · discourses(담화) · chronology(연대별) · ages(나이별) · acts(행적 대조표) · teachings(새들러 워크북)
#   틀은 극동판 tools/jesus/build_hub.py, web_en/*.html·common.*, build_acts_web.py(CSS·JS·쪽 틀), site/en/jesus/teachings/index.html
#   에서 빌려 쓴다(고치지 않음).
#   원고: src/skeleton.json + src/teachings_body.html + src/cNN.json (영어 단위)
#        + <l>/cNN.json (번역: 인용 dict 를 뺀 모든 단위, 같은 키)
#        + 인용: auto_<l>.json (자동) 또는 <l>/quotes_cNN.json (손으로 자른 것, 이쪽이 우선)
#   검사: 키 누락·구조·자리표시·한글·영어 잔재·인용(tools/data/<l>.json 원문 그대로) — 하나라도 어긋나면 쪽을 만들지 않는다.
#   python build_jesus_am.py es [fr pt]           검사 + 통과 시 빌드
#   python build_jesus_am.py es --chunk c03       그 묶음만 검사 (쓰지 않음)
#   python build_jesus_am.py es --draft           빠진 단위는 영어로 채워 _draft_<l>/ 에 미리보기
import hashlib, html, json, os, re, shutil, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
FEJ = os.path.join(FE, "tools", "jesus")
ENJ = os.path.join(FE, "site", "en", "jesus")
args = sys.argv[1:]
DRAFT = "--draft" in args
CHUNK = args[args.index("--chunk") + 1] if "--chunk" in args else None
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]
esc = html.escape

SK = json.load(open(os.path.join(H, "src", "skeleton.json"), encoding="utf-8"))
EN, CH = {}, {}
for c in SK["chunks"]:
    d = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
    EN.update(d); CH.update({k: c for k in d})
HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their)\b")
MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧")
nows = lambda s: re.sub(r"\s+", "", s)
strip_marks = lambda s: re.sub(r"⟦/?Q[^⟧]*⟧", "", s)
CIRC = "①②③④⑤⑥⑦⑧⑨⑩⑪⑫⑬⑭⑮⑯⑰⑱⑲⑳"
LOCALE = {"es": "es-ES", "fr": "fr-FR", "pt": "pt-BR"}
FAREAST_EN = "https://fareast.urantiareaders.com/en/"

# ---------------------------------------------------------------- Bible book abbreviations (RVR 1909 · Louis Segond · Almeida)
BOOKS = {  # English regex → (es, fr, pt)
    r"Matt(?:hew)?\.?": ("Mt", "Mt", "Mt"), r"Mark": ("Mr", "Mc", "Mc"), r"Luke": ("Lc", "Lc", "Lc"),
    r"I\s*John|1\s*John": ("1 Jn", "1 Jn", "1 Jo"), r"John": ("Jn", "Jn", "Jo"), r"Acts": ("Hch", "Ac", "At"),
    r"Rom\.?": ("Ro", "Rm", "Rm"), r"I\s*Cor\.?|1\s*Cor\.?": ("1 Co", "1 Co", "1 Co"), r"II\s*Cor\.?|2\s*Cor\.?": ("2 Co", "2 Co", "2 Co"),
    r"Gal\.?": ("Gá", "Ga", "Gl"), r"Eph\.?": ("Ef", "Ep", "Ef"), r"Phil\.?": ("Fil", "Ph", "Fp"), r"Col\.?": ("Col", "Col", "Cl"),
    r"Heb\.?": ("He", "Hé", "Hb"), r"Rev\.?": ("Ap", "Ap", "Ap"), r"Isa\.?|Isa,": ("Is", "Es", "Is"), r"Jer\.?": ("Jer", "Jé", "Jr"),
    r"Ezek\.?": ("Ez", "Ez", "Ez"), r"Dan\.?": ("Dn", "Dn", "Dn"), r"Hos\.?": ("Os", "Os", "Os"), r"Mic\.?": ("Mi", "Mi", "Mq"),
    r"Mal\.?": ("Mal", "Ml", "Ml"), r"Zech\.?": ("Zac", "Za", "Zc"), r"Joel": ("Jl", "Jl", "Jl"), r"Amos": ("Am", "Am", "Am"),
    r"Jonah": ("Jon", "Jon", "Jn"), r"Ps\.?|Psa\.?|Psalms?": ("Sal", "Ps", "Sl"), r"Prov\.?": ("Pr", "Pr", "Pv"),
    r"Eccl\.?": ("Ec", "Ec", "Ec"), r"Job": ("Job", "Jb", "Jó"), r"Gen\.?": ("Gn", "Gn", "Gn"), r"Ex\.?|Exod\.?": ("Éx", "Ex", "Êx"),
    r"Lev\.?": ("Lv", "Lv", "Lv"), r"Num\.?": ("Nm", "Nb", "Nm"), r"Deut\.?": ("Dt", "Dt", "Dt"), r"Josh\.?": ("Jos", "Jos", "Js"),
    r"Judg\.?": ("Jue", "Jg", "Jz"), r"I\s*Sam\.?|1\s*Sam\.?": ("1 S", "1 S", "1 Sm"), r"II\s*Sam\.?|2\s*Sam\.?": ("2 S", "2 S", "2 Sm"),
    r"I\s*Kings|1\s*Kings": ("1 R", "1 R", "1 Rs"), r"II\s*Kings|2\s*Kings": ("2 R", "2 R", "2 Rs"), r"Jas\.?|James": ("Stg", "Jc", "Tg"),
    r"I\s*Pet\.?|1\s*Pet\.?": ("1 P", "1 P", "1 Pe"), r"II\s*Pet\.?|2\s*Pet\.?": ("2 P", "2 P", "2 Pe"),
    r"I\s*Tim\.?|1\s*Tim\.?": ("1 Ti", "1 Tm", "1 Tm"), r"II\s*Tim\.?|2\s*Tim\.?": ("2 Ti", "2 Tm", "2 Tm"),
    r"I\s*Thess\.?|1\s*Thess\.?": ("1 Ts", "1 Th", "1 Ts"),
}
LI = {"es": 0, "fr": 1, "pt": 2}
ACTSBK = {"Matt": r"Matt(?:hew)?\.?", "Mark": r"Mark", "Luke": r"Luke", "John": r"John", "Acts": r"Acts"}


def bible(l, s):
    """'(Matt. 12:9-14. Mark 3:1-6.)' → '(Mt 12:9-14. Mr 3:1-6.)' (성경 장절만 있는 꼬리말)."""
    out = s
    for pat in sorted(BOOKS, key=lambda x: -len(x)):
        out = re.sub(r"(?<![A-Za-zÀ-ÿ])(?:" + pat + r")\s*(?=\d)", BOOKS[pat][LI[l]] + "\u00a0", out)
    return out


def kb(l, refs, none):
    if not refs: return none
    s, pb, pc = "", None, None
    for b, c, a, z in refs:
        v = f"{a}" if a == z else f"{a}-{z}"
        if b == pb and c == pc: s += f", {v}"
        elif b == pb: s += f"; {c}:{v}"
        else: s += ("; " if s else "") + f"{BOOKS[ACTSBK[b]][LI[l]]}\u00a0{c}:{v}"
        pb, pc = b, c
    return s


def fr_nb(s):
    s = re.sub(r" ([;:!?»])", "\u00a0\\1", s)
    return s.replace("« ", "«\u00a0")


# ---------------------------------------------------------------- load + check
def load(l):
    BOOK = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
    TIT = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}_titles.json"), encoding="utf-8"))
    T = {}
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    for c in SK["chunks"]:
        p = os.path.join(H, l, c + ".json")
        if os.path.exists(p): T.update(json.load(open(p, encoding="utf-8")))
        elif not CHUNK and not DRAFT: print(f"  [missing file] {l}/{c}.json")
        hand = {}
        p = os.path.join(H, l, f"quotes_{c}.json")
        if os.path.exists(p): hand = json.load(open(p, encoding="utf-8"))
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        for k, v in S.items():
            if isinstance(v, dict):
                q = hand.get(k, auto.get(k))
                if q is not None: T[k] = {"q": q, "cit": v["cit"], "kind": v["kind"]}
    return BOOK, TIT, T


def check(l, BOOK, T):
    def quote_ok(text, cit):
        if cit not in BOOK: return False, "citation not in book"
        hay = nows(BOOK[cit]); pos = 0
        parts = text if isinstance(text, list) else re.split(r"…|\.\.\.", text)
        for piece in parts:
            piece = nows(piece).strip("“”\"'‘’«»")
            if not piece: continue
            k = hay.find(piece, pos)
            if k < 0: return False, piece[:50]
            pos = k + len(piece)
        return True, ""
    errs, warns, badq, nq = [], [], [], 0
    for k, ev in EN.items():
        if CHUNK and CH[k] != CHUNK: continue
        if k not in T:
            if not DRAFT: errs.append(f"missing: {k}")
            elif isinstance(ev, dict): warns.append(f"quotation not cut yet (English shown in the draft): {k}")
            continue
        tv = T[k]
        if isinstance(ev, dict):
            nq += 1
            if not isinstance(tv, dict) or not isinstance(tv["q"], (str, list)): errs.append(f"bad quotation value: {k}"); continue
            ok, why = quote_ok(tv["q"], tv["cit"])
            if not ok: badq.append(f"{k} [{tv['cit']}] {why}")
            if HANGUL.search(json.dumps(tv["q"], ensure_ascii=False)): errs.append(f"hangul: {k}")
            continue
        if not isinstance(tv, str): errs.append(f"not a string: {k}"); continue
        if HANGUL.search(tv): errs.append(f"hangul: {k}")
        if [m.group(1) for m in MARK.finditer(ev)] != [m.group(1) for m in MARK.finditer(tv)]:
            errs.append(f"inline quotation markers changed: {k}")
        if tv.count("⟦") != tv.count("⟧") or len(MARK.findall(tv)) * 2 != tv.count("⟦"):
            errs.append(f"broken marker: {k}")
        for m in MARK.finditer(tv):
            nq += 1
            ok, why = quote_ok(m.group(2), m.group(1))
            if not ok: badq.append(f"{k} inline [{m.group(1)}] {why}")
        ph = set(re.findall(r"\{\w+\}", ev))
        if ph != set(re.findall(r"\{\w+\}", tv)): errs.append(f"placeholders {sorted(ph)} changed: {k}")
        if ev.count("**") != tv.count("**"): errs.append(f"** bold markers changed: {k}")
        if "  ·  " in ev and "  ·  " not in tv: errs.append(f"separator '  ·  ' lost: {k}")
        plain = re.sub(r"“[^”]*”|\"[^\"]*\"|«[^»]*»|⟦Q[^⟧]*⟧.*?⟦/Q⟧|\([^)]*\)", "", tv)
        hits = ENGW.findall(plain)
        if ev.strip() and nows(tv) == nows(ev) and len(ev.split()) > 3: warns.append(f"untranslated? {k}")
        elif len(hits) >= 2: warns.append(f"English words {hits[:4]}: {k}")
    for k in T:
        if k not in EN: errs.append(f"extra key: {k}")
    scope = f" chunk {CHUNK}" if CHUNK else ""
    sel = [k for k in EN if not CHUNK or CH[k] == CHUNK]
    print(f"[{l}{scope}] translated: {sum(1 for k in sel if k in T and not isinstance(EN[k], dict))}/"
          f"{sum(1 for k in sel if not isinstance(EN[k], dict))} · quotations checked: {nq} · bad: {len(badq)} · "
          f"errors {len(errs)} · warnings {len(warns)}")
    for e in errs[:40]: print("  ERR", e)
    if len(errs) > 40: print(f"  … {len(errs) - 40} more errors")
    for b in badq[:40]: print("  BADQ", b)
    if len(badq) > 40: print(f"  … {len(badq) - 40} more bad quotations")
    for w in warns[:30]: print("  WARN", w)
    if len(warns) > 30: print(f"  … {len(warns) - 30} more warnings")
    return bool(errs or badq)


# ---------------------------------------------------------------- build
def w(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w", encoding="utf-8", newline="\n").write(text)


def jstr(s):  # JavaScript single-quoted string
    return "'" + s.replace("\\", "\\\\").replace("'", "\\'").replace("\n", " ") + "'"


def rep(s, pairs, where):
    for a, b in pairs:
        if a not in s: raise SystemExit(f"template changed ({where}): {a[:70]!r}")
        s = s.replace(a, b)
    return s


def build(l, BOOK, TIT, T):
    out = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "jesus")
    if os.path.isdir(out): shutil.rmtree(out)
    os.makedirs(out)

    def V(k):
        v = T.get(k, EN[k]) if DRAFT else T[k]
        if isinstance(v, dict) or isinstance(EN[k], dict):
            q = v["q"] if isinstance(v, dict) else v["q"]
            return " ".join(x.strip() for x in q) if isinstance(q, list) else q
        if l == "fr":   # no-break spaces only outside the quoted official text
            parts = re.split(r"(⟦Q [^⟧]+⟧.*?⟦/Q⟧)", v)
            v = "".join(p if p.startswith("⟦Q ") else fr_nb(p) for p in parts)
        return strip_marks(v)
    UI = lambda name: V("ui." + name)
    AU = lambda name: V("acts.ui." + name)
    bold = lambda s: re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", esc(s))
    ptitle = lambda p: TIT[str(p)]["title"]
    stitle = lambda p, s: TIT[str(p)]["sec"].get(str(s), "")
    reader = f"/{l}/book/#"

    # ---------- hub
    hub_src = open(os.path.join(FEJ, "build_hub.py"), encoding="utf-8").read()
    ns = {"__file__": os.path.join(FEJ, "build_hub.py")}; exec(hub_src.split("def build(lang):")[0], ns)
    items = [dict(id=i, name=UI("item_" + i), url=f"/{l}/jesus/{i}/") for i in ("discourses", "chronology", "ages", "acts", "teachings")]
    items += [dict(id="life", name=UI("item_life"), url=FAREAST_EN + "jesus-book/"),
              dict(id="apostles", name=UI("item_apostles"), url=FAREAST_EN + "apostles-book/")]
    links = "\n".join(f'    <a href="{x["url"]}" data-id="{x["id"]}"><span class="n">{n}</span><span>{esc(x["name"])}</span></a>'
                      for n, x in enumerate(items, 1))
    hub = ns["TPL"].format(lang=l, title=esc(UI("hub_title")), sub="Urantia America", home="", homeUrl=f"/{l}/",
                           menu=esc(UI("hub_menu")), open=esc(UI("hub_open")), font="Noto+Sans", fontname="Noto Sans",
                           links=links, items=json.dumps(items, ensure_ascii=False))
    hub = rep(hub, [(f'    <a class="home" href="/{l}/"></a>\n', ""),
                    ("| Urantia Far East</title>", "| Urantia America</title>"),
                    ('<link rel="icon" href="/favicon.ico" sizes="any">',
                     '<link rel="icon" href="/favicon.ico" sizes="any">\n<script src="/home-button.js" data-into=".top" defer></script>')], "hub")
    w(os.path.join(out, "index.html"), hub)

    # ---------- shared css / js (read aloud in the page language)
    shutil.copy(os.path.join(ENJ, "common.css"), os.path.join(out, "common.css"))
    cjs = open(os.path.join(ENJ, "common.js"), encoding="utf-8").read()
    cjs = rep(cjs, [("/* Jesus Study (English) shared script", f"/* Jesus Study ({l}) shared script"),
                    ("E = '.!?”\"';", "E = '.!?”\"»';"),
                    ("tl=en&", f"tl={l}&"),
                    ("return /^en/i.test(v.lang)", f"return /^{l}/i.test(v.lang)"),
                    ("o.textContent = 'Default voice'", "o.textContent = " + jstr(UI("voice_default"))),
                    ("'jz_voice_en'", f"'jz_voice_{l}'"),
                    ("u.lang = 'en-US'", f"u.lang = '{LOCALE[l]}'")], "common.js")
    w(os.path.join(out, "common.js"), cjs)

    common_head = [('<html lang="en">', f'<html lang="{l}">'),
                   ('href="/en/jesus/" target="_top" title="Jesus Study home">🏠 Home</a>',
                    f'href="/{l}/jesus/" target="_top" title="{esc(UI("home_title"))}">{esc(UI("home"))}</a>'),
                   ('<button class="btn" id="burger">☰ Contents</button>', f'<button class="btn" id="burger">{esc(UI("contents"))}</button>'),
                   ('<span class="by">The Urantia Book, Part IV · Papers 120–196</span>', f'<span class="by">{esc(UI("by"))}</span>'),
                   ('title="Text size"', f'title="{esc(UI("textsize"))}"'), ('title="Light / dark"', f'title="{esc(UI("dark"))}"'),
                   ('<p class="empty">Loading…</p>', f'<p class="empty">{esc(UI("loading"))}</p>')]

    # ---------- discourses
    ds = []
    for d in SK["discourses"]:
        sec = stitle(d["pno"], d["sec"]) if d["sec"] else UI("d_intro")
        ds.append(dict(id=d["id"], ref=d["ref"], paper=ptitle(d["pno"]), pno=d["pno"], sec=sec,
                       verses=[[EN[k]["cit"], V(k)] for k in d["verses"]], title=V(f"d.{d['id']}.title")))
    data = {"discourses/data.js": "window.DISCOURSES=%s;\n" % json.dumps(ds, ensure_ascii=False, separators=(",", ":"))}
    s = open(os.path.join(FEJ, "web_en", "discourses.html"), encoding="utf-8").read()
    s = rep(s, common_head + [
        ("<title>The Discourses of Jesus</title>", f"<title>{esc(UI('d_title'))}</title>"),
        ('content="Discourses of Jesus from Part IV of The Urantia Book, each at least three lines long, with titles and paragraph references."',
         f'content="{esc(UI("d_desc"))}"'),
        ("<h1>The Discourses of Jesus</h1>", f"<h1>{esc(UI('d_title'))}</h1>"),
        ('>■ Stop</button>', f'>{esc(UI("stop"))}</button>'), ('title="Voice"', f'title="{esc(UI("voice"))}"'),
        ('title="Reading speed"', f'title="{esc(UI("speed"))}"'),
        ('placeholder="Search titles and text (e.g. forgive, prayer)"', f'placeholder="{esc(UI("d_search"))}"'),
        ("function ptitle(p) { return p.title.replace(/^Paper\\s+\\d+\\s*[—–-]\\s*/, '') }", "function ptitle(p) { return p.title }"),
        ("var h = '<div class=\"lead\"><h2>The Discourses of Jesus</h2><p>From Part IV of The Urantia Book (Papers 120–196), <b>' + D.length + ' discourses</b> in which Jesus speaks at length (three lines or more) have been gathered and given titles. Click a title to open the passage; the number on the left is the paragraph reference (click it to open that paragraph in the full text).</p>'",
         "var h = '<div class=\"lead\"><h2>' + " + jstr(esc(UI("d_title"))) + " + '</h2><p>' + " + jstr(bold(UI("d_lead"))) + ".replace('{n}', D.length) + '</p>'"),
        ("<button id=\"openall\">Expand all</button><button id=\"closeall\">Collapse all</button>",
         f"<button id=\"openall\">{esc(UI('d_expand'))}</button><button id=\"closeall\">{esc(UI('d_collapse'))}</button>"),
        ("'\">Paper ' + p.no + ' · '", "'\">' + " + jstr(esc(UI("d_paper"))) + ".replace('{n}', p.no) + ' · '"),
        ("list.length + (list.length === 1 ? ' discourse' : ' discourses')",
         "(list.length === 1 ? " + jstr(esc(UI("d_one"))) + " : " + jstr(esc(UI("d_many"))) + ").replace('{n}', list.length)"),
        (">🔊 Listen<", f">{esc(UI('d_listen'))}<"), (">🔗 Copy link<", f">{esc(UI('d_copy'))}<"),
        ("href=\"/en/book/#' + v[0] + '\" target=\"_blank\" rel=\"noopener\" title=\"Open in the full text\"",
         f"href=\"{reader}' + v[0] + '\" target=\"_blank\" rel=\"noopener\" title=\"{esc(UI('d_open'))}\""),
        ("'<p class=\"empty\">No discourses found.</p>'", "'<p class=\"empty\">' + " + jstr(esc(UI("d_none"))) + " + '</p>'"),
        ("'<div class=\"foot\">Source: selected from an extract of the words of Jesus in Part IV of The Urantia Book, arranged by paragraph reference; only discourses of three lines or more are included. The extract was made from quotation marks and context, so it may include words of the people Jesus was speaking with, or leave out some of his sayings. Click a paragraph reference to read it in context.</div>'",
         "'<div class=\"foot\">' + " + jstr(esc(UI("d_foot"))) + " + '</div>'"),
        (">Nothing found.<", f">{esc(UI('d_nothing'))}<"),
        ("flash('Link copied')", "flash(" + jstr(UI("d_copied")) + ")"),
        ("prompt('Link', u) }); else prompt('Link', u);", "prompt(" + jstr(UI("d_link")) + ", u) }); else prompt(" + jstr(UI("d_link")) + ", u);"),
    ], "discourses.html")
    pages = {"discourses/index.html": s}

    # ---------- chronology / ages
    ctpl = open(os.path.join(FEJ, "web_en", "chronology.html"), encoding="utf-8").read()
    for kind, folder in (("y", "chronology"), ("a", "ages")):
        sk = SK["chrono_" + kind]
        eras = [V(f"c{kind}.era{j + 1}") for j in range(sk["eras"])]
        its = []
        for i, it in enumerate(sk["items"]):
            p = f"c{kind}.{i + 1:02d}"
            x = dict(era=eras[it["era"] - 1], title=V(p + ".title"), event=V(p + ".event"),
                     impact=V(p + ".impact") if p + ".impact" in EN else "")
            if kind == "y": x.update(ko=V(p + ".date"), en=V(p + ".day") if p + ".day" in EN else "")
            else: x.update(age=it["age"], year=V(p + ".year"))
            its.append(x)
        C = dict(kind="year" if kind == "y" else "age", title=V(f"c{kind}.title"), sub=V(f"c{kind}.sub").replace("{n}", str(len(its))),
                 eras=eras, items=its, eventLabel=V(f"c{kind}.event_label"), impactLabel=V(f"c{kind}.impact_label"),
                 quote=V(f"c{kind}.quote"), source=V(f"c{kind}.source"))
        data[folder + "/data.js"] = "window.CHRONO=%s;\n" % json.dumps(C, ensure_ascii=False, separators=(",", ":"))
        y = kind == "y"
        s = ctpl
        for a, b in (("TITLE", UI("c_year_title" if y else "c_age_title")), ("DESC", UI("c_year_desc" if y else "c_age_desc")),
                     ("OTHER_URL", f"/{l}/jesus/{'ages' if y else 'chronology'}/"), ("OTHER_NAME", UI("c_by_age" if y else "c_by_year"))):
            s = s.replace(f"__{a}__", esc(b))
        s = rep(s, common_head + [
            ('placeholder="Search events (e.g. baptism, Cana)"', f'placeholder="{esc(UI("c_search"))}"'),
            ("list.length + (list.length === 1 ? ' event' : ' events')",
             "(list.length === 1 ? " + jstr(esc(UI("c_one"))) + " : " + jstr(esc(UI("c_many"))) + ").replace('{n}', list.length)"),
            ("(x.age === '1' ? 'year' : 'years')", "(x.age === '1' ? " + jstr(esc(UI("c_year1"))) + " : " + jstr(esc(UI("c_years"))) + ")"),
            ("'<b>Age ' + esc(x.age) + '</b> '", "'<b>' + " + jstr(esc(UI("c_age"))) + ".replace('{n}', esc(x.age)) + '</b> '"),
            ("'<p class=\"empty\">No events found.</p>'", "'<p class=\"empty\">' + " + jstr(esc(UI("c_none"))) + " + '</p>'"),
            ("— The Urantia Book, Part IV</small>", esc(UI("c_quote_by")) + "</small>"),
            ("esc(C.eventLabel || 'Event')", "esc(C.eventLabel)"),
        ], "chronology.html")
        pages[folder + "/index.html"] = s
    ver = hashlib.md5("".join(data[k] for k in sorted(data)).encode("utf-8") + cjs.encode("utf-8")).hexdigest()[:8]
    for k, v in data.items(): w(os.path.join(out, k), v)
    for k, v in pages.items():
        v = v.replace("__V__", ver)
        v = re.sub(r"\?v=[0-9a-f]{8}", "?v=" + ver, v)
        left = re.findall(r"__[A-Z_]+__", v); assert not left, left
        w(os.path.join(out, k), v)

    build_acts(l, out, V, AU, ptitle, stitle, reader)
    build_teachings(l, out, V, UI, ptitle, stitle, reader)

    bad = []
    for dp, _, fs in os.walk(out):
        for f in fs:
            if f.endswith((".html", ".js")) and HANGUL.search(open(os.path.join(dp, f), encoding="utf-8").read()):
                bad.append(os.path.relpath(os.path.join(dp, f), out))
    if bad: raise SystemExit(f"CHECK FAILED: hangul in output {bad}")
    if DRAFT:
        for dp, _, fs in os.walk(out):
            for f in fs:
                if f.endswith(".html"):
                    p = os.path.join(dp, f); t = open(p, encoding="utf-8").read()
                    t = re.sub(r"(<body[^>]*>)", r'\1\n<div style="background:#c00;color:#fff;text-align:center;padding:4px;font:13px sans-serif">DRAFT — not for publication</div>', t, count=1)
                    w(p, t)
    n = sum(len(fs) for _, _, fs in os.walk(out))
    print(f"[{l}{' DRAFT' if DRAFT else ''}] {n} files → {out}")


# ---------------------------------------------------------------- acts
def build_acts(l, out, V, AU, ptitle, stitle, reader):
    from PIL import Image
    d = os.path.join(out, "acts"); os.makedirs(os.path.join(d, "img"))
    src = open(os.path.join(FEJ, "build_acts_web.py"), encoding="utf-8").read()
    ns = {"esc": esc, "os": os, "re": re}
    exec(src[src.index('CSS = r"""'):src.index("# ---------- 한 언어 짓기 ----------")], ns)
    css = ns["CSS"].replace("word-break:keep-all;", "word-break:normal;hyphens:auto;") \
        + 'html[lang=es],html[lang=fr],html[lang=pt]{--sans:"Noto Sans","Segoe UI",Arial,sans-serif;--serif:"Noto Serif",Georgia,serif}\n'
    w(os.path.join(d, "acts.css"), css.strip() + "\n"); w(os.path.join(d, "acts.js"), ns["JS"].strip() + "\n")
    A = SK["acts"]
    ns["L"] = {l: dict(lang=l, font="https://fonts.googleapis.com/css2?family=Noto+Sans:wght@400;500;700&family=Noto+Serif:wght@400;700&display=swap",
                       toc=AU("toc"), title=AU("title"), sub=AU("sub"), other=AU("other"), other_href=FAREAST_EN + "jesus/acts/",
                       home=AU("home"), home_href=f"/{l}/jesus/")}
    page = ns["page"]; toc_html = ns["toc_html"]
    none = AU("none"); cols = (AU("col_event"), AU("col_ub"), AU("col_bible"))
    UBRE = re.compile(r"(\d{1,3}):(\d+)\.(\d+)((?:[–-]\d+)?)")

    def ublink(text):
        s, o, last = esc(text), [], 0
        for m in UBRE.finditer(s):
            o.append(s[last:m.start()])
            o.append(f'<a class="ub" href="{reader}{m.group(1)}:{m.group(2)}.{m.group(3)}" target="_blank" rel="noopener">{m.group(0)}</a>')
            last = m.end()
        o.append(s[last:]); return "".join(o)

    def bib(refs):
        t = kb(l, refs, none)
        if t == none: return f'<span class="none">{esc(none)}</span>'
        return "; ".join(f'<span class="nw">{esc(x)}</span>' for x in t.split("; "))
    dims = {}
    for n in range(1, 39):
        f = os.path.join(ENJ, "acts", "img", f"m{n:02d}.webp")
        shutil.copy(f, os.path.join(d, "img")); dims[n] = Image.open(f).size
    MI = {n: its for n, its in A["maps"]}
    mtitle = lambda n: V(f"acts.map{n}.head")
    msub = lambda n: V(f"acts.map{n}.sub")
    mper = lambda n: msub(n).split("  ·  ")[0]
    ihead = lambda n, k: V(f"acts.map{n}.{k}.head")
    paper_lbl = lambda p: AU("paper").replace("{n}", str(p))
    parts = {p: i + 1 for i, p in enumerate(A["parts"])}
    ptit = lambda i: re.sub(r"\s{2,}", " ", V(f"acts.part{i}.title"))

    pagefile, cur, mappage, plist = {}, None, {}, {}
    for r in A["rows"]:
        if r["kind"] == "paper":
            if r["p"] in parts: cur = f"part{parts[r['p']]}.html"
            plist.setdefault(cur, []).append((f"p{r['p']}", paper_lbl(r["p"]), ptitle(r["p"])))
        elif r["kind"] == "map": mappage[r["n"]] = cur
    pages = [("index.html", AU("front"), [])]
    for i in range(1, len(A["parts"]) + 1): pages.append((f"part{i}.html", ptit(i), plist[f"part{i}.html"]))
    a1, a2 = AU("app1"), AU("app2")
    pages.append(("appendix.html", AU("app"), [("app1", "1", re.split(r"\s{2,}", a1, maxsplit=1)[-1]), ("app2", "2", re.split(r"\s{2,}", a2, maxsplit=1)[-1])]))
    order = [p[0] for p in pages]; labels = {p[0]: p[1] for p in pages}

    def pn(f):
        i = order.index(f)
        return ((order[i - 1], labels[order[i - 1]]) if i else (None, None),
                (order[i + 1], labels[order[i + 1]]) if i < len(order) - 1 else (None, None))

    def write(f, title, desc, content):
        t = page(l, f, title, desc, toc_html(l, pages, f), content, pn(f))
        t = t.replace(f'href="{FAREAST_EN}jesus/acts/{"" if f == "index.html" else f}"', f'href="{FAREAST_EN}jesus/acts/{"" if f == "index.html" else f}" hreflang="en"')
        t = t.replace("<p class=\"foot\">", "<p class=\"foot\">", 1)
        w(os.path.join(d, f), t)
    maplink = lambda n, frm: f"#map{n}" if mappage[n] == frm else f"{mappage[n]}#map{n}"

    ev = [r for r in A["rows"] if r["kind"] in ("sec", "sub")]
    secs = [r for r in ev if r["kind"] == "sec"]
    stats = AU("stats_text").format(ev=len(ev), secs=len(secs), subs=len(ev) - len(secs),
                                    par=len(ev) - sum(1 for r in secs if not r["refs"]), none=sum(1 for r in secs if not r["refs"]),
                                    tagged=sum(len(r["maps"]) for r in ev), ndiff=sum(1 for r in ev if f"acts.note.{r['key']}.diff" in EN))
    c = [f'<h1>{esc(AU("title"))}</h1>', f'<p class="subt">{esc(AU("sub"))}</p>', f'<p class="tag">{esc(AU("tagline"))}</p>',
         f'<h2 class="sec">{esc(AU("guide"))}</h2>', '<div class="prose">']
    c += [f"<p>{esc(V(k))}</p>" for k in EN if k.startswith("acts.guide.")]
    c.append(f'<p class="ni"><b>{esc(AU("stats"))}:</b> {esc(stats)}</p>')
    c.append(f'<h2 class="sec" style="font-size:18px;color:var(--rust)">{esc(AU("notes"))}</h2><ul>')
    c += [f"<li>{esc(V(k))}</li>" for k in EN if k.startswith("acts.fix.")]
    c.append("</ul></div>")
    c.append(f'<div class="cta"><a href="part1.html">{esc(AU("start"))} →</a></div>')
    write("index.html", f'{AU("title")} — {AU("sub")}', AU("tagline"), "\n".join(c))

    thead = (f'<table class="acts"><colgroup><col class="c1"><col class="c2"><col class="c3"></colgroup><thead><tr><th>{esc(cols[0])}</th>'
             f'<th>{esc(cols[1])}</th><th>{esc(cols[2])}</th></tr></thead><tbody>')
    buf, pending, state = [], [], {"cur": None, "table": False}

    def close_table():
        if state["table"]: buf.append("</tbody></table>"); state["table"] = False

    def flush():
        close_table()
        for n in pending:
            wd, ht = dims[n]; li = []
            for num, col, ref in MI[n]:
                li.append(f'<li><span class="c" style="color:{col}">{CIRC[num - 1]}</span><span class="h" style="color:{col}">{esc(ihead(n, num))}</span>'
                          f'{esc(V(f"acts.map{n}.{num}.body"))} <span class="r">[{ublink(ref)}]</span></li>')
            buf.append(f'<figure class="map" id="map{n}"><h4><span class="mn">{esc(AU("map"))} {n}</span>{esc(mtitle(n))}</h4>'
                       f'<div class="per">{esc(msub(n))}</div>'
                       f'<a class="img" href="img/m{n:02d}.webp" target="_blank" rel="noopener"><img src="img/m{n:02d}.webp" width="{wd}" height="{ht}" loading="lazy" decoding="async" alt="{esc(AU("map"))} {n}: {esc(mtitle(n))}"></a>'
                       f'<div class="big"><a href="img/m{n:02d}.webp" target="_blank" rel="noopener">{esc(AU("enlarge"))} ↗</a></div>'
                       f'<ol>{"".join(li)}</ol></figure>')
        pending.clear()

    def end_page():
        flush()
        if state["cur"]:
            i = int(state["cur"][4:-5])
            write(state["cur"], f'{ptit(i)} — {AU("title")}', f'{ptit(i)} ({V(f"acts.part{i}.range")})', "\n".join(buf))
        buf.clear()
    for r in A["rows"]:
        if r["kind"] == "paper":
            flush()
            if r["p"] in parts:
                end_page(); i = parts[r["p"]]; state["cur"] = f"part{i}.html"
                buf.append(f'<h2 class="part">{esc(ptit(i))}</h2><p class="rng">{esc(V(f"acts.part{i}.range"))}</p>')
            per = V(f"acts.per.{r['p']}") if r["per"] else ""
            buf.append(f'<h3 class="paper" id="p{r["p"]}"><span class="no">{esc(paper_lbl(r["p"]))}</span>{esc(ptitle(r["p"]))}'
                       + (f'<span class="per">{esc(per)}</span>' if per else "") + "</h3>")
            buf.append(thead); state["table"] = True
            continue
        if r["kind"] == "map":
            n = r["n"]
            buf.append(f'<tr class="band"><td colspan="3"><a href="{maplink(n, state["cur"])}"><span class="mn">{esc(AU("map"))} {n}</span>'
                       f'<span class="t">{esc(mtitle(n))}</span><span class="mp">{esc(mper(n))}</span></a></td></tr>')
            pending.append(n); continue
        sub = r["kind"] == "sub"
        if sub: name = V(f"acts.sub.{r['ub']}")
        elif r["s"]: name = f"{r['s']}. " + stitle(r["p"], r["s"])
        else: name = V(f"acts.intro.{r['p']}") if f"acts.intro.{r['p']}" in EN else AU("intro_default")
        tags = "".join(f'<span class="mt"><a href="{maplink(n, state["cur"])}">{esc(AU("map"))} {n}-{CIRC[num - 1]}</a> <span>{esc(ihead(n, num))}</span></span>'
                       for n, num in r["maps"])
        kd, kf = f"acts.note.{r['key']}.desc", f"acts.note.{r['key']}.diff"
        has = kd in EN or kf in EN
        cls = "ev" + (" sub" if sub else "") + (" hasnote" if has else "")
        buf.append(f'<tr class="{cls}"><td class="e">{esc(name)}{tags}</td><td class="u" data-l="{esc(cols[1])}">{ublink(r["ub"])}</td>'
                   f'<td class="b" data-l="{esc(cols[2])}">{bib(r["refs"])}</td></tr>')
        if has:
            t = esc(V(kd)) if kd in EN else ""
            if kf in EN: t += f'<span class="df"><b>{esc(AU("diff"))}</b>{esc(V(kf))}</span>'
            buf.append(f'<tr class="nt{" sub" if sub else ""}"><td colspan="3">{t}</td></tr>')
    end_page()
    c = [f'<h2 class="part" id="app1">{esc(a1)}</h2>', f'<div class="prose"><p>{esc(V("acts.appx.1"))}</p></div>', thead]
    for i, refs in enumerate(A["bible_only"]):
        c.append(f'<tr class="ev"><td class="e">{esc(V(f"acts.bo{i + 1}"))}</td><td class="u" data-l="{esc(cols[1])}"><span class="none">{esc(none)}</span></td>'
                 f'<td class="b" data-l="{esc(cols[2])}">{bib(refs)}</td></tr>')
    c.append("</tbody></table>")
    c += [f'<h2 class="part" id="app2" style="margin-top:44px">{esc(a2)}</h2>', f'<div class="prose"><p>{esc(V("acts.appx.2"))}</p></div>',
          f'<table class="acts two"><colgroup><col class="c1"><col class="c2"></colgroup><thead><tr><th>{esc(AU("app2col"))}</th><th>{esc(cols[1])}</th></tr></thead><tbody>']
    for n, its in A["maps"]:
        c.append(f'<tr class="band"><td colspan="2"><a href="{mappage[n]}#map{n}"><span class="mn">{esc(AU("map"))} {n}</span><span class="t">{esc(mtitle(n))}</span><span class="mp">{esc(mper(n))}</span></a></td></tr>')
        for num, col, ref in its:
            c.append(f'<tr><td><b style="color:var(--rust)">{CIRC[num - 1]}</b> {esc(ihead(n, num))}</td><td class="u">{ublink(ref)}</td></tr>')
    c.append("</tbody></table>")
    write("appendix.html", f'{AU("app")} — {AU("title")}', AU("app"), "\n".join(c))


# ---------------------------------------------------------------- teachings
HOME_CSS = (".ur-home-btn{display:inline-flex;align-items:center;gap:4px;flex:0 0 auto;margin-right:6px;padding:8px 14px;"
            "border-radius:999px;background:#ff5a1f;color:#fff!important;border:2px solid #fff;box-shadow:0 2px 6px rgba(0,0,0,.25);"
            "font:700 13.5px/1.1 \"Segoe UI\",system-ui,sans-serif;text-decoration:none!important;white-space:nowrap}"
            ".ur-home-btn:hover{background:#e64a10}@media print{.ur-home-btn{display:none}}")


def build_teachings(l, out, V, UI, ptitle, stitle, reader):
    src = open(os.path.join(ENJ, "teachings", "index.html"), encoding="utf-8").read()
    body = open(os.path.join(H, "src", "teachings_body.html"), encoding="utf-8").read()
    sub = {"T": lambda k: esc(V(k)), "R": lambda k: esc(V(k)), "B": lambda t: esc(bible(l, html.unescape(t))),
           "UI": lambda n: esc(UI(n)), "PT": lambda p: esc(ptitle(int(p)))}
    body = re.sub(r"⟦UIF (\w+) (\d+)⟧", lambda m: esc(UI(m.group(1)).replace("{n}", m.group(2))), body)
    body = re.sub(r"⟦ST (\d+) (\d+)⟧", lambda m: esc(stitle(int(m.group(1)), int(m.group(2)))), body)
    body = re.sub(r"⟦(T|R|B|UI|PT) ([^⟧]+)⟧", lambda m: sub[m.group(1)](m.group(2)), body)
    assert "⟦" not in body, re.findall(r"⟦[^⟧]*⟧", body)[:5]

    def reflink(m):
        t = m.group(1)
        t = re.sub(r"\b(\d{3}):(\d+)(?:\.(\d+))?", lambda x: f'<a href="{reader}{x.group(1)}:{x.group(2)}.{x.group(3) or "1"}" target="_blank" rel="noopener">{x.group(0)}</a>', t)
        return f'<span class="ref">{t}</span>'
    body = re.sub(r'<span class="ref">(.*?)</span>', reflink, body)
    css = src[src.index("<style>") + 7:src.index("</style>")]
    css += ("\n/* es·fr·pt */\n.section-body p.ubq { border-left: 2px solid var(--gold-dim); padding-left: 14px; }\n"
            ".section-body .qlabel { color: var(--gold); }\n.section-body .ref a { color: inherit; }\n" + HOME_CSS + "\n")
    parts = ("sayings", "miracles", "parables", "sermons")
    groups, order = {}, []
    for m in re.finditer(r'<article class="section-content" id="sec-([^"]+)">.*?<h2>(.*?)</h2>', body, re.S):
        aid, h2 = m.group(1), html.unescape(m.group(2)); part = aid.split("-")[0]
        mm = re.match(r"^(\d+)\.\s*(.*)$", h2)
        n, t = (mm.group(1) + ".", mm.group(2)) if mm else ("", h2)
        if part not in groups: groups[part] = []; order.append(part)
        groups[part].append(f'<div class="section-item" onclick="showSection(\'{aid}\')" id="item-{aid}"><span class="item-num">{n}</span>'
                            f'<span class="item-title">{esc(t)}</span></div>')
    side = "".join(f'<div class="part-group" data-part="{p}"><div class="part-header" onclick="togglePart(\'{p}\')"><span class="part-icon">✦</span>'
                   f'<span class="part-title">{esc(UI("t_part_" + p))}</span><span class="chevron">›</span></div><div class="section-list" id="list-{p}">'
                   + "".join(groups[p]) + "</div></div>" for p in order)
    a = src.rindex("</article>") + len("</article>"); tail = src[a:src.index("<script>", a)]
    tail = rep(tail, [(">‹ Previous<", f">{esc(UI('t_prev'))}<"), (">Next ›<", f">{esc(UI('t_next'))}<"),
                      (">Share This Reading<", f">{esc(UI('t_share_h'))}<"),
                      (">Generate a beautiful image to share on social media<", f">{esc(UI('t_share_p'))}<"),
                      (">↓ Download Image<", f">{esc(UI('t_dl'))}<"), (">⎘ Copy to Clipboard<", f">{esc(UI('t_copy'))}<"),
                      (">Close<", f">{esc(UI('t_close'))}<")], "teachings tail")
    bs = src.index("<body>"); script = src[src.index("<script>", bs):src.rindex("</script>") + 9]
    lab = re.escape(UI("t_ref")).replace("/", "\\/")
    script = rep(script, [
        ("const group = document.querySelector();", "const group = document.querySelector(`.part-group[data-part=\"${partId}\"]`);"),
        ("text = text.replace(/UB p\\.\\d+/g, '').trim();", f"text = text.replace(/{lab} [0-9:.;,\\- –]+/g, '').replace(/\\s+/g, ' ').trim();"),
        ("'THE TEACHINGS OF JESUS  ·  URANTIA BOOK WORKBOOK'", jstr(UI("t_canvas_top"))),
        ("sec ? sec.tag.toUpperCase() : 'THE TEACHINGS OF JESUS'", "sec ? sec.tag.toUpperCase() : " + jstr(UI("t_title").upper())),
        ("sec ? sec.title : 'Organized by Jay Han'", "sec ? sec.title : " + jstr(UI("t_credit"))),
        ("'ORGANIZED BY JAY HAN'", jstr(UI("t_credit").upper())),
        ("alert('Image copied to clipboard!')", "alert(" + jstr(UI("t_copied")) + ")"),
        ("alert('Copy not supported in this browser. Please use Download instead.')", "alert(" + jstr(UI("t_nocopy")) + ")"),
        ("a.download = 'urantia-teachings-jay-han.png'", f"a.download = 'urantia-teachings-{l}-jay-han.png'")], "teachings script")
    t = esc
    wp = "".join(f'''          <div class="welcome-part-item" onclick="jumpToPart('{p}')">
            <span class="wpi-icon">{ic}</span>
            <span class="wpi-roman">{t(UI("t_roman%d" % (i + 1)))}</span>
            <span class="wpi-title">{t(UI("t_part_" + p))}</span>
            <span class="wpi-arrow">›</span>
          </div>
''' for i, (p, ic) in enumerate(zip(parts, "✦✧◈❋")))
    tabs = "".join(f'        <div class="part-tab" onclick="filterPart(\'{p}\')">{t(UI("t_tab_" + p))}</div>\n' for p in parts)
    pg = f'''<!DOCTYPE html>
<html lang="{l}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t(UI("t_title"))} — {t(UI("t_sub"))}</title>
<meta name="description" content="{t(UI("t_desc"))}">
<meta property="og:type" content="website">
<meta property="og:title" content="{t(UI("t_title"))}">
<meta property="og:description" content="{t(UI("t_desc"))}">
<meta property="og:site_name" content="Urantia America">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,300;0,400;0,600;1,300;1,400&family=Cinzel:wght@400;600&family=EB+Garamond:ital,wght@0,400;0,500;1,400&display=swap" rel="stylesheet">
<style>{css}</style>
</head>
<body>
<header>
  <a class="ur-home-btn" href="/{l}/jesus/" target="_top" title="{t(UI("home_title"))}">{t(UI("home"))}</a>
  <button class="menu-btn" onclick="toggleMobileMenu()" title="{t(UI("t_menu"))}">☰</button>
  <div class="header-ornament">✦</div>
  <div>
    <div class="header-title">{t(UI("t_title"))}</div>
    <div class="header-subtitle">{t(UI("t_sub"))}</div>
  </div>
  <div class="header-right">
    <button class="share-btn" onclick="openShareModal()">{t(UI("t_share"))}</button>
  </div>
</header>

<div class="app-body">
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-top">
      <div class="sidebar-label">{t(UI("t_nav"))}</div>
      <div class="part-tabs">
        <div class="part-tab active" onclick="filterPart('all')">{t(UI("t_all"))}</div>
{tabs}      </div>
    </div>
    <div class="search-wrap">
      <input class="search-input" type="text" placeholder="{t(UI("t_search"))}" oninput="searchSections(this.value)" id="searchInput">
    </div>
    {side}
  </aside>

  <main class="main" id="mainContent">
    <div class="main-inner">
      <div class="welcome" id="welcomeScreen">
        <div class="welcome-symbol">✦</div>
        <h1>{t(UI("t_title"))}</h1>
        <p>{t(UI("t_welcome"))}</p>
        <div class="welcome-parts">
{wp}        </div>
        <div class="welcome-credit">{t(UI("t_credit"))}</div>
      </div>
      {body}
{tail}
{script}
</body>
</html>
'''
    w(os.path.join(out, "teachings", "index.html"), pg)
    shutil.copy(os.path.join(ENJ, "teachings", "favicon.ico"), os.path.join(out, "teachings", "favicon.ico"))


fail_any = False
for l in LANGS:
    BOOK, TIT, T = load(l)
    failed = check(l, BOOK, T)
    fail_any |= failed
    if CHUNK: continue
    if failed and not DRAFT:
        print(f"CHECK FAILED [{l}] — site/{l}/jesus/ not written (use --draft for a preview)"); continue
    build(l, BOOK, TIT, T)
if fail_any: print("errors 1"); sys.exit(1)
print("errors 0")
