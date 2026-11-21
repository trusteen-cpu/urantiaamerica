# -*- coding: utf-8 -*-
# 읽기 쉬운 해설판 (Easy-Reading Commentary Edition) 스페인어·프랑스어·포르투갈어판 → site/<l>/easy/
#   극동판 tools/zh/easy/build_easy_zh.py 를 옮긴 것. 극동판 영어 도구(tools/easy_en/apply.py · to_html.py · make_reader.py)의
#   함수·틀만 빌려 쓰고 고치지 않는다. 영어 docx(극동판 site/en/easy/files)의 문단을 번역문으로 바꿔 끼워 <l> docx 를 만들고,
#   그 docx 에서 웹 조각 c/NNN.html + toc.json, 그리고 읽기 화면 index.html 을 만든다.
#   원고: src/cNN.json (영어 단위) + <l>/cNN.json (번역, 같은 키) + fixed_<l>.json (자동 제목) + auto_<l>.json (자동 인용)
#   번역문의 빈 인용 표시 ⟦Q 9:3.5⟧⟦/Q⟧ 는 auto_<l>.json 에서 채운다(같은 절 번호의 자동 인용을 영어 순서대로).
#   검사: 키 누락·남는 키·한글·** 짝·⟦Q⟧ 표시(같은 절 번호)·인용(tools/data/<l>.json 원문 그대로, 공백 무시)·절 번호·자리표시,
#         영어 잔재는 경고. 하나라도 어긋나면 쪽을 만들지 않는다.
#   python build_easy_am.py es [fr pt]            검사 + 통과 시 site/<l>/easy/ 빌드
#   python build_easy_am.py es --chunk c03        그 묶음만 검사 (쓰지 않음)
#   python build_easy_am.py es --draft            빠진 단위는 영어로(자동 인용은 공식 번역으로) 채워 _draft_<l>/ 에 미리보기
#   PDF(선택, Microsoft Word 필요): 빌드 뒤 powershell -File to_pdf_am.ps1 es [-Draft]  → 이 빌더를 다시 돌리면 PDF 단추가 생긴다.
#        PDF 가 없는 편은 화면에 Word 단추만 나온다.
import ast, glob, html, json, os, re, sys, zipfile
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
EASY_EN = os.path.join(FE, "tools", "easy_en")
EN_FILES = os.path.join(FE, "site", "en", "easy", "files")
args = sys.argv[1:]
DRAFT = "--draft" in args
CHUNK = args[args.index("--chunk") + 1] if "--chunk" in args else None
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]

sys.path.insert(0, EASY_EN)
from apply import put, out_name      # noqa: E402  apply.py 는 __main__ 가드가 있어 import 해도 파일을 쓰지 않는다
import common                        # noqa: E402
from common import P_RE, T_RE        # noqa: E402


def _defs(path, names):
    tree = ast.parse(open(path, encoding="utf-8").read())
    keep = [n for n in tree.body if (isinstance(n, ast.FunctionDef) and n.name in names) or
            (isinstance(n, ast.Assign) and any(getattr(t, "id", "") in names for t in n.targets))]
    return ast.Module(body=keep, type_ignores=[])


TH = {k: getattr(common, k) for k in dir(common) if not k.startswith("__")}
TH["html"] = html
exec(compile(_defs(os.path.join(EASY_EN, "to_html.py"), {"BLOCK", "a", "runs_html", "para", "load_styles", "table"}), "to_html.py", "exec"), TH)
for n in ast.parse(open(os.path.join(EASY_EN, "make_reader.py"), encoding="utf-8").read()).body:
    if isinstance(n, ast.Assign) and getattr(n.targets[0], "id", "") == "TPL": TPL = ast.literal_eval(n.value)

CHUNKS = [c["id"] for c in json.load(open(os.path.join(H, "src", "chunks.json"), encoding="utf-8"))]
EN, CH = {}, {}
for c in CHUNKS:
    d = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
    EN.update(d); CH.update({k: c for k in d})
HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their)\b")
QM = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧", re.S)
REF = re.compile(r"\d+:\d+\.\d+(?:\s*[-–]\s*\d+(?::\d+)?\.\d+|\s*[-–]\s*\d+)?")
nows = lambda s: re.sub(r"\s+", "", s)
clean = lambda s: re.sub(r"⟦/?Q[^⟧]*⟧", "", s)
BOOKNAME = {"es": "El libro de Urantia", "fr": "Le Livre d’Urantia", "pt": "O Livro de Urântia"}
LANGTAG = {"es": "es-ES", "fr": "fr-FR", "pt": "pt-BR"}
SHORT = {"es": r"^Documento (\d+):\s*", "fr": r"^Fascicule (\d+)\s*:\s*", "pt": r"^Documento (\d+):\s*"}
HEAD = {"es": "Documento {n}  {t}", "fr": "Fascicule {n}  {t}", "pt": "Documento {n}  {t}"}


