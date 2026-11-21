# -*- coding: utf-8 -*-
# 「The Urantia Book for Young Readers」(청소년판) 스페인어·프랑스어·포르투갈어판 → site/<l>/youth/
#   극동판 tools/zh/youth/build_youth_zh.py 를 옮긴 것. 색·CSS·도움 함수(col, tint, CSS, clean)는
#   극동판 tools/build_youth_en.py 에서 exec 로 빌려 쓴다(그 파일은 고치지 않고, 그 main() 은 돌리지 않음).
#   원고: src/cNN.json (영어 단위) + src/_structure.json (편마다 [키, 종류])
#        + <l>/cNN.json (번역: 같은 키, 같은 묶음)
#        + auto_<l>.json (prep.py 가 자동으로 잘라 둔 인용 {"키#n": "…"}) — 번역에서 ⟦Q 절⟧⟦/Q⟧ 처럼 안을 비워 두면 이것으로 채운다.
#   편 제목: tools/data/<l>_titles.json (공식 번역 제목; 번역 단위가 아님).
#   검사: 키 누락·남는 키·빈 값·인용 표시(같은 절, 같은 순서)·소제목 번호·{n} 자리표시·한글·인용 글자 그대로(tools/data/<l>.json, 공백 무시)
#         + 영어 잔재(경고). 하나라도 어긋나면 site/<l>/youth/ 를 쓰지 않는다.
#   python build_youth_am.py es [fr pt]          검사 + 통과 시 빌드
#   python build_youth_am.py es --chunk c03      그 묶음만 검사 (쓰지 않음)
#   python build_youth_am.py es --draft          빠진 단위는 영어로 채워 _draft_es/ 에 미리보기 (검사 실패해도 씀)
import html, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
args = sys.argv[1:]
DRAFT = "--draft" in args
CHUNK = args[args.index("--chunk") + 1] if "--chunk" in args else None
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]

# ---- 영어판 빌더에서 색·CSS·함수만 빌려 옴
EN_BUILDER = os.path.join(FE, "tools", "build_youth_en.py")
_code = re.sub(r"\nmain\(\)\s*$", "\n", open(EN_BUILDER, encoding="utf-8").read())
assert not re.search(r"^main\(\)", _code, re.M), "English builder still calls main()"
ns = {"__file__": EN_BUILDER, "__name__": "youth_en_borrowed"}
exec(_code, ns)
col, tint, CSS0, clean = ns["col"], ns["tint"], ns["CSS"], ns["clean"]
esc = html.escape
CSS = CSS0 + ("\nsection.paper p{hyphens:auto;overflow-wrap:break-word}"
              "\na.q{color:inherit;text-decoration:none;border-bottom:1px dotted rgba(0,0,0,.35)}"
              "\na.q:hover{border-bottom-style:solid}\n")

ST = json.load(open(os.path.join(H, "src", "_structure.json"), encoding="utf-8"))
CHUNKS = sorted(ST["_chunks"])
EN, CH = {}, {}
for c in CHUNKS:
    d = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
    EN.update(d); CH.update({k: c for k in d})
KIND = {k: kd for n in ST if n.isdigit() for k, kd in ST[n]["items"]}
PAPERS = sorted(int(n) for n in ST if n.isdigit())

MARK = re.compile(r"⟦Q ([^⟧]+)⟧(.*?)⟦/Q⟧", re.S)
HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their|they|you|your)\b")
HNUM = re.compile(r"^\d+(?:,\s*\d+)*\.")
nows = lambda s: re.sub(r"\s+", "", s.replace("\u00a0", " "))
QCH = "«»“”\"‘’'"


def fr_nb(s):
    s = re.sub(r" ([;:!?»])", "\u00a0\\1", s)
    return s.replace("« ", "«\u00a0")


def fr_outside_quotes(s):
    """프랑스어 띄움을 인용 표시 밖에만 넣는다(인용 안은 공식 본문 그대로)."""
    out, pos = [], 0
    for m in MARK.finditer(s):
        out.append(fr_nb(s[pos:m.start()])); out.append(m.group(0)); pos = m.end()
    out.append(fr_nb(s[pos:]))
    return "".join(out)


def load(l):
    BOOK = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
    TIT = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}_titles.json"), encoding="utf-8"))
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    T, nofill = {}, []
    for c in CHUNKS:
        p = os.path.join(H, l, c + ".json")
        if os.path.exists(p): T.update(json.load(open(p, encoding="utf-8")))
        elif not CHUNK or CHUNK == c: print(f"  [missing file] {l}/{c}.json")
    for k, v in list(T.items()):
        if not isinstance(v, str): continue
        cnt = [-1]

        def fill(m):
            cnt[0] += 1
            if m.group(2).strip(): return m.group(0)
            a = auto.get(f"{k}#{cnt[0]}")
            if a is None: nofill.append(f"{k}#{cnt[0]}"); return m.group(0)
            return f"⟦Q {m.group(1)}⟧{a}⟦/Q⟧"
        T[k] = MARK.sub(fill, v)
    return BOOK, TIT, T, nofill


