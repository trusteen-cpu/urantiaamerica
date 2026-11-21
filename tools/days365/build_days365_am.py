# -*- coding: utf-8 -*-
# 365 Days with The Urantia Book — es / fr / pt → site/<l>/365days/ (days.json + index.html)
#   Port of the Far East tools/zh/days365/build_days365_zh.py. The page template is the Far East English
#   tools/days365_en/page.html (read only), patched here. Nothing in the Far East folder is written.
#   Inputs:  src/cNN.json (English units)  +  <l>/cNN.json (translation, same keys and structure)
#   Daily blockquote = tools/data/<l>.json verses cit..cit_end (never translated); source line = official paper title.
#   Inline ⟦Q cit⟧…⟦/Q⟧ must be verbatim in tools/data/<l>.json[cit] (whitespace ignored; " … " allowed).
#   python build_days365_am.py es [fr pt]          checks; writes site/<l>/365days/ only if all checks pass
#   python build_days365_am.py es --chunk c03      checks that chunk only (writes nothing)
#   python build_days365_am.py es --draft          English fill-in for missing units → tools/days365/_draft_<l>/
import datetime, html, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
args = sys.argv[1:]
DRAFT = "--draft" in args
CHUNK = args[args.index("--chunk") + 1] if "--chunk" in args else None
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]

EN_BOOK = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
KEYS = list(EN_BOOK); IDX = {k: i for i, k in enumerate(KEYS)}
ENTRIES = json.load(open(os.path.join(FE, "tools", "days365_en", "entries.json"), encoding="utf-8"))
CHUNKS = sorted(f[:-5] for f in os.listdir(os.path.join(H, "src")) if re.fullmatch(r"c\d\d\.json", f))
EN, CH = {}, {}
for c in CHUNKS:
    d = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
    EN.update(d); CH.update({k: c for k in d})
HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their|you|your)\b")
QM = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧", re.S)
nows = lambda s: re.sub(r"\s+", "", s.replace("\u00a0", " "))
strip = lambda s: QM.sub(lambda m: m.group(2), s)

