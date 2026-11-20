# -*- coding: utf-8 -*-
# 「A Conceptual Overview of The Urantia Book」(Meredith J. Sprunger) 스페인어·프랑스어·포르투갈어판
#   → site/es/overview/index.html, site/fr/overview/index.html, site/pt/overview/index.html
#   원고: src/c01.json      영어 단위 (극동판 tools/zh/overview/src/c01.json 사본, 손대지 않음)
#         src_<l>.json      같은 키의 번역. 인용 단위(.q)는 {"refs": "..."} 만 — 인용문은 quotes_am.py 가
#                           공식 번역(tools/data/<l>.json)에서 글자 그대로 잘라 넣는다(번역하지 않음).
#   화면: 극동판 영어판 site/en/overview/index.html 의 CSS·스크립트를 그대로 가져옴(읽기만).
#   검사(하나라도 걸리면 그 언어 페이지를 쓰지 않고 exit 1):
#     키·구조(n) 같음 · 한글 없음 · 인용이 그 절에 글자 그대로(amq.check) · [편:장.절] 참조가 영어와 같음
#   실행: python tools/overview/build_overview_am.py  [es fr pt]
import html, json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
SITE = os.path.join(ROOT, "site")
EN_PAGE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\overview\index.html"
sys.path.insert(0, H)
import quotes_am  # noqa: E402

esc = html.escape
HANGUL = re.compile(r"[가-힣ㄱ-ㅎㅏ-ㅣ]")
SRC = json.load(open(os.path.join(H, "src", "c01.json"), encoding="utf-8"))
REF = re.compile(r"\[(?:See )?(?:Paper (\d+)|(\d+)\s*[:.]\s*(\d+)(?:\s*[.:]\s*([\d\s,\-–]+))?)\]")
HTML_LANG = {"es": "es", "fr": "fr", "pt": "pt-BR"}


def strings(v):
    if isinstance(v, str): yield v
    elif isinstance(v, dict):
        for k, x in v.items():
            if k not in ("cit", "n"): yield from strings(x)
    elif isinstance(v, list):
        for x in v: yield from strings(x)


def refs_of(s):
    return sorted(re.sub(r"\s+", "", m.group(0)) for m in REF.finditer(s))