def quote_ok(BOOK, cit, text):
    if cit not in BOOK: return False, "citation not in book"
    hay = nows(BOOK[cit]); pos = 0
    pieces = [p for p in re.split(r"…|\.\.\.", text) if p.strip()]
    if not pieces: return False, "empty quotation"
    for p in pieces:
        p = nows(p).strip(QCH)
        k = hay.find(p, pos)
        if k < 0:
            p2 = p.rstrip(".,;:!?")            # 끝 문장부호 하나 차이는 허용
            k = hay.find(p2, pos) if p2 else -1
            if k < 0: return False, p[:50]
            p = p2
        pos = k + len(p)
    return True, ""


def check(l, BOOK, T, nofill):
    errs, warns, badq, nq = [], [], [], 0
    scope = [k for k in EN if not CHUNK or CH[k] == CHUNK]
    for k in scope:
        ev, tv = EN[k], T.get(k)
        if not isinstance(tv, str) or not tv.strip(): errs.append(f"missing: {k}"); continue
        if HANGUL.search(tv): errs.append(f"hangul: {k}")
        if [m.group(1) for m in MARK.finditer(ev)] != [m.group(1) for m in MARK.finditer(tv)]:
            errs.append(f"quotation markers differ from English: {k}")
        if tv.count("⟦") != tv.count("⟧") or len(MARK.findall(tv)) * 2 != tv.count("⟦"):
            errs.append(f"broken marker: {k}")
        for m in MARK.finditer(tv):
            nq += 1
            if not m.group(2).strip(): continue      # nofill 에서 보고
            ok, why = quote_ok(BOOK, m.group(1), m.group(2))
            if not ok: badq.append(f"{k} [{m.group(1)}] {why}")
        if KIND.get(k) == "h" and HNUM.match(ev):
            if not tv.startswith(HNUM.match(ev).group(0)): errs.append(f"heading number prefix changed: {k}")
        if k.startswith("ui."):
            ph = set(re.findall(r"\{\w+\}", ev))
            if ph - set(re.findall(r"\{\w+\}", tv)): errs.append(f"placeholder lost: {k}")
        plain = MARK.sub("", tv)
        hits = ENGW.findall(plain)
        if nows(tv) == nows(ev) and len(ev.split()) > 3: warns.append(f"untranslated? {k}")
        elif len(hits) >= 3: warns.append(f"English words {hits[:4]}: {k}")
    for k in nofill:
        if not CHUNK or CH.get(k.split("#")[0]) == CHUNK: errs.append(f"empty quotation with no auto cut (cut it by hand): {k}")
    for k in T:
        if k not in EN: errs.append(f"extra key: {k}")
        elif CHUNK and CH[k] != CHUNK: pass
    sc = f" chunk {CHUNK}" if CHUNK else ""
    done = sum(1 for k in scope if isinstance(T.get(k), str) and T[k].strip())
    print(f"[{l}{sc}] translated: {done}/{len(scope)} · quotations checked: {nq} · bad: {len(badq)} · errors {len(errs)} · warnings {len(warns)}")
    for e in errs[:40]: print("  ERR", e)
    if len(errs) > 40: print(f"  … {len(errs) - 40} more errors")
    for b in badq[:40]: print("  BADQ", b)
    if len(badq) > 40: print(f"  … {len(badq) - 40} more bad quotations")
    for w in warns[:30]: print("  WARN", w)
    if len(warns) > 30: print(f"  … {len(warns) - 30} more warnings")
    return bool(errs or badq)


