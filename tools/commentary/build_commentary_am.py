# -*- coding: utf-8 -*-
# 역주 해설 (Paper-by-Paper Commentary, 머리말 + 196편) 스페인어·프랑스어·포르투갈어판 → site/<l>/commentary/
#   극동판 tools/zh/commentary/build_commentary_zh.py 를 옮긴 것. CSS·inline 은 영어 빌더
#   E:/OneDrive/유란시아 작업/uui-en/commentary/build_en.py 에서 빌려 쓴다(exec, 고치지 않음; 안 되면 극동판 site/en/commentary/p001.html 의 CSS).
#   원고: src/skeleton.json (쪽 구조) + src/cNN.json (영어 단위)
#        + <l>/cNN.json (번역: 블록 인용을 뺀 모든 단위, 같은 키 — work/src_cNN.json 과 같은 모양)
#        + 블록 인용: auto_<l>.json (자동, prep.py) 또는 <l>/quotes_cNN.json (손으로 자른 것, 이쪽이 우선)
#   검사: 키 누락·남는 키·구조(표 모양, foot ref, ⟦Q⟧ 표지, {자리표시}, **)·한글·인용(tools/data/<l>.json 원문 그대로, 공백만 무시)
#         ·영어 잔재(경고) — 하나라도 어긋나면 쪽을 만들지 않는다.
#   python build_commentary_am.py es [fr pt]          검사 + 통과 시 빌드
#   python build_commentary_am.py es --chunk c03      그 묶음만 검사 (쓰지 않음)
#   python build_commentary_am.py es --draft          빠진 단위는 영어로 채워 _draft_<l>/ 에 미리보기
import html, json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
EN_BUILDER = r"E:/OneDrive/유란시아 작업/uui-en/commentary/build_en.py"
args = sys.argv[1:]
DRAFT = "--draft" in args
CHUNK = args[args.index("--chunk") + 1] if "--chunk" in args else None
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]


# ---- 영어 빌더에서 CSS 빌리기 ----
def load_css():
    ns = {"__name__": "build_en_lib", "__file__": EN_BUILDER}
    try:
        exec(compile(open(EN_BUILDER, encoding="utf-8").read(), EN_BUILDER, "exec"), ns)
        return ns["CSS"]
    except Exception as e:
        print(f"note: English builder not usable here ({type(e).__name__}); CSS taken from Far East site/en/commentary/p001.html")
        t = open(os.path.join(FE, "site", "en", "commentary", "p001.html"), encoding="utf-8").read()
        return t[t.index("<style>") + 7:t.index("</style>")]


SK = json.load(open(os.path.join(H, "src", "skeleton.json"), encoding="utf-8"))
EN, CH = {}, {}
for c in SK["chunks"]:
    d = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
    EN.update(d); CH.update({k: c for k in d})
HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their)\b")
MARK = re.compile(r"⟦Q ([0-9]+:[0-9]+\.[0-9]+)⟧(.*?)⟦/Q⟧", re.S)
PH = re.compile(r"\{[a-z]+\}")
nows = lambda s: re.sub(r"\s+", "", s)
strip_marks = lambda s: MARK.sub(lambda m: m.group(2), s)
E = html.escape
isq = lambda v: isinstance(v, dict) and "q" in v


def strings(v):
    if isinstance(v, str): yield v
    elif isinstance(v, dict):
        for kk, x in v.items():
            if kk not in ("cit", "ref"): yield from strings(x)
    elif isinstance(v, list):
        for x in v: yield from strings(x)


def fr_nb(s):
    """프랑스어 산문: ; : ! ? » 앞과 « 뒤를 줄바꿈 없는 공백으로. ⟦Q⟧…⟦/Q⟧ 인용 안은 건드리지 않는다."""
    def f(x):
        x = re.sub(r" ([;:!?»])", "\u00a0\\1", x)
        return x.replace("« ", "«\u00a0")
    out, pos = [], 0
    for m in MARK.finditer(s):
        out.append(f(s[pos:m.start()])); out.append(m.group(0)); pos = m.end()
    out.append(f(s[pos:]))
    return "".join(out)