def fr_nb(s):
    """프랑스어 문장부호 앞뒤 띄움을 줄바꿈 없는 공백으로 — ⟦Q⟧ 인용 안은 건드리지 않는다"""
    def f(t):
        t = re.sub(r" ([;:!?»])", "\u00a0\\1", t)
        return t.replace("« ", "«\u00a0")
    parts = re.split(r"(⟦Q [^⟧]+⟧.*?⟦/Q⟧)", s, flags=re.S)
    return "".join(p if p.startswith("⟦Q ") else f(p) for p in parts)


def load(l):
    T, bad = {}, []
    for c in CHUNKS:
        p = os.path.join(H, l, c + ".json")
        if os.path.exists(p):
            try: T.update(json.load(open(p, encoding="utf-8")))
            except Exception as e: bad.append(f"JSON error {l}/{c}.json: {e}")
        elif not CHUNK and not DRAFT: print(f"  [missing file] {l}/{c}.json")
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    fixed = json.load(open(os.path.join(H, f"fixed_{l}.json"), encoding="utf-8"))
    BOOK = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
    return T, auto, fixed, BOOK, bad


def fill(v, lst):
    """빈 ⟦Q c⟧⟦/Q⟧ 를 자동 인용으로 채운다. 못 채운 절 번호 목록도 돌려준다."""
    used, miss = [False] * len(lst), []
    def rep(m):
        c, q = m.group(1), m.group(2)
        if q.strip(): return m.group(0)
        for i, (cc, r) in enumerate(lst):
            if not used[i] and cc == c and r:
                used[i] = True; return f"⟦Q {c}⟧{r}⟦/Q⟧"
        miss.append(c); return m.group(0)
    return QM.sub(rep, v), miss


def english_fill(k, lst):
    """--draft: 번역이 없는 단위 = 영어, 자동 인용만 공식 번역으로"""
    it = iter(lst)
    return QM.sub(lambda m: (lambda x: f"⟦Q {m.group(1)}⟧{x[1]}⟦/Q⟧" if x and x[1] else m.group(0))(next(it, None)), EN[k])


def check(l, T, auto, BOOK, bad):
    def cit_text(cit):
        m = re.fullmatch(r"(\d+):(\d+)\.(\d+)", cit)
        return BOOK.get(cit) if m else None
    def quote_ok(c, q):
        t = cit_text(c)
        if not t: return False, "citation not in book"
        hay = nows(t)
        for p in re.split(r"…|\.\.\.", q.replace("**", "")):
            p = nows(p).strip("“”\"'‘’«»")
            if p and p not in hay: return False, p[:50]
        return True, ""
    errs, warns, badq, nq = list(bad), [], [], 0
    F = {}
    for k, ev in EN.items():
        if CHUNK and CH[k] != CHUNK: continue
        nq += len(QM.findall(ev))
        if k not in T: errs.append(f"missing: {k}"); continue
        tv = T[k]
        if not isinstance(tv, str): errs.append(f"not a string: {k}"); continue
        tv, miss = fill(tv, auto.get(k, []))
        F[k] = tv
        for c in miss: errs.append(f"empty marker ⟦Q {c}⟧⟦/Q⟧ but no automatic quotation for it (see work/todo_{l}_*.json): {k}")
        if HANGUL.search(tv): errs.append(f"hangul: {k}")
        if tv.count("**") % 2: errs.append(f"** not balanced: {k}")
        if tv.count("⟦") != tv.count("⟧") or len(QM.findall(tv)) * 2 != tv.count("⟦"): errs.append(f"broken marker: {k}")
        a = sorted(c for c, _ in QM.findall(ev)); b = sorted(c for c, _ in QM.findall(tv))
        if a != b: errs.append(f"quotation markers changed {a} → {b}: {k}")
        for c, q in QM.findall(tv):
            if not q.strip(): continue
            ok, why = quote_ok(c, q)
            if not ok: badq.append(f"{k} [{c}] {why}")
        ra = sorted(nows(r).replace("–", "-") for r in REF.findall(QM.sub("", ev)))
        rb = sorted(nows(r).replace("–", "-") for r in REF.findall(QM.sub("", tv)))
        if ra != rb: errs.append(f"references changed {ra} → {rb}: {k}")
        if k.startswith("ui."):
            continue
        plain = re.sub(r"\*\*|⟦Q[^⟧]*⟧.*?⟦/Q⟧|“[^”]*”|\"[^\"]*\"|\([^)]*\)", "", tv)
        hits = ENGW.findall(plain)
        if len(ev.split()) > 3 and nows(clean(tv)) == nows(clean(ev)): warns.append(f"untranslated? {k}")
        elif len(hits) >= 2: warns.append(f"English words {hits[:4]}: {k}")
    for k in T:
        if k not in EN: errs.append(f"extra key: {k}")
    scope = f" chunk {CHUNK}" if CHUNK else ""
    tot = sum(1 for k in EN if not CHUNK or CH[k] == CHUNK)
    print(f"[{l}{scope}] translated: {sum(1 for k in EN if k in T and (not CHUNK or CH[k] == CHUNK))}/{tot} · "
          f"quotation markers: {nq} · bad: {len(badq)} · errors {len(errs)} · warnings {len(warns)}")
    for e in errs[:40]: print("  ERR", e)
    if len(errs) > 40: print(f"  … {len(errs) - 40} more errors")
    for b_ in badq[:40]: print("  BADQ", b_)
    if len(badq) > 40: print(f"  … {len(badq) - 40} more bad quotations")
    for w in warns[:30]: print("  WARN", w)
    if len(warns) > 30: print(f"  … {len(warns) - 30} more warnings")
    return bool(errs or badq), F


