# -*- coding: utf-8 -*-
# 「A New Reader's Guide to The Urantia Book」(새 독자 12주 안내서) 스페인어·프랑스어·포르투갈어판 → site/<l>/newcomer/
#   극동판 tools/zh/newcomer/build_newcomer_zh.py 를 옮긴 것. 화면·렌더러는 극동판 영어 빌더 tools/build_newreader_en.py 를
#   읽어 와(exec, 고치지 않음) 그대로 쓰고, 영어 원고(newreader-book\en, front_en)의 줄마다 번역 단위를 바꿔 끼운다.
#   원고: src/cNN.json (영어 단위, extract_src.py)
#        + <l>/cNN.json (번역: 블록 인용을 뺀 모든 단위, 같은 키)
#        + 블록 인용: auto_<l>.json (prep.py 자동) 또는 <l>/quotes_cNN.json (손으로 자른 것, 이쪽이 우선)
#   검사: 키 누락·남는 키·구조·빈 값·자리표시·한글·표 칸의 '|'·영어 잔재(경고)·인용(tools/data/<l>.json 원문 그대로, 공백만 무시)
#   python build_newcomer_am.py es [fr pt]           검사 + 통과 시 site/<l>/newcomer/ 빌드
#   python build_newcomer_am.py es --chunk c02       그 묶음만 검사 (쓰지 않음)
#   python build_newcomer_am.py es --draft           빠진 단위는 영어로 채워 _draft_<l>/ 에 미리보기
import glob, json, os, re, shutil, sys
sys.stdout.reconfigure(encoding="utf-8")
sys.dont_write_bytecode = True
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지"
EN_BUILDER = os.path.join(FE, "tools", "build_newreader_en.py")
EN_FIG = os.path.join(FE, "site", "en", "newcomer", "fig")
sys.path.insert(0, H)
import extract_src as X  # noqa: E402  (같은 폴더: 줄 분류·파일 목록·청크 정의)

args = sys.argv[1:]
DRAFT = "--draft" in args
CHUNK = args[args.index("--chunk") + 1] if "--chunk" in args else None
LANGS = [a for a in args if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]

HANGUL = re.compile(r"[가-힣ᄀ-ᇿ㄰-㆏]")
ENGW = re.compile(r"\b(the|and|which|that|with|of|is|are|was|were|this|these|from|by|his|their)\b")
nows = lambda s: re.sub(r"\s+", "", s)
isq = lambda v: isinstance(v, dict) and "q" in v

SRC, CH = {}, {}
for c in X.CHUNKS:
    d = json.load(open(os.path.join(H, "src", c + ".json"), encoding="utf-8"))
    SRC.update(d); CH.update({k: c for k in d})


def cit_keys(cit, book):
    keys, cur = [], None
    for part in re.split(r"\s*,\s*", cit.strip()):
        m = re.fullmatch(r"(?:(\d+):(\d+)\.)?(\d+)(?:\s*[-–]\s*(\d+))?", part)
        if not m: return None
        if m.group(1): cur = (m.group(1), m.group(2))
        if cur is None: return None
        for p in range(int(m.group(3)), int(m.group(4) or m.group(3)) + 1):
            k = f"{cur[0]}:{cur[1]}.{p}"
            if k not in book: return None
            keys.append(k)
    return keys


def fr_nb(s):
    s = re.sub(r" ([;:!?»])", "\u00a0\\1", s)
    return s.replace("« ", "«\u00a0")


def load(l):
    book = json.load(open(os.path.join(ROOT, "tools", "data", f"{l}.json"), encoding="utf-8"))
    auto = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    T = {}
    for c in X.CHUNKS:
        p = os.path.join(H, l, c + ".json")
        if os.path.exists(p): T.update(json.load(open(p, encoding="utf-8")))
        elif not CHUNK or CHUNK == c: print(f"  [missing file] {l}/{c}.json")
        p = os.path.join(H, l, f"quotes_{c}.json")
        hand = json.load(open(p, encoding="utf-8")) if os.path.exists(p) else {}
        for k in hand:
            if not (k in SRC and isq(SRC[k]) and CH[k] == c): T.setdefault("__bad_quote_keys", []).append(f"{l}/quotes_{c}.json: {k}")
        for k, v in SRC.items():
            if CH[k] == c and isq(v):
                q = hand.get(k, auto.get(k))
                if q is not None: T[k] = {"q": q, "cit": v["cit"]}
    return book, T