def build(l, TIT, T):
    def V(k):
        v = T.get(k) if isinstance(T.get(k), str) and T[k].strip() else (EN[k] if DRAFT else T[k])
        return fr_outside_quotes(v) if l == "fr" else v

    def render(text):
        out, pos = [], 0
        for m in MARK.finditer(text):
            out.append(esc(clean(text[pos:m.start()])))
            out.append(f'<a class="q" href="/{l}/book/#{m.group(1)}">{esc(m.group(2))}</a>')
            pos = m.end()
        out.append(esc(clean(text[pos:])))
        return "".join(out)
    ui = lambda k: MARK.sub(lambda m: m.group(2), V("ui." + k))
    lab = lambda n: ui("paper").replace("{n}", str(n)) if n else ui("foreword")
    title_of = lambda n: TIT[str(n)]["title"]
    site_t = ui("site_title")
    colon = "\u00a0: " if l == "fr" else ": "
    HEAD = (f'<!DOCTYPE html>\n<html lang="{l}">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n<title>{title}</title>\n'
            '<meta property="og:title" content="{title}">\n'
            f'<meta property="og:description" content="{esc(ui("og_desc"))}">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500&family=Nunito:wght@400;600;700&display=swap" rel="stylesheet">\n'
            '<style>{css}</style>\n<script src="/home-button.js" data-pos="left" defer></script>\n</head>\n<body>\n')
    FOOT = f'<footer>{esc(ui("footer"))}</footer>\n</div>\n</body>\n</html>\n'
    back = esc(ui("back"))
    TOP = (f'<header class="top" style="padding:26px 0 22px"><div class="series">{esc(ui("series"))}</div>'
           f'<h1 style="font-size:30px;margin:6px 0 2px">{esc(ui("book"))}</h1><div class="range">'
           f'<a href="./" style="border-bottom:1px solid rgba(255,255,255,.5)">{back}</a></div></header>\n')

    def section(n):
        c, t = col(n), tint(n)
        out = [f'<section class="paper" id="p{n}">',
               f'  <div class="banner" style="background:{c}"><div class="n">{esc(lab(n).upper())}</div>'
               f'<div class="t">{esc(title_of(n))}</div></div>']
        for key, kind in ST[str(n)]["items"]:
            text = render(V(key))
            if kind == "h":
                m = re.match(r"^(\d+(?:,\s*\d+)*\.)\s*(.*)$", text)
                num, h = (m.group(1), m.group(2)) if m else ("", text)
                out.append(f'  <h3 class="sec" style="background:{t};border-left:7px solid {c}">'
                           f'<span class="num" style="color:{c}">{num}</span>{h}</h3>')
            else:
                out.append(f"  <p>{text}</p>")
        out += [f'  <div class="ornament" style="color:{c}">◆ ◇ ◆</div>',
                f'  <div style="text-align:center"><a class="up" href="./">{back}</a></div>', "</section>"]
        return "\n".join(out) + "\n"

    name = lambda n: f'{esc(lab(n))}{" " + esc(title_of(n)) if n else ""}'
    pages = {}
    for i, n in enumerate(PAPERS):
        prev = f'<a href="p{PAPERS[i-1]}.html">← {name(PAPERS[i-1])}</a>' if i else "<span></span>"
        nxt = f'<a href="p{PAPERS[i+1]}.html">{name(PAPERS[i+1])} →</a>' if i + 1 < len(PAPERS) else "<span></span>"
        title = f'{lab(n)}{colon + title_of(n) if n else ""} — {site_t}'
        pages[f"p{n}.html"] = (HEAD.format(title=esc(title), css=CSS) + TOP + '<div class="wrap">\n' + section(n)
                               + f'<nav class="pager">{prev}<a href="./">{esc(ui("contents"))}</a>{nxt}</nav>\n' + FOOT)
    cards = []
    for n in range(0, 197):
        c = col(n)
        if n in PAPERS:
            cards.append(f'    <a class="card" href="p{n}.html" style="border-left:6px solid {c}">'
                         f'<div class="n" style="color:{c}">{esc(lab(n).upper())}</div><div class="t">{esc(title_of(n))}</div></a>')
        else:
            cards.append(f'    <div class="card off" style="border-left:6px solid #ddd"><div class="n">{esc(lab(n).upper())}</div>'
                         f'<div class="soon">{esc(ui("soon"))}</div></div>')
    pages["index.html"] = (HEAD.format(title=esc(site_t), css=CSS)
                           + f'<header class="top">\n  <div class="series">{esc(ui("series"))}</div>\n  <h1>{esc(ui("book"))}</h1>\n'
                           + f'  <div class="range">{esc(ui("range"))}</div>\n</header>\n'
                           + f'<div class="wrap">\n<nav class="toc" id="toc">\n  <h2>{esc(ui("contents_h"))}</h2>\n'
                           + f'  <div class="stat">{esc(ui("stat"))}</div>\n'
                           + '  <div class="cards">\n' + "\n".join(cards) + "\n  </div>\n</nav>\n" + FOOT)
    left = [f for f, p in pages.items() if HANGUL.search(p) or "⟦" in p]
    if left and not DRAFT: raise SystemExit(f"CHECK FAILED: Hangul or markers left in output {left[:10]}")
    out = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "youth")
    os.makedirs(out, exist_ok=True)
    for f, p in pages.items():
        if DRAFT: p = p.replace("<body>\n", '<body>\n<div style="background:#c00;color:#fff;text-align:center;padding:4px;font:13px sans-serif">DRAFT — not for publication</div>\n', 1)
        open(os.path.join(out, f), "w", encoding="utf-8").write(p)
    nq = sum(len(MARK.findall(V(k))) for k in EN)
    print(f"[{l}{' DRAFT' if DRAFT else ''}] pages: {len(pages)} (index + {len(PAPERS)} papers), quotations: {nq} → {out}")


fail_any = False
for l in LANGS:
    BOOK, TIT, T, nofill = load(l)
    failed = check(l, BOOK, T, nofill)
    fail_any |= failed
    if CHUNK: continue
    if failed and not DRAFT:
        print(f"CHECK FAILED [{l}] — site/{l}/youth/ not written (use --draft for a preview)"); continue
    build(l, TIT, T)
if fail_any: print("errors 1"); sys.exit(1)
print("errors 0")
