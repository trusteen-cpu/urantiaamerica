# -*- coding: utf-8 -*-
# 「376 Key Lists in The Urantia Book」 스페인어·프랑스어·포르투갈어판 → site/<es|fr|pt>/lists/ (data.json + index.html)
#   원본 구조: urantiafareast 홈페이지/site/en/lists/data.json, index.html (읽기만 한다)
#   원고: src/cNN.json (영어, 극동판 중국어판과 같은 단위) + <l>/c*.json (번역, 같은 키·같은 구조; 여러 파일로 나눠도 됨)
#   검사: 키 누락·중복, 구조(열 수·행 수·칸 수, 번호 칸·빈 칸 그대로), 한글, {n},
#         인용 ⟦Q 절⟧…⟦/Q⟧ 가 공식 번역 <l>.json[절] 에 글자 그대로 있는지(amq.check),
#         영어 칸이 본문 글자 그대로인 곳은 번역 칸도 공식 번역 본문 글자 그대로인지 비율 보고(경고).
#   하나라도 틀리면 그 언어는 쓰지 않고 끝 코드 1.
#   python build_lists_am.py [es fr pt] [--preview]
import json, os, re, sys, glob, unicodedata
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
SITE = os.path.join(ROOT, "site")
FE = os.path.normpath(os.path.join(ROOT, "..", "urantiafareast 홈페이지", "site", "en", "lists"))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import amq  # noqa: E402

PREVIEW = "--preview" in sys.argv
KEYS = None  # --keys 48-94 : 그 목록만 검사(번역자용, 만들지 않음)
if "--keys" in sys.argv:
    _a, _, _b = sys.argv[sys.argv.index("--keys") + 1].partition("-")
    KEYS = {"L%03d" % i for i in range(int(_a), int(_b or _a) + 1)} | ({"ui"} if int(_a) == 1 else set())
LANGS = [a for a in sys.argv[1:] if a in amq.LANGS] or list(amq.LANGS)
EN_DATA = json.load(open(os.path.join(FE, "data.json"), encoding="utf-8"))
EN_HTML = open(os.path.join(FE, "index.html"), encoding="utf-8").read()
EN = json.load(open(r"E:\OneDrive\유란시아 작업\theology-book\en.json", encoding="utf-8"))
REFS = json.load(open(os.path.join(H, "src", "refs.json"), encoding="utf-8"))
SRC = {}
for p in sorted(glob.glob(os.path.join(H, "src", "c[0-9][0-9].json"))):
    SRC.update(json.load(open(p, encoding="utf-8")))
assert len(SRC) == 377 and len(EN_DATA) == 376

QM = re.compile(r"⟦Q ([0-9]+:[0-9]+\.[0-9]+)⟧(.*?)⟦/Q⟧", re.S)
HANGUL = re.compile(r"[가-힣ㄱ-ㆎ]")
HTML_LANG = {"es": "es", "fr": "fr", "pt": "pt-BR"}


def strs(x):
    if isinstance(x, str): yield x
    elif isinstance(x, dict):
        for v in x.values(): yield from strs(v)
    else:
        for v in x: yield from strs(v)


def W(s):  # 낱말만 (대소문자·문장부호 무시)
    return " ".join(re.findall(r"\w+", s.lower()))


def fr_nb(s):
    """프랑스어: ; : ! ? » 앞과 « 뒤 공백 → 줄바꿈 없는 공백 (인용 안쪽은 건드리지 않음)."""
    parts = re.split(r"(⟦Q [^⟧]+⟧.*?⟦/Q⟧)", s, flags=re.S)
    for i in range(0, len(parts), 2):
        t = re.sub(r" ([;:!?»])", "\u00a0\\1", parts[i])
        parts[i] = t.replace("« ", "«\u00a0")
    return "".join(parts)


def load(l):
    T, dup = {}, []
    for p in sorted(glob.glob(os.path.join(H, l, "c*.json"))):
        for k, v in json.load(open(p, encoding="utf-8")).items():
            if k in T: dup.append(k)
            T[k] = v
    return T, dup