def check(l, book, T):
    def quote_ok(text, cit):
        ks = cit_keys(cit, book)
        if not ks: return False, "citation not in book"
        hay = nows("".join(book[k] for k in ks))
        for piece in re.split(r"…|\.\.\.", text):
            piece = nows(piece).strip("“”\"'‘’«»")
            if piece and piece not in hay: return False, piece[:50]
        return True, ""
    errs, warns, badq, nq = [], [], [], 0
    errs += [f"key in quotes file is not a quotation of that chunk: {x}" for x in T.pop("__bad_quote_keys", [])]
    for k, ev in SRC.items():
        if CHUNK and CH[k] != CHUNK: continue
        if k not in T: errs.append(f"missing: {k}"); continue
        tv = T[k]
        if isq(ev):
            nq += 1
            if not isinstance(tv.get("q"), str) or not tv["q"].strip(): errs.append(f"empty quotation: {k}"); continue
            ok, why = quote_ok(tv["q"], ev["cit"])
            if not ok: badq.append(f"{k} [{ev['cit']}] {why}")
            if HANGUL.search(tv["q"]): errs.append(f"hangul: {k}")
            continue
        if isinstance(ev, dict):   # 부록 1 낱말 {"term","def"}
            if not isinstance(tv, dict) or set(tv) != set(ev) or not all(isinstance(x, str) for x in tv.values()):
                errs.append(f"shape differs (need {{\"term\",\"def\"}}): {k}"); continue
            pairs = [(ev["term"], tv["term"]), (ev["def"], tv["def"])]
        elif isinstance(ev, list):
            if not isinstance(tv, list) or len(tv) != len(ev) or not all(isinstance(x, str) for x in tv):
                errs.append(f"shape differs (need {len(ev)} strings): {k}"); continue
            if any("|" in x for x in tv): errs.append(f"'|' in table cell: {k}")
            pairs = list(zip(ev, tv))
        else:
            if not isinstance(tv, str): errs.append(f"not a string: {k}"); continue
            pairs = [(ev, tv)]
        for es_, ts in pairs:
            if not ts.strip(): errs.append(f"empty: {k}"); continue
            if HANGUL.search(ts): errs.append(f"hangul: {k}")
            if "\n" in ts: errs.append(f"line break inside value: {k}")
            if k.startswith("ui:"):
                if set(re.findall(r"\{\w+\}", es_)) != set(re.findall(r"\{\w+\}", ts)): errs.append(f"placeholders differ: {k}")
            elif "|" in ts and "|" not in es_: errs.append(f"'|' not allowed: {k}")
            plain = re.sub(r"\*[^*]+\*|“[^”]*”|\"[^\"]*\"|\([^)]*\)", "", ts)
            hits = ENGW.findall(plain)
            if nows(ts) == nows(es_) and len(es_.split()) > 3: warns.append(f"untranslated? {k}")
            elif len(hits) >= 2: warns.append(f"English words {hits[:4]}: {k}")
    for k in T:
        if k not in SRC: errs.append(f"extra key: {k}")
    scope = f" chunk {CHUNK}" if CHUNK else ""
    tot = [k for k in SRC if not CHUNK or CH[k] == CHUNK]
    print(f"[{l}{scope}] units present: {sum(1 for k in tot if k in T)}/{len(tot)} · quotations checked: {nq} · bad: {len(badq)}"
          f" · errors {len(errs)} · warnings {len(warns)}")
    for e in errs[:40]: print("  ERR", e)
    if len(errs) > 40: print(f"  … {len(errs) - 40} more errors")
    for b in badq[:40]: print("  BADQ", b)
    if len(badq) > 40: print(f"  … {len(badq) - 40} more bad quotations")
    for w in warns[:30]: print("  WARN", w)
    if len(warns) > 30: print(f"  … {len(warns) - 30} more warnings")
    return bool(errs or badq)


# ---------- 영어 빌더 빌려 오기 ----------
def load_en(l, U):
    t = open(EN_BUILDER, encoding="utf-8").read()
    t = t[:t.rstrip().rindex("\nmain()")]  # 끝의 main() 호출은 빼고 함수·CSS만
    R = [
        ('<html lang="en">', f'<html lang="{l}">'),
        ('f"Figure {week}.{nf}" if week else f"Figure {nf}"',
         'U["ui:figure_label"].format(week=week, n=nf) if week else U["ui:figure_label_nw"].format(n=nf)'),
        ('f"Table {week}.{nt}" if week else f"Table {nt}"',
         'U["ui:table_label"].format(week=week, n=nt) if week else U["ui:table_label_nw"].format(n=nt)'),
        ('href="/en/book/#{first}"', f'href="/{l}/book/#{{first}}"'),
        ("'<a href=\"./\">Contents</a>'", "f'<a href=\"./\">{esc(U[\"ui:contents\"])}</a>'"),
        ('>Contents</a>', '>{esc(U["ui:contents"])}</a>'),
    ]
    for a, b in R:
        if a not in t: raise SystemExit("not found in the English builder: " + a[:70])
        t = t.replace(a, b)
    ns = {"__file__": EN_BUILDER, "__name__": "en_newreader_borrowed", "U": U}
    exec(compile(t, EN_BUILDER, "exec"), ns)
    ns["TITLE"] = U["ui:title"]; ns["SUB"] = U["ui:sub"]
    ns["BOX_TITLE"] = {"points": U["ui:box_points"], "questions": U["ui:box_questions"], "next": U["ui:box_next"]}
    ns["CSS"] = ns["CSS"].replace("body{", "body{overflow-wrap:break-word;hyphens:auto;", 1)
    return ns