# ---------------- 만들기 ----------------
def lang_docx(x, l):
    """영어 docx 의 언어 표시를 바꾸고, 한글 이름으로 남은 eastAsia 글꼴은 ascii 글꼴로"""
    x = re.sub(r'(<w:lang [^>]*)w:val="[^"]*"', r'\1w:val="' + LANGTAG[l] + '"', x)
    def f(m):
        s = m.group(0); asc = re.search(r'w:ascii="([^"]*)"', s)
        return re.sub(r'w:eastAsia="([^"]*)"', lambda n: 'w:eastAsia="' + (asc.group(1) if asc else "Georgia") + '"'
                      if HANGUL.search(n.group(1)) else n.group(0), s)
    return re.sub(r"<w:rFonts [^>]*/>", f, x)


def header_title(l, no, fixed_title):
    if no == 0: return BOOKNAME[l] + "  |  " + fixed_title
    t = re.sub(r"^\D+\d+\s*:\s*", "", fixed_title)
    return BOOKNAME[l] + "  |  " + HEAD[l].format(n=no, t=t)


def build_docx(l, no, text, out):
    zin = zipfile.ZipFile(os.path.join(EN_FILES, out_name(no) + ".docx"))
    dst = os.path.join(out, "files", out_name(no) + ".docx")
    zout = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED)
    ht = header_title(l, no, text[f"{no:03d}:0"])
    for it in zin.infolist():
        data = zin.read(it.filename)
        if it.filename == "word/document.xml":
            x = data.decode("utf-8"); k = [-1]
            def sub(m):
                k[0] += 1; key = f"{no:03d}:{k[0]}"
                return put(m.group(0), text[key]) if key in text else m.group(0)
            data = lang_docx(P_RE.sub(sub, x), l).encode("utf-8")
        elif re.match(r"word/(header\d*|footer\d*|styles|numbering|fontTable)\.xml", it.filename):
            x = data.decode("utf-8")
            if it.filename.startswith("word/header"):
                x = P_RE.sub(lambda m: put(m.group(0), ht) if "The Urantia Book" in "".join(T_RE.findall(m.group(0))) else m.group(0), x)
            data = lang_docx(x, l).encode("utf-8")
        elif it.filename == "docProps/core.xml":
            x = data.decode("utf-8")
            data = re.sub(r"<dc:title>[^<]*</dc:title>", "<dc:title>" + html.escape(ht) + "</dc:title>", x).encode("utf-8")
        zout.writestr(it, data)
    zout.close(); return dst


LINK = re.compile(r"(?<![0-9A-Za-z:.#])(\d{1,3}:\d{1,2}\.\d{1,3})((?:\s*[-–]\s*\d+(?::\d+)?(?:\.\d+)?)?)")