def build(l):
    T = json.load(open(os.path.join(H, f"src_{l}.json"), encoding="utf-8"))
    if l == "fr":  # 프랑스어 문장부호: ; : ! ? 앞과 « » 안쪽 공백을 줄바꿈 없는 공백으로 (인용문은 공식 번역 그대로)
        def nb(v):
            if isinstance(v, str):
                v = re.sub(r" ([;:!?»])", " \\1", v)
                return re.sub(r"« ", "« ", v)
            if isinstance(v, dict): return {k: (x if k in ("n", "cit") else nb(x)) for k, x in v.items()}
            return v
        T = {k: (v if k.startswith("ui.") and k not in ("ui.src_note", "ui.lead") else nb(v)) for k, v in T.items()}
    err = []
    # 인용 채우기
    D, nq = {}, 0
    for k, sv in SRC.items():
        if k not in T:
            err.append(("missing", k)); continue
        tv = T[k]
        if k.endswith(".q"):
            if not isinstance(tv, dict) or set(tv) != {"refs"}:
                err.append(("structure", k)); continue
            paras = []
            for i, p in enumerate(sv["paras"]):
                txt = quotes_am.quote(l, k, i, p["cit"])
                if not quotes_am.check(l, p["cit"], txt):
                    err.append(("quote", k, p["cit"]))
                paras.append({"cit": p["cit"], "text": txt}); nq += 1
            tv = {"paras": paras, "refs": tv["refs"]}
        elif type(sv) is not type(tv) or (isinstance(sv, dict) and (set(sv) != set(tv) or sv.get("n") != tv.get("n"))):
            err.append(("structure", k)); continue
        D[k] = tv
        for s in strings(tv):
            if HANGUL.search(s): err.append(("hangul", k))
        if k.startswith("p") and not k.startswith("part"):
            a = " ".join(strings(sv)) if not k.endswith(".q") else sv["refs"]
            b = " ".join(strings(tv)) if not k.endswith(".q") else tv["refs"]
            if refs_of(a) != refs_of(b): err.append(("refs", k, refs_of(a), refs_of(b)))
    err += [("extra", k) for k in T if k not in SRC]
    for k, need in (("ui.ref_see", "{ref}"), ("ui.ref_paper", "{n}"), ("ui.part_label", "{rn}")):
        if need not in T.get(k, ""): err.append(("placeholder", k))
    nparts = len([k for k in SRC if re.match(r"^part\d+\.title$", k)])
    if len(T.get("ui.part_rn", "").split("|")) != nparts: err.append(("part_rn", "count"))
    nsec = sum(1 for k in SRC if k.endswith(".h"))
    print(f"[{l}] units {len(T)}/{len(SRC)}  sections {nsec}  quotation paragraphs {nq}  problems {len(err)}")
    for e in err[:30]: print("   ", e)
    if err:
        return False

    U = D.__getitem__

    def link_refs(s):
        def label(m):
            if m.group(1): return "[" + U("ui.ref_paper").format(n=m.group(1)) + "]"
            inner = m.group(0)[1:-1]
            if inner.startswith("See "): return "[" + U("ui.ref_see").format(ref=inner[4:]) + "]"
            return m.group(0)

        def href(m):
            if m.group(1): return f"{m.group(1)}:0.1"
            p, sec = m.group(2), m.group(3)
            par = re.match(r"\d+", m.group(4).strip()).group() if m.group(4) else ("0" if sec == "0" else "1")
            return f"{p}:{sec}.{par}"

        out, last = [], 0
        for m in REF.finditer(s):
            out.append(esc(s[last:m.start()]))
            out.append(f'<a class="rf" href="/{l}/book/#{href(m)}">{esc(label(m))}</a>')
            last = m.end()
        out.append(esc(s[last:]))
        return "".join(out)

    def render_part(no):
        o, secs, si = [], [], 0
        keys = sorted((k for k in SRC if re.match(rf"^p{no}\.\d{{3}}\.", k)), key=lambda k: int(k.split(".")[1]))
        for k in keys:
            t = k.split(".")[2]; v = D[k]
            if t == "h":
                if si: o.append("</section>")
                si += 1; sid = f"p{no}-{si}"; secs.append((sid, v))
                cls = " class='summary'" if SRC[k].lower() == "summary" else ""
                o.append(f"<section id='{sid}'{cls}><h3>{esc(v)}</h3>")
            elif t == "q":
                o.append("<blockquote>" + "".join(f"<p>{esc(p['text'])}</p>" for p in v["paras"]) +
                         f"<cite>{link_refs(v['refs'].strip())}</cite></blockquote>")
            elif t in ("pt", "sp"):
                o.append(f"<p class='{t}'><span class='n'>{v['n']}.</span>{link_refs(v['text'])}</p>")
            else:
                o.append(f"<p>{link_refs(v)}</p>")
        if si: o.append("</section>")
        return secs, "\n".join(o)

    en = open(EN_PAGE, encoding="utf-8").read()
    css = en[en.index("<style>") + 7:en.index("</style>")]
    css = css.replace("word-break:keep-all", "word-break:normal;hyphens:auto")
    script = en[en.rindex("<script>"):en.rindex("</script>") + 9]
    assert "' — open/close'" in script
    script = script.replace("' — open/close'", json.dumps(U("ui.toggle_suffix"), ensure_ascii=False).replace("'", "’").replace('"', "'"))

    RN = U("ui.part_rn").split("|")
    nos = sorted(int(m.group(1)) for k in SRC for m in [re.match(r"^part(\d+)\.title$", k)] if m)
    arts, toc = [], []
    for idx, no in enumerate(nos):
        rn = RN[idx]; secs, h = render_part(no); title = U(f"part{no}.title")
        toc.append(f"<a href='#p{no}'><span>{esc(rn)}</span>{esc(title)}</a>")
        sub = "".join(f"<a href='#{sid}'>{esc(t)}</a>" for sid, t in secs)
        lead = f"<p class='lead2'>{esc(U(f'part{no}.lead'))}</p>" if f"part{no}.lead" in D else ""
        arts.append(f"<article class='part' id='p{no}'><div class='ph'><div class='rn'>{esc(U('ui.part_label').format(rn=rn))}</div><h2>{esc(title)}</h2>"
                    f"<nav class='sub'>{sub}</nav></div>{lead}{h}</article>")

    page = (f"<!doctype html>\n<html lang='{HTML_LANG[l]}'>\n<head>\n<meta charset='utf-8'>\n<meta name='viewport' content='width=device-width,initial-scale=1'>\n"
            f"<title>{esc(U('ui.html_title'))}</title>\n<style>" + css + "</style>\n"
            "<script src='/home-button.js' defer></script>\n</head>\n<body>\n"
            f"<header id='top'><div class='in'><div class='crumb'><a href='/{l}/'>{esc(U('ui.crumb_home'))}</a> › {esc(U('ui.crumb_section'))}</div>\n"
            f"<h1>{esc(U('ui.h1'))}</h1>\n"
            f"<p class='lead'>{esc(U('ui.lead'))}</p>\n"
            f"<p class='by'>{U('ui.by')}</p>\n"
            f"<div class='all'><button type='button' id='openAll'>{esc(U('ui.open_all'))}</button><button type='button' id='closeAll'>{esc(U('ui.close_all'))}</button></div>\n"
            "<nav class='toc'>" + "".join(toc) + "</nav></div></header>\n<main>" + "\n".join(arts) +
            f"<p class='src'>{esc(U('ui.src_note'))}</p>"
            f"</main>\n<a class='top' href='#top' aria-label='{esc(U('ui.back_to_top'))}'>↑</a>\n" + script + "\n</body></html>\n")

    if HANGUL.search(page): print("   Hangul in page"); return False
    if re.search(r"/(en|zh)/book/|lang=en", page): print("   foreign link left"); return False
    out = os.path.join(SITE, l, "overview"); os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)
    print(f"   wrote site/{l}/overview/index.html  {len(page)} bytes, parts {len(nos)}, ref links {page.count(chr(34)+'/'+l+'/book/#')}")
    return True


ok = all([build(l) for l in (sys.argv[1:] or ["es", "fr", "pt"])])
sys.exit(0 if ok else 1)