def load(l):
    BOOK = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
    TT = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}_titles.json"), encoding="utf-8"))
    # 공식 번역 data 는 121:8.12–14 번호가 영어와 돌아가 있다(번역 8.12 = 영어 8.14). prep.py 의 alias 와 같음.
    AL = {}
    if BOOK.get("121:8.12", "").lstrip().startswith("["):
        AL = {"121:8.12": "121:8.13", "121:8.13": "121:8.14", "121:8.14": "121:8.12"}
    T = {}
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    for c in SK["chunks"]:
        p = os.path.join(H, l, c + ".json")
        if os.path.exists(p): T.update(json.load(open(p, encoding="utf-8")))
        elif not CHUNK or CHUNK == c: print(f"  [missing file] {l}/{c}.json")
        hand = {}
        p = os.path.join(H, l, f"quotes_{c}.json")
        if os.path.exists(p): hand = json.load(open(p, encoding="utf-8"))
        for k in hand:
            if k not in EN or not isq(EN[k]): print(f"  [{l}/quotes_{c}.json] key is not a block quotation: {k}")
        S = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
        for k, v in S.items():
            if isq(v):
                q = hand.get(k, auto.get(k))
                if q is not None: T[k] = {"q": q, "cit": v["cit"]}
    return BOOK, TT, AL, T


def check(l, BOOK, AL, T):
    def quote_ok(text, cit):
        cit = AL.get(cit, cit)
        if cit not in BOOK: return False, "citation not in book"
        hay, pos = nows(BOOK[cit]), 0
        for piece in re.split(r"…|\.\.\.", text):
            piece = nows(piece).strip("“”\"'‘’«»")
            if not piece: continue
            i = hay.find(piece, pos)
            if i < 0: return False, piece[:50]
            pos = i + len(piece)
        return True, ""
    errs, warns, badq, nq = [], [], [], 0
    for k, ev in EN.items():
        if CHUNK and CH[k] != CHUNK: continue
        if k not in T: errs.append(f"missing: {k}"); continue
        tv = T[k]
        if type(tv) is not type(ev): errs.append(f"type differs: {k}"); continue
        if isinstance(ev, dict):
            if set(tv) != set(ev): errs.append(f"fields {sorted(tv)} ≠ {sorted(ev)}: {k}"); continue
            if isq(ev):
                nq += 1
                if not isinstance(tv["q"], str) or not tv["q"].strip(): errs.append(f"empty quotation: {k}"); continue
                ok, why = quote_ok(tv["q"], tv["cit"])
                if not ok: badq.append(f"{k} [{tv['cit']}] {why}")
                if HANGUL.search(tv["q"]): errs.append(f"hangul: {k}")
                continue
            if "ref" in ev and tv["ref"] != ev["ref"]: errs.append(f"foot ref changed: {k}")
            if "head" in ev:
                if not isinstance(tv["head"], list) or not isinstance(tv["rows"], list) or len(tv["head"]) != len(ev["head"]) \
                   or len(tv["rows"]) != len(ev["rows"]) \
                   or any(not isinstance(a, list) or len(a) != len(b) for a, b in zip(tv["rows"], ev["rows"])):
                    errs.append(f"table shape differs: {k}"); continue
        ens, tss = list(strings(ev)), list(strings(tv))
        if len(ens) != len(tss): errs.append(f"structure differs: {k}"); continue
        for es_, ts in zip(ens, tss):
            if not isinstance(ts, str): errs.append(f"not a string: {k}"); break
            if es_.strip() and not ts.strip(): errs.append(f"empty text: {k}")
            if HANGUL.search(ts): errs.append(f"hangul: {k}")
            if [m.group(1) for m in MARK.finditer(es_)] != [m.group(1) for m in MARK.finditer(ts)]:
                errs.append(f"inline quotation markers changed: {k}")
            rest = MARK.sub("", ts)
            if "⟦" in rest or "⟧" in rest: errs.append(f"broken marker: {k}")
            for m in MARK.finditer(ts):
                nq += 1
                ok, why = quote_ok(m.group(2), m.group(1))
                if not ok: badq.append(f"{k} inline [{m.group(1)}] {why}")
            if sorted(PH.findall(es_)) != sorted(PH.findall(ts)): errs.append(f"placeholder {{…}} changed: {k}")
            if ts.count("**") % 2: errs.append(f"unbalanced **: {k}")
            plain = re.sub(r"\*\*[^*]+\*\*|“[^”]*”|\"[^\"]*\"|⟦Q[^⟧]*⟧.*?⟦/Q⟧|\([^)]*\)", "", ts)
            hits = ENGW.findall(plain)
            if es_.strip() and nows(ts) == nows(es_) and len(es_.split()) > 3: warns.append(f"untranslated? {k}")
            elif len(hits) >= 2: warns.append(f"English words {hits[:4]}: {k}")
    for k in T:
        if k not in EN: errs.append(f"extra key: {k}")
    scope = f" chunk {CHUNK}" if CHUNK else ""
    print(f"[{l}{scope}] translated: {sum(1 for k in EN if k in T and (not CHUNK or CH[k] == CHUNK))}/"
          f"{sum(1 for k in EN if not CHUNK or CH[k] == CHUNK)} · quotations checked: {nq} · bad: {len(badq)} · errors {len(errs)} · warnings {len(warns)}")
    for e in errs[:40]: print("  ERR", e)
    if len(errs) > 40: print(f"  … {len(errs) - 40} more errors")
    for b in badq[:40]: print("  BADQ", b)
    if len(badq) > 40: print(f"  … {len(badq) - 40} more bad quotations")
    for w in warns[:30]: print("  WARN", w)
    if len(warns) > 30: print(f"  … {len(warns) - 30} more warnings")
    return bool(errs or badq)