def to_html(l, no, path, out):
    z = zipfile.ZipFile(path); TH["STYLES"] = TH["load_styles"](z); TH["FIRST"] = [True]
    x = z.read("word/document.xml").decode("utf-8"); x = x[x.index("<w:body>"):]
    parts = [TH["table"](b) if b.startswith("<w:tbl") else TH["para"](b) for b in TH["BLOCK"].findall(x)]
    h = "\n".join(p for p in parts if p)
    k = [0]
    def hid(m): k[0] += 1; return '<h3 id="h' + str(k[0]) + '"'
    h = re.sub(r"<h3(?=[ >])", hid, h)
    h = re.sub(r"(<[^>]+>)|([^<]+)", lambda m: m.group(1) or LINK.sub(
        lambda r: f'<a class="ref" href="/{l}/book/#' + r.group(1) + '" target="_blank">' + r.group(1) + r.group(2) + "</a>", m.group(2)), h)
    title = re.sub("<[^>]+>", "", re.search(r"<h1[^>]*>(.*?)</h1>", h).group(1))
    secs = [[m.group(1), html.unescape(re.sub("<[^>]+>", "", m.group(2)))] for m in re.finditer(r'<h3 id="(h\d+)"[^>]*>(.*?)</h3>', h)]
    open(os.path.join(out, "c", f"{no:03d}.html"), "w", encoding="utf-8").write(h)
    name = out_name(no)
    return [html.unescape(title), secs, name, 1 if os.path.exists(os.path.join(out, "files", name + ".pdf")) else 0]


def reader(l, ui, out):
    tpl = TPL
    old = """document.getElementById('dl').innerHTML = T.dl + ' <a href="' + f + '.pdf" target="_blank" rel="noopener">' + T.pdf + '</a><a href="' + f + '.docx">' + T.word + '</a>';"""
    new = """document.getElementById('dl').innerHTML = T.dl + ' ' + (TOC[n][3] ? '<a href="' + f + '.pdf" target="_blank" rel="noopener">' + T.pdf + '</a>' : '') + '<a href="' + f + '.docx">' + T.word + '</a>';"""
    assert old in tpl, "make_reader.py download line changed"
    tpl = tpl.replace(old, new)
    e = lambda s: html.escape(s, quote=True)
    c = dict(lang=l, title=e(ui["ui.title"]), book=e(ui["ui.book"]), files="files/", list=e(ui["ui.list"]), search=e(ui["ui.search"]),
             loading=e(ui["ui.loading"]), font='Georgia,"Times New Roman",serif', ui='"Segoe UI",system-ui,sans-serif')
    c["parts"] = json.dumps([ui["ui.part%d" % i] for i in range(5)], ensure_ascii=False)
    c["shortjs"] = json.dumps(SHORT[l])
    c["tjs"] = json.dumps({x: ui["ui." + x] for x in ("prev", "next", "pdf", "word", "loading", "title", "dl")}, ensure_ascii=False)
    h = tpl % c
    h = h.replace("#doc p{margin:6px 0 10px;text-align:justify}", "#doc p{margin:6px 0 10px;text-align:justify;hyphens:auto;overflow-wrap:break-word}", 1)
    if DRAFT:
        h = h.replace('<div id="top">', '<div style="position:fixed;bottom:0;left:0;right:0;z-index:99;background:#c00;color:#fff;text-align:center;'
                      'padding:3px;font:12px sans-serif">DRAFT — not for publication</div>\n<div id="top">', 1)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(h)


def build(l, F, auto, fixed):
    out = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "easy")
    text = dict(fixed)
    for k in EN:
        v = F[k] if k in F else english_fill(k, auto.get(k, []))
        text[k] = v
    if l == "fr": text = {k: fr_nb(v) for k, v in text.items()}
    text = {k: clean(v) for k, v in text.items()}
    ui = {k: text[k] for k in EN if k.startswith("ui.")}
    for d in ("files", "c"): os.makedirs(os.path.join(out, d), exist_ok=True)
    toc = []
    for no in range(197):
        if not os.path.exists(os.path.join(EN_FILES, out_name(no) + ".docx")): toc.append(None); continue
        toc.append(to_html(l, no, build_docx(l, no, text, out), out))
    json.dump(toc, open(os.path.join(out, "c", "toc.json"), "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
    reader(l, ui, out)
    left = [n for n in range(197) if toc[n] and HANGUL.search(open(os.path.join(out, "c", f"{n:03d}.html"), encoding="utf-8").read())]
    if left and not DRAFT: raise SystemExit(f"CHECK FAILED: hangul in output {left[:20]}")
    print(f"[{l}{' DRAFT' if DRAFT else ''}] papers: {sum(1 for t in toc if t)} · PDF: {sum(1 for t in toc if t and t[3])} "
          f"· pages with hangul: {left[:10]} → {out}")


fail_any = False
for l in LANGS:
    T, auto, fixed, BOOK, bad = load(l)
    failed, F = check(l, T, auto, BOOK, bad)
    fail_any |= failed
    if CHUNK: continue
    if failed and not DRAFT:
        print(f"CHECK FAILED [{l}] — site/{l}/easy/ not written (use --draft for a preview)"); continue
    build(l, F, auto, fixed)
if fail_any: print("errors 1"); sys.exit(1)
print("errors 0")