# Dates are produced by the builder (not translated): month names, day-month order, ordinal for day 1, separator before a title.
DATE = {
    "es": (["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
           "{d} de {m}", "1", ": "),
    "fr": (["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "décembre"],
           "{d} {m}", "1er", "\u00a0: "),
    "pt": (["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"],
           "{d} de {m}", "1º", ": "),
}


def fr_nb(s):
    """French no-break spaces, applied outside quotation markers only."""
    parts = re.split(r"(⟦Q [^⟧]+⟧.*?⟦/Q⟧)", s, flags=re.S)
    f = lambda t: re.sub(r"«\s", "«\u00a0", re.sub(r"\s([;:!?»])", "\u00a0\\1", t))
    return "".join(p if p.startswith("⟦Q ") else f(p) for p in parts)


def ref_keys(ref):
    m = re.fullmatch(r"(\d+):(\d+)\.(\d+)(?:[–\-](?:(\d+):(\d+)\.)?(\d+))?", ref.strip())
    if not m: return None
    a = f"{m.group(1)}:{m.group(2)}.{m.group(3)}"
    if not m.group(6): b = a
    elif m.group(4): b = f"{m.group(4)}:{m.group(5)}.{m.group(6)}"
    else: b = f"{m.group(1)}:{m.group(2)}.{m.group(6)}"
    if a not in IDX or b not in IDX: return None
    return KEYS[IDX[a]:IDX[b] + 1]


def load(l):
    BOOK = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
    TT = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}_titles.json"), encoding="utf-8"))
    T = {}
    for c in CHUNKS:
        if CHUNK and c != CHUNK: continue
        p = os.path.join(H, l, c + ".json")
        if os.path.exists(p): T.update(json.load(open(p, encoding="utf-8")))
        else: print(f"  [missing file] {l}/{c}.json")
    return BOOK, TT, T


def check(l, BOOK, T):
    errs, warns, badq = [], [], []
    nq = [0]

    def text(tag, es_, ts):
        if not isinstance(ts, str): errs.append(f"not a string: {tag}"); return
        if not ts.strip(): errs.append(f"empty: {tag}")
        if HANGUL.search(ts): errs.append(f"hangul: {tag}")
        qe = [m.group(1) for m in QM.finditer(es_)]; qt = [m.group(1) for m in QM.finditer(ts)]
        if qe != qt: errs.append(f"quotation markers changed: {tag} en={qe} {l}={qt}")
        if "⟦" in strip(ts) or "⟧" in strip(ts): errs.append(f"broken marker: {tag}")
        for m in QM.finditer(ts):
            nq[0] += 1
            hay = nows(BOOK.get(m.group(1), ""))
            pieces = [nows(p).strip("“”\"'‘’«»") for p in re.split(r"…|\.\.\.", m.group(2))]
            pieces = [p for p in pieces if p]
            bad = [p for p in pieces if p not in hay]
            if not pieces or bad: badq.append(f"{tag} [{m.group(1)}] {(bad or ['(empty)'])[0][:50]}")
        if "/ui." in tag:
            ph = set(re.findall(r"\{\w+\}", es_))
            if ph != set(re.findall(r"\{\w+\}", ts)): errs.append(f"placeholder {sorted(ph)} lost: {tag}")
            if nows(ts) == nows(es_) and len(es_.split()) > 2: warns.append(f"untranslated? {tag}")
            return
        plain = re.sub(r"⟦Q[^⟧]*⟧.*?⟦/Q⟧|\([^)]*\)", "", ts, flags=re.S)
        hits = ENGW.findall(plain)
        if nows(strip(ts)) == nows(strip(es_)) and len(es_.split()) > 3: warns.append(f"untranslated? {tag}")
        elif len(hits) >= 2: warns.append(f"English words {hits[:4]}: {tag}")

    for k, ev in EN.items():
        c = CH[k]
        if CHUNK and c != CHUNK: continue
        if k not in T: errs.append(f"missing: {c}/{k}"); continue
        tv = T[k]
        if isinstance(ev, str): text(f"{c}/{k}", ev, tv); continue
        if not isinstance(tv, dict) or set(tv) != set(ev) or tv.get("_ref") != ev["_ref"] \
                or not isinstance(tv.get("msg"), list) or len(tv["msg"]) != len(ev["msg"]):
            errs.append(f"structure (keys, _ref or number of msg paragraphs): {c}/{k}"); continue
        text(f"{c}/{k}.t", ev["t"], tv["t"])
        for i, (a, b) in enumerate(zip(ev["msg"], tv["msg"])): text(f"{c}/{k}.msg[{i}]", a, b)
        text(f"{c}/{k}.pr", ev["pr"], tv["pr"])
    for k in T:
        if k not in EN: errs.append(f"extra key: {k}")
    scope = f" chunk {CHUNK}" if CHUNK else ""
    n_all = sum(1 for k in EN if not CHUNK or CH[k] == CHUNK)
    print(f"[{l}{scope}] translated: {sum(1 for k in EN if k in T and (not CHUNK or CH[k] == CHUNK))}/{n_all} units · "
          f"inline quotations checked: {nq[0]} · bad: {len(badq)} · errors {len(errs)} · warnings {len(warns)}")
    for e in errs[:40]: print("  ERR", e)
    if len(errs) > 40: print(f"  … {len(errs) - 40} more errors")
    for b in badq[:40]: print("  BADQ", b)
    if len(badq) > 40: print(f"  … {len(badq) - 40} more bad quotations")
    for w in warns[:30]: print("  WARN", w)
    if len(warns) > 30: print(f"  … {len(warns) - 30} more warnings")
    return bool(errs or badq)


def build(l, BOOK, TT, T):
    def V(k):
        v = T.get(k, EN[k]) if DRAFT else T[k]
        if DRAFT and isinstance(EN[k], dict) and (not isinstance(v, dict) or set(v) != set(EN[k])
                                                  or len(v.get("msg", [])) != len(EN[k]["msg"])):
            v = EN[k]
        if l == "fr":
            v = fr_nb(v) if isinstance(v, str) else dict(v, t=fr_nb(v["t"]), msg=[fr_nb(x) for x in v["msg"]], pr=fr_nb(v["pr"]))
        return v
    UI = {k[3:]: strip(V(k)) for k in EN if k.startswith("ui.")}
    MN, DF, D1, SEP = DATE[l]

    days, d0 = [], datetime.date(2027, 1, 1)
    for e in ENTRIES:
        k = "d%03d" % e["day"]; u = V(k)
        assert u["_ref"] == e["cit"] + ("–" + e["cit_end"] if e.get("cit_end") else ""), k
        dt = d0 + datetime.timedelta(days=e["day"] - 1)
        ks = ref_keys(u["_ref"])
        ref = e["cit"]
        if e.get("cit_end"):
            p1, p2 = e["cit"].split(":")[0], e["cit_end"].split(":")[0]
            ref += "–" + (e["cit_end"].split(":")[1] if p1 == p2 else e["cit_end"])
        p = e["paper"]
        src = TT["0"]["title"] if p == 0 else f"{UI['paper_label'].format(n=p)} · {TT[str(p)]['title']}"
        days.append({"d": e["day"], "m": dt.month, "md": dt.day, "src": src, "ref": ref, "cit": e["cit"],
                     "t": strip(u["t"]), "q": [BOOK[x] for x in ks], "msg": [strip(x) for x in u["msg"]], "pr": strip(u["pr"])})
    assert len(days) == 365

    t = open(os.path.join(FE, "tools", "days365_en", "page.html"), encoding="utf-8").read()
    A = lambda s: html.escape(s, quote=True)
    J = lambda s: s.replace("\\", "\\\\").replace("'", "\\'")
    dl = UI["day_label"].split("{n}", 1) if "{n}" in UI["day_label"] else [UI["day_label"] + " ", ""]
    fd = lambda m, d: f"fd({m}, {d})"
    R = [
        ('<html lang="en">', f'<html lang="{l}">'),
        ('<title>365 Days with The Urantia Book | Urantia Far East</title>', f'<title>{A(UI["page_title"])}</title>'),
        ('content="One passage of The Urantia Book for every day of the year, with a meditation and a practice for the day."', f'content="{A(UI["meta_description"])}"'),
        ('<link rel="canonical" href="https://urantiafareast.com/en/365days/">\n', ''),
        ('<meta property="og:title" content="365 Days with The Urantia Book">', f'<meta property="og:title" content="{A(UI["page_title"])}">'),
        ('<meta property="og:description" content="One passage a day, a year-long spiritual journey.">', f'<meta property="og:description" content="{A(UI["og_description"])}">'),
        ('<h1>365 Days with The Urantia Book</h1>', f'<h1>{A(UI["page_title"])}</h1>'),
        ('<p>One passage a day, a year-long spiritual journey</p>', f'<p>{A(UI["subtitle"])}</p>'),
        ('aria-label="Choose a day"', f'aria-label="{A(UI["aria_choose_day"])}"'),
        ('aria-label="Previous day">‹ Prev</button>', f'aria-label="{A(UI["aria_prev"])}">{A(UI["prev"])}</button>'),
        ('aria-label="Month"', f'aria-label="{A(UI["aria_month"])}"'),
        ('aria-label="Day"', f'aria-label="{A(UI["aria_day"])}"'),
        ('aria-label="Next day">Next ›</button>', f'aria-label="{A(UI["aria_next"])}">{A(UI["next"])}</button>'),
        ('id="today">Today</button>', f'id="today">{A(UI["today_button"])}</button>'),
        ('>Loading…</p>', f'>{A(UI["loading"])}</p>'),
        ('<summary>All 365 days</summary>', f'<summary>{A(UI["toc_summary"])}</summary>'),
        ('The quotations are from the original English text of <i>The Urantia Book</i>. The meditations are commentary on each passage and are not part of <i>The Urantia Book</i> itself.', UI["about_html"]),
        ("var MN = ['January','February','March','April','May','June','July','August','September','October','November','December'];",
         "var MN = [" + ",".join(f"'{J(m)}'" for m in MN) + "];\n"
         f"var DF = '{J(DF)}', D1 = '{J(D1)}', SEP = '{J(SEP)}';\n"
         "function cap(s) { return s.charAt(0).toUpperCase() + s.slice(1); }\n"
         "function fd(m, d) { return DF.replace('{d}', d === 1 ? D1 : d).replace('{m}', MN[m - 1]); }"),
        ("// 윤년 2월 29일은 28일 쪽을 보여 준다", "// Feb 29 (leap year) shows the Feb 28 page"),
        ("MN[x.m - 1] + ' ' + x.md + '</div><div class=\"dayno\">DAY ' + ('00' + x.d).slice(-3) + '</div>",
         f"{fd('x.m', 'x.md')} + '</div><div class=\"dayno\">{J(A(dl[0]))}' + ('00' + x.d).slice(-3) + '{J(A(dl[1]))}</div>"),
        ("<a href=\"/en/book/#' + x.cit + '\" title=\"Open in The Urantia Book\">'", f"<a href=\"/{l}/book/#' + x.cit + '\" title=\"{J(A(UI['open_in_book']))}\">'"),
        ("'<cite>— The Urantia Book ' + esc(x.ref)", f"'<cite>{J(A(UI['cite_prefix']))} ' + esc(x.ref)"),
        ("'<div class=\"practice\"><b>Today</b>", f"'<div class=\"practice\"><b>{J(A(UI['practice_label']))}</b>"),
        ("MN[prev.m - 1] + ' ' + prev.md + ': '", f"{fd('prev.m', 'prev.md')} + SEP"),
        ("MN[next.m - 1] + ' ' + next.md + ': '", f"{fd('next.m', 'next.md')} + SEP"),
        ("document.title = MN[x.m - 1] + ' ' + x.md + ': ' + x.t + ' | 365 Days with The Urantia Book';",
         f"document.title = {fd('x.m', 'x.md')} + SEP + x.t + ' | {J(UI['page_title'])}';"),
        ("o.textContent = n; ms.appendChild(o);", "o.textContent = cap(n); ms.appendChild(o);"),
        ("COLORS[i][0] + '\">' + n + '</h3>", "COLORS[i][0] + '\">' + cap(n) + '</h3>"),
        ("'<p style=\"text-align:center\">The daily pages could not be loaded. Please reload the page.</p>'",
         f"'<p style=\"text-align:center\">{J(A(UI['load_error']))}</p>'"),
    ]
    for a, b in R:
        if a not in t: raise SystemExit("page.html: not found: " + a[:80])
        t = t.replace(a, b)
    if DRAFT:
        t = t.replace("<body>\n", '<body>\n<div style="background:#c00;color:#fff;text-align:center;padding:4px;font:13px sans-serif">DRAFT — not for publication</div>\n', 1)
    blob = t + json.dumps(days, ensure_ascii=False)
    post = {"hangul": len(HANGUL.findall(blob)), "/en/": t.count("/en/"), "urantiafareast": blob.lower().count("far east") + blob.count("urantiafareast")}
    if any(post.values()):
        raise SystemExit(f"[{l}] OUTPUT CHECK FAILED {post}")
    out = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "365days")
    os.makedirs(out, exist_ok=True)
    json.dump(days, open(os.path.join(out, "days.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(t)
    print(f"[{l}{' DRAFT' if DRAFT else ''}] 365 days, {sum(len(d['q']) for d in days)} passage verses → {out}")


fail_any = False
for l in LANGS:
    BOOK, TT, T = load(l)
    failed = check(l, BOOK, T)
    fail_any |= failed
    if CHUNK: continue
    if failed and not DRAFT:
        print(f"CHECK FAILED [{l}] — site/{l}/365days/ not written (use --draft for a preview)"); continue
    build(l, BOOK, TT, T)
if fail_any: print("errors 1"); sys.exit(1)
print("errors 0")