def check(l, T, dup):
    err = {"missing": [], "extra": [k for k in T if k not in SRC], "dup": dup, "struct": [], "hangul": [],
           "quote_count": [], "quote_bad": [], "ui": [], "marker": []}
    same, qn, vb = [], 0, [0, 0, []]

    def quotes(key, a, b):
        nonlocal qn
        x, y = QM.findall(a), QM.findall(b)
        if [c for c, _ in x] != [c for c, _ in y]: err["quote_count"].append((key, [c for c, _ in x], [c for c, _ in y]))
        for cit, inner in y:
            qn += 1
            if not inner.strip() or not amq.check(l, cit, inner): err["quote_bad"].append((key, cit, inner[:60]))
        if "⟦" in QM.sub("", b) or "⟧" in QM.sub("", b): err["marker"].append(key)

    for k, ev in SRC.items():
        if KEYS is not None and k not in KEYS: continue
        if k not in T: err["missing"].append(k); continue
        tv = T[k]
        for s in strs(tv):
            if HANGUL.search(s): err["hangul"].append((k, s[:40]))
        if k == "ui":
            if not isinstance(tv, dict) or set(tv) != set(ev): err["ui"].append("ui keys differ"); continue
            for u, s in ev.items():
                if ("{n}" in s) != ("{n}" in tv[u]) or not str(tv[u]).strip(): err["ui"].append(u)
            continue
        ok = (isinstance(tv, dict) and set(tv) == {"t", "cols", "rows", "d"}
              and isinstance(tv["cols"], list) and len(tv["cols"]) == len(ev["cols"])
              and isinstance(tv["rows"], list) and len(tv["rows"]) == len(ev["rows"])
              and all(isinstance(r, list) and len(r) == len(er) for r, er in zip(tv["rows"], ev["rows"])))
        if not ok: err["struct"].append(k); continue
        for a, b in zip(ev["cols"], tv["cols"]):
            if (a == "") != (b == ""): err["struct"].append(k + " cols blank")
        en_body = " ".join(W(EN.get(p, "")) for p in REFS[k]["src"])
        tr_body = " ".join(W(amq._load(l).get(p, "")) for p in REFS[k]["src"])
        for er, tr in zip(ev["rows"], tv["rows"]):
            for a, b in zip(er, tr):
                if not isinstance(b, str) or (re.fullmatch(r"[0-9]*", a) and a != b):
                    err["struct"].append(f"{k} number cell {a!r}->{b!r}")
                elif a and a == b and re.search(r"[A-Za-z]{4,}", a) and " " in a:
                    same.append(k)
                elif len(a.split()) >= 3 and "⟦" not in a and W(a) in en_body:
                    vb[0] += 1
                    if W(b) in tr_body: vb[1] += 1
                    else: vb[2].append((k, b[:50]))
                quotes(k, a, b)
        if not str(tv["t"]).strip() or not str(tv["d"]).strip(): err["struct"].append(k + " empty t/d")
        quotes(k, ev["d"], tv["d"]); quotes(k, ev["t"], tv["t"])
    return err, same, qn, vb


def jsq(s): return json.dumps(s, ensure_ascii=False)


def fmt(tpl, expr):
    a, b = tpl.split("{n}", 1) if "{n}" in tpl else (tpl, "")
    out = []
    if a: out.append(jsq(a))
    if "{n}" in tpl: out.append(expr)
    if b: out.append(jsq(b))
    return " + ".join(out) if out else "''"


def attr(s): return s.replace("&", "&amp;").replace('"', "&quot;").replace("<", "&lt;")


def plain(l, s):
    s = s if l != "fr" else fr_nb(s)
    return QM.sub(lambda m: m.group(2), s)