def build(l, T):
    def V(k):
        v = T.get(k, SRC[k]) if DRAFT else T[k]
        if l != "fr" or isq(v): return v
        if isinstance(v, list): return [fr_nb(x) for x in v]
        if isinstance(v, dict): return {a: fr_nb(b) for a, b in v.items()}
        return fr_nb(v)

    def rebuild(name, lines):
        """영어 원고 줄 → 같은 마크다운 머리표 + 번역 단위. 오디오북 안내 줄은 뺀다."""
        out = []
        for i, ln in enumerate(lines, 1):
            s = ln.strip(); k = f"{name}:{i}"
            if X.SKIP(name, s): continue
            if k not in SRC: out.append(ln); continue
            z = V(k)
            if s.startswith(":::box"): out.append(":::box " + z)
            elif s.startswith("@part"): out.append(f"@part {z[0]} | {z[1]}")
            elif re.match(r"^# Week \d+", s) or s.startswith("Text:"): out.append(ln)  # 주 제목·본문 범위는 따로 씀
            elif s.startswith("### "): out.append("### " + z)
            elif s.startswith("## "): out.append("## " + z)
            elif s.startswith("# "): out.append("# " + z)
            elif s.startswith("[[Figure"):
                path = re.match(r"^\[\[Figure\s*\|\s*([^|]+?)\s*\|", s).group(1)
                out.append(f"[[Figure | {path} | {z}]]")
            elif s.startswith("Table:"): out.append("Table: " + z)
            elif s.startswith("|"): out.append("| " + " | ".join(z) + " |")
            elif s.startswith(">"): out.append(f"> {z['q']} [{SRC[k]['cit']}]" if isq(z) else "> " + z)
            elif s.startswith("- "): out.append("- " + z)
            elif re.match(r"^\d+\.\s", s): out.append(re.match(r"^\d+\.", s).group() + " " + z)
            else: out.append(z)
        return out

    U = {k: V(k) for k in SRC if k.startswith("ui:")}
    E = load_en(l, U)
    esc, inline, render, page, head = E["esc"], E["inline"], E["render"], E["page"], E["head"]
    files = dict(X.FILES)
    OUT = os.path.join(H, f"_draft_{l}") if DRAFT else os.path.join(ROOT, "site", l, "newcomer")
    os.makedirs(os.path.join(OUT, "fig"), exist_ok=True)
    wk = lambda n: U["ui:week_label"].format(n=n)
    pages = []
    weeks = []
    for n in range(1, 13):
        name = f"w{n:02d}"; L = X.read(files[name]); part = None; i = 0
        while i < len(L) and not L[i].startswith("# "):
            if L[i].startswith("@part"): part = V(f"{name}:{i + 1}")
            i += 1
        title = V(f"{name}:{i + 1}")
        has_text = L[i + 1].startswith("Text:")
        text = U["ui:text_label"].format(text=V(f"{name}:{i + 2}")) if has_text else ""
        rest = rebuild(name, L)[i + 2 if has_text else i + 1:]
        weeks.append(dict(n=n, title=title, text=text, lines=rest, part=part, file=f"{name}.html"))
    extra = []
    for name, fn in (("closing", "afterword.html"), ("reading", "reading.html")):
        L = rebuild(name, X.read(files[name]))
        extra.append(dict(title=L[0][2:].strip(), lines=L[1:], file=fn))
    short = lambda t: re.split(r"\s+[—–]+\s+|\s*—\s*", t)[0].strip()
    seq = ([(w["file"], wk(w["n"])) for w in weeks] + [(e["file"], short(e["title"])) for e in extra]
           + [("words.html", U["ui:appx1"])])
    for k, w in enumerate(weeks):
        body, _ = render(w["lines"], w["n"])
        p = w["part"] or next((x["part"] for x in reversed(weeks[:k]) if x["part"]), None)
        eb = (p[0].upper() + "  ·  " if p else "") + U["ui:week_eyebrow"].format(n=w["n"])
        pages.append((w["file"], page(f"{wk(w['n'])}: {w['title']}", eb, w["title"], w["text"], body,
                                      seq[k - 1] if k else None, seq[k + 1], "")))
    for j, e in enumerate(extra):
        k = len(weeks) + j
        body, _ = render(e["lines"], 0)
        pages.append((e["file"], page(e["title"], "", e["title"], "", body, seq[k - 1], seq[k + 1])))
    # 부록 1: 새 낱말 — 영어판과 같은 순서(영어 알파벳), 번역 용어를 크게·영어 원어를 작게
    first = {t: n for t, (_, n) in X.term_rows().items()}
    dl = ""
    for k, v in SRC.items():
        if not k.startswith("terms:"): continue
        z = V(k); en = v["term"]; n = first.get(en, 0)
        dl += (f"<dt>{inline(z['term'])} <small style='font-weight:400'>{esc(en) if z['term'] != en else ''}</small></dt>"
               f"<dd>{inline(z['def'])}" + (f" <small>({esc(wk(n))})</small>" if n else "") + "</dd>")
    pages.append(("words.html", page(U["ui:appx1"], "", U["ui:appx1"], "",
                                     f"<p>{inline(U['ui:appx1_intro'])}</p><dl class='terms'>" + dl + "</dl>", seq[-2], None)))
    # 첫 쪽
    F = lambda name: rebuild(name, X.read(files[name]))
    toc, cur = [], None
    for w in weeks:
        if w["part"] and w["part"] != cur:
            cur = w["part"]; toc.append(f'<div class="part">{esc(cur[0])}<small>{esc(cur[1])}</small></div>')
        toc.append(f'<div class="toc"><a href="{w["file"]}"><b>{esc(wk(w["n"]))}</b><span>{inline(w["title"])}</span></a></div>')
    toc.append(f'<div class="part">{esc(U["ui:part_after"])}</div>')
    for f_, t in [(e["file"], e["title"]) for e in extra] + [("words.html", U["ui:appx1"])]:
        toc.append(f'<div class="toc"><a href="{f_}"><b>·</b><span>{inline(t)}</span></a></div>')
    idx = (head(U["ui:title"])
           + f'<header class="top"><div class="eb">{esc(U["ui:eyebrow_index"])}</div><h1>{esc(U["ui:title"])}</h1><p>{esc(U["ui:sub"])}</p>'
             f'<div class="by">{esc(U["ui:author"])}</div></header>\n'
           + '<div class="wrap">'
           + f'<h2 class="sec">{esc(U["ui:sec_preface"])}</h2>' + render(F("preface"), 0)[0]
           + f'<h2 class="sec">{esc(U["ui:sec_howto"])}</h2>' + render(F("howto"), 0)[0]
           + f'<h2 class="sec">{esc(U["ui:sec_contents"])}</h2>' + "\n".join(toc)
           + '<div class="colo">' + render(F("colophon"), 0)[0] + "</div>"
           + "\n</div>\n</body>\n</html>\n")
    pages.append(("index.html", idx))
    bad = [f for f, p in pages if HANGUL.search(p)]
    enlink = [f for f, p in pages if "/en/book/" in p or "/audiobook/" in p]
    if (bad or enlink) and not DRAFT: raise SystemExit(f"CHECK FAILED: hangul {bad} / English links {enlink} in output")
    for f, p in pages:
        if DRAFT: p = p.replace("<body>\n", '<body>\n<div style="background:#c00;color:#fff;text-align:center;padding:4px;font:13px sans-serif">DRAFT — not for publication</div>\n', 1)
        open(os.path.join(OUT, f), "w", encoding="utf-8").write(p)
    # 그림: 영어판이 만든 webp 를 그대로 복사(그림 속 글자는 영어)
    miss, nfig = [], 0
    for p in sorted(set(E["FIGS"])):
        fn = os.path.basename(p).replace(".png", ".webp"); s = os.path.join(EN_FIG, fn)
        if os.path.exists(s): shutil.copy2(s, os.path.join(OUT, "fig", fn)); nfig += 1
        else: miss.append(fn)
    if miss: print("  WARN figures missing in the English edition:", miss)
    nq = sum(1 for w in weeks for x in w["lines"] if x.startswith(">"))
    print(f"[{l}{' DRAFT' if DRAFT else ''}] pages: {len(pages)} (12 weeks + afterword + reading + words + index), figures: {nfig}, "
          f"block quotations in weeks: {nq}, Hangul: {bad or 'none'}, English links: {enlink or 'none'} → {OUT}")


fail_any = False
for l in LANGS:
    book, T = load(l)
    failed = check(l, book, T)
    fail_any |= failed
    if CHUNK: continue
    if failed and not DRAFT:
        print(f"CHECK FAILED [{l}] — site/{l}/newcomer/ not written (use --draft for a preview)"); continue
    build(l, T)
if fail_any: print("errors 1"); sys.exit(1)
print("errors 0")