def build(l, TT, AL, T):
    CSS = load_css()
    V0 = (lambda k: T.get(k, EN[k])) if DRAFT else (lambda k: T[k])
    if l == "fr":
        def V(k):
            v = V0(k)
            if isinstance(v, str): return fr_nb(v)
            if isinstance(v, dict) and "head" in v:
                return {"head": [fr_nb(x) for x in v["head"]], "rows": [[fr_nb(x) for x in r] for r in v["rows"]]}
            if isinstance(v, dict) and "text" in v: return {"text": fr_nb(v["text"]), "ref": v["ref"]}
            return v
    else:
        V = V0

    def Tu(k, **kw):
        s = strip_marks(V(k))
        for a, b in kw.items(): s = s.replace("{" + a + "}", str(b))
        return s

    def inline(s): return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", E(strip_marks(s)))
    def lk(r): return f'<a class="rl" href="/{l}/book/#{AL.get(r, r)}" target="_blank" rel="noopener">{r}</a>'
    def refs(rs): return ' <span class="r">(' + ", ".join(lk(r) for r in rs) + ")</span>" if rs else ""
    def title(n): return TT[str(n)]["title"]
    def label(n): return Tu("ui.label_foreword") if n == 0 else Tu("ui.label_paper", n=n)

    out = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "commentary")
    os.makedirs(out, exist_ok=True)
    pages, nbq = [], 0
    for n in range(197):
        P = f"p{n:03d}"; S = SK["papers"][P]; body, toc = [], []
        for i, blocks in enumerate(S["sections"]):
            sid = f"s{i}"; hd = V(f"{P}.s{i}.h")
            toc.append(f'<li><a href="#{sid}">{inline(hd)}</a></li>')
            h = [f'<section id="{sid}"><h2>{inline(hd)}</h2>']
            for j, b in enumerate(blocks):
                u = V(f"{P}.s{i}.b{j}")
                if b["k"] == "q":
                    nbq += 1
                    h.append(f'<blockquote>{E(u["q"])} <span class="r">({lk(b["r"])})</span></blockquote>')
                elif b["k"] == "t":
                    head = "<tr>" + "".join(f"<th>{inline(x)}</th>" for x in u["head"]) + "</tr>"
                    rows = "".join("<tr>" + "".join(f"<td>{inline(c)}</td>" for c in row) + "</tr>" for row in u["rows"])
                    cap = f'<caption>{E(Tu("ui.source"))} {lk(b["r"])}</caption>' if b["r"] else ""
                    h.append(f'<div class="tw"><table>{cap}{head}{rows}</table></div>')
                else:
                    h.append(f"<p>{inline(u)}{refs(b['r'])}</p>")
            h.append("</section>"); body.append("".join(h))
        prev = f'<a class="nb" href="p{n-1:03d}.html">{E(Tu("ui.prev"))}</a>' if n > 0 else ""
        nxt = f'<a class="nb" href="p{n+1:03d}.html">{E(Tu("ui.next"))}</a>' if n < 196 else ""
        idx = f'<a class="nb" href="./">{E(Tu("ui.index"))}</a>'
        foot = ""
        if f"{P}.foot" in EN:
            f = V(f"{P}.foot"); foot = E(strip_marks(f["text"])) + (f" ({lk(f['ref'])})" if f["ref"] else "") + " · "
        lab, tit, lead = label(n), title(n), strip_marks(V(f"{P}.lead"))
        page = f'''<!DOCTYPE html><html lang="{l}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{E(Tu("ui.page_title", label=lab, title=tit))}</title><meta property="og:title" content="{E(Tu("ui.page_og_title", label=lab, title=tit))}">
<meta property="og:description" content="{E(lead)}"><style>{CSS}</style><script src="/home-button.js" defer></script></head><body>
<header><span class="badge">{E(Tu("ui.badge_paper", label=lab))}</span><h1>{E(tit)}</h1><p>{E(lead)}</p></header>
<div class="wrap"><nav><b>{E(Tu("ui.contents"))}</b><ol>{"".join(toc)}</ol><a class="all" href="./">{E(Tu("ui.all_papers"))}</a></nav>
<main><div class="bar">{prev}{idx}{nxt}<button onclick="window.print()">{E(Tu("ui.print"))}</button></div>{"".join(body)}
<div class="bar bot">{prev}{idx}{nxt}</div>
<div class="foot">{foot}{E(Tu("ui.foot"))}</div></main></div>
</body></html>'''
        pages.append((P + ".html", page))
    parts = [("ui.part0", 0, 0), ("ui.part1", 1, 31), ("ui.part2", 32, 56), ("ui.part3", 57, 119), ("ui.part4", 120, 196)]
    h = []
    for key, a, b in parts:
        h.append(f"<h2>{E(Tu(key))}</h2><ol class='plist'>")
        for n in range(a, b + 1):
            lab = Tu("ui.label_short_foreword") if n == 0 else str(n)
            h.append(f'<li><a href="p{n:03d}.html"><b>{E(lab)}</b>{E(title(n))}</a></li>')
        h.append("</ol>")
    idx = f'''<!DOCTYPE html><html lang="{l}"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{E(Tu("ui.index_title"))}</title><meta property="og:title" content="{E(Tu("ui.index_og_title"))}"><meta property="og:description" content="{E(Tu("ui.index_og_desc"))}">
<style>{CSS}
.plist{{list-style:none;padding:0;margin:0 0 10px;columns:2;column-gap:24px}}.plist li{{break-inside:avoid}}
.plist a,.plist span{{display:flex;gap:10px;padding:6px 8px;border-radius:7px;color:var(--ink);text-decoration:none;font-size:15px}}
.plist a:hover{{background:#efe6d4}}.plist b{{flex:0 0 40px;color:var(--gold)}}
@media(max-width:700px){{.plist{{columns:1}}}}</style><script src="/home-button.js" defer></script></head><body>
<header><span class="badge">{E(Tu("ui.index_badge"))}</span><h1>{E(Tu("ui.index_h1"))}</h1><p>{E(Tu("ui.index_sub", ready=197))}</p></header>
<div class="wrap"><main style="max-width:980px;margin:0 auto"><div class="bar"><a class="nb" href="/{l}/">{E(Tu("ui.home"))}</a></div>{"".join(h)}</main></div>
</body></html>'''
    pages.append(("index.html", idx))
    bad = [f for f, p in pages if HANGUL.search(p)]
    if bad and not DRAFT: raise SystemExit(f"CHECK FAILED: hangul in output {bad[:5]}")
    for f, p in pages:
        if DRAFT: p = p.replace("<body>\n", '<body>\n<div style="background:#c00;color:#fff;text-align:center;padding:4px;font:13px sans-serif">DRAFT — not for publication</div>\n', 1)
        open(os.path.join(out, f), "w", encoding="utf-8").write(p)
    print(f"[{l}{' DRAFT' if DRAFT else ''}] pages: 197 papers + index, block quotations: {nbq} → {out}")


fail_any = False
for l in LANGS:
    BOOK, TT, AL, T = load(l)
    failed = check(l, BOOK, AL, T)
    fail_any |= failed
    if CHUNK: continue
    if failed and not DRAFT:
        print(f"CHECK FAILED [{l}] — site/{l}/commentary/ not written (use --draft for a preview)"); continue
    build(l, TT, AL, T)
if fail_any: print("errors 1"); sys.exit(1)
print("errors 0")