def build(l, T, dst):
    U = {k: plain(l, v) for k, v in T["ui"].items()}
    out = []
    for e in EN_DATA:
        z = T["L%03d" % e["n"]]
        out.append({"n": e["n"], "part": e["part"], "ref": e["ref"], "t": plain(l, z["t"]),
                    "cols": [plain(l, x) for x in z["cols"]], "rows": [[plain(l, v) for v in r] for r in z["rows"]],
                    "d": plain(l, z["d"])})
    t = EN_HTML
    EN_SHOW = """  art.innerHTML = '<div class="no" style="--c:' + c + '">List ' + e.n + ' · ' + PARTS[e.part][0].replace(/\\s+/g, ' ') + '</div>' +
    '<h2>' + esc(e.t) + '</h2><div class="ref">The Urantia Book ' + esc(e.ref) + '</div><div class="rule"></div>' +
    '<div class="tw"><table><thead><tr>' + head + '</tr></thead><tbody>' + body + '</tbody></table></div>' +
    '<p class="src">— The Urantia Book ' + esc(e.ref) + '</p>' +
    '<div class="desc"><h4>COMMENTARY</h4><p>' + esc(e.d) + '</p></div>' +
    '<div class="pn">' + (pv ? '<a href="#' + pv.n + '" data-go="' + pv.n + '">← Previous · List ' + pv.n + '<b>' + esc(pv.t) + '</b></a>' : '<span class="gap"></span>') +
    (nx ? '<a class="nx" href="#' + nx.n + '" data-go="' + nx.n + '">List ' + nx.n + ' · Next →<b>' + esc(nx.t) + '</b></a>' : '<span class="gap"></span>') + '</div>';"""
    NEW_SHOW = """  var bk = esc(%s), at = '/%s/book/#' + e.ref.split('-')[0];
  art.innerHTML = '<div class="no" style="--c:' + c + '">' + %s + ' · ' + PARTS[e.part][0].replace(/\\s+/g, ' ') + '</div>' +
    '<h2>' + esc(e.t) + '</h2><div class="ref">' + bk + ' <a href="' + at + '">' + esc(e.ref) + '</a></div><div class="rule"></div>' +
    '<div class="tw"><table><thead><tr>' + head + '</tr></thead><tbody>' + body + '</tbody></table></div>' +
    '<p class="src">— ' + bk + ' <a href="' + at + '">' + esc(e.ref) + '</a></p>' +
    '<div class="desc"><h4>' + esc(%s) + '</h4><p>' + esc(e.d) + '</p></div>' +
    '<div class="pn">' + (pv ? '<a href="#' + pv.n + '" data-go="' + pv.n + '">' + %s + '<b>' + esc(pv.t) + '</b></a>' : '<span class="gap"></span>') +
    (nx ? '<a class="nx" href="#' + nx.n + '" data-go="' + nx.n + '">' + %s + '<b>' + esc(nx.t) + '</b></a>' : '<span class="gap"></span>') + '</div>';""" % (
        jsq(U["book"]), l, fmt(U["list_no"], "e.n"), jsq(U["commentary"]), fmt(U["prev"], "pv.n"), fmt(U["next"], "nx.n"))
    R = [
        ('<html lang="en">', '<html lang="%s">' % HTML_LANG[l]),
        ("<title>376 Key Lists in The Urantia Book</title>", "<title>%s</title>" % attr(U["title"])),
        ('content="The 376 numbered lists found in the text of The Urantia Book, arranged as tables with commentary. Choose a list on the left to view it."',
         'content="%s"' % attr(U["meta_desc"])),
        ("article h2{margin:6px 0 4px;font-size:24px;line-height:1.45;color:var(--navy);word-break:keep-all}",
         "article h2{margin:6px 0 4px;font-size:24px;line-height:1.45;color:var(--navy);hyphens:auto}"),
        ("td{padding:9px 12px;border-top:1px solid var(--line);vertical-align:top;word-break:keep-all}",
         "td{padding:9px 12px;border-top:1px solid var(--line);vertical-align:top;hyphens:auto}"),
        (".ref{font-size:13px;color:var(--dim)}",
         ".ref{font-size:13px;color:var(--dim)}\n.ref a,.src a{color:var(--navy);border-bottom:1px dotted var(--gold)}.ref a:hover,.src a:hover{color:var(--gold)}"),
        ('<button id="burger">☰ Lists</button>', '<button id="burger">%s</button>' % attr(U["burger"])),
        ("<h1>376 Key Lists in The Urantia Book</h1>", "<h1>%s</h1>" % attr(U["h1"])),
        ('<span class="sub">Numbered lists from the text, as tables with commentary — choose a list on the left</span>',
         '<span class="sub">%s</span>' % attr(U["sub"])),
        ('placeholder="Search by number, title, or content (e.g. seven, Adjuster)"', 'placeholder="%s"' % attr(U["placeholder"])),
        ('<p class="msg">Loading…</p>', '<p class="msg">%s</p>' % attr(U["loading"])),
        ("// 영어판: 목록 376개(data.json, 영어 원문 표 + 영어 해설)",
         "// %s: data.json built by urantiaamerica tools/lists/build_lists_am.py" % l),
        ("'Part I  The Central and Superuniverses'", jsq(U["part1"])),
        ("'Part II  The Local Universe'", jsq(U["part2"])),
        ("'Part III  The History of Urantia'", jsq(U["part3"])),
        ("'Part IV  The Life and Teachings of Jesus'", jsq(U["part4"])),
        ("cnt.textContent = D.length + ' lists';\n}", "cnt.textContent = %s;\n}" % fmt(U["count_all"], "D.length")),
        (EN_SHOW, NEW_SHOW),
        # 악센트를 무시하고 찾기 (corazon → corazón)
        ("function esc(s) {", "function fold(s) { return String(s).normalize('NFD').replace(/[\\u0300-\\u036f]/g, '').toLowerCase(); }\nfunction esc(s) {"),
        ("var v = q.value.trim().toLowerCase(), shown = 0;", "var v = fold(q.value.trim()), shown = 0;"),
        ("(e.t + ' ' + e.rows.join(' ') + ' ' + e.ref).toLowerCase().indexOf(v) > -1", "fold(e.t + ' ' + e.rows.join(' ') + ' ' + e.ref).indexOf(v) > -1"),
        ("cnt.textContent = v ? shown + ' lists found' : D.length + ' lists';",
         "cnt.textContent = v ? %s : %s;" % (fmt(U["count_found"], "shown"), fmt(U["count_all"], "D.length"))),
        ("art.innerHTML = '<p class=\"msg\">The lists could not be loaded. Please try again in a moment.</p>';",
         "art.innerHTML = '<p class=\"msg\">' + esc(%s) + '</p>';" % jsq(U["error"])),
    ]
    for a, b in R:
        if t.count(a) != 1: raise SystemExit("English page changed? not found exactly once: " + a[:90])
        t = t.replace(a, b)
    assert '<script src="/home-button.js"' in t
    left = [s for s in ("The Urantia Book", "COMMENTARY", "Previous", "Next →", " lists", "Loading") if s in t]
    assert len(out) == 376 and [e["n"] for e in out] == list(range(1, 377))
    for e, z in zip(out, EN_DATA):
        assert len(e["rows"]) == len(z["rows"]) and len(e["cols"]) == len(z["cols"])
    os.makedirs(dst, exist_ok=True)
    dj = json.dumps(out, ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(dst, "data.json"), "w", encoding="utf-8").write(dj)
    open(os.path.join(dst, "index.html"), "w", encoding="utf-8").write(t)
    print("  written", dst, "| lists:", len(out), "| rows:", sum(len(e["rows"]) for e in out),
          "| English UI left:", left or "none", "| Hangul:", bool(HANGUL.search(t + dj)), "| markers:", "⟦" in dj)


bad = False
for l in LANGS:
    T, dup = load(l)
    print(f"[{l}] units {len(T)}/{len(SRC)}")
    err, same, qn, vb = check(l, T, dup)
    print("  quotations checked %d, bad %d" % (qn, len(err["quote_bad"])))
    if vb[0]: print("  verbatim cells: %d/%d official wording (%.0f%%)" % (vb[1], vb[0], 100 * vb[1] / vb[0]))
    if "--vb" in sys.argv:
        for x in vb[2]: print("    vb?", *x)
    for name, lst in err.items():
        if lst: print("  FAIL %-11s %d  %s" % (name, len(lst), lst if KEYS else lst[:8]))
    if same: print("  warn: cells identical to English in %d units: %s" % (len(set(same)), sorted(set(same))[:12]))
    failed = any(err.values())
    if KEYS is not None:
        print("  (--keys: partial check only, nothing written)"); bad = bad or failed; continue
    if PREVIEW and not err["missing"] and not err["struct"]:
        build(l, T, os.path.join(H, "preview", l))
    if failed:
        print(f"  CHECKS FAILED — site/{l}/lists/ not written."); bad = True; continue
    build(l, T, os.path.join(SITE, l, "lists"))
sys.exit(1 if bad else 0)
