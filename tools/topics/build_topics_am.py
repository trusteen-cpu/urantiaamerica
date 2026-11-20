# -*- coding: utf-8 -*-
# 주제별 연구(Topical Studies) 스페인어·프랑스어·포르투갈어판 → site/<l>/topics/ (index.html + data.js)
#   틀: 극동판 영어판 site/en/topics/index.html (읽기만 함) 의 화면 글자만 바꾼다.
#   구조·절 번호: 극동판 영어 원고 tools/topics_en/data/tNNN.json (읽기만 함) — 주제·소제목·항목의 수와 순서를 그대로 쓴다.
#   글자: 주제 이름 names.py · 산문 <l>/c*.json (src/c*.json 과 같은 키) · 인용 auto_<l>.json + <l>/quotes_*.json (손으로 자른 것이 우선).
#   검사(하나라도 틀리면 만들지 않음): 키가 빠짐·남음·빈 값 · 한글 · 인용이 공식 번역 그 절에 글자 그대로 있는가(amq.check) ·
#         주제 이름 겹침 · 주제/소제목/항목 수가 영어와 같은가.
#   python build_topics_am.py [es fr pt] [--draft]   (--draft: 빠진 곳을 영어로 채워 미리보기용으로 만든다)
import glob, json, os, re, sys, unicodedata

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(H, "..", ".."))
sys.path.insert(0, os.path.join(H, ".."))
sys.path.insert(0, H)
import amq  # noqa: E402
from extract_src import load_en, units  # noqa: E402
from names import name  # noqa: E402

EN_PAGE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\topics\index.html"
HANGUL = re.compile(r"[ᄀ-ᇿ㄰-㆏가-힯]")
DRAFT = "--draft" in sys.argv
LANGS = [a for a in sys.argv[1:] if a in ("es", "fr", "pt")] or ["es", "fr", "pt"]

UI = {
 "es": {
  "title": "Estudios temáticos de El libro de Urantia",
  "desc": "Cien temas; cada uno resume la enseñanza de El libro de Urantia y cita el texto",
  "sub": "Cada tema resume la enseñanza del texto y lo cita",
  "find": "Buscar un tema",
  "choose": "Elegir un tema",
  "prev": "Tema anterior",
  "next": "Tema siguiente",
  "print": "Imprimir",
  "open": "Abrir {r} en el texto",
  "count": "{n} temas · de la A a la Z",
  "related": "Temas relacionados",
  "note": "Las referencias entre paréntesis indican documento:sección.párrafo de El libro de Urantia. Haga clic en una para abrir ese párrafo en una pestaña nueva.",
 },
 "fr": {
  "title": "Études thématiques du Livre d’Urantia",
  "desc": "Cent thèmes ; chacun résume l’enseignement du Livre d’Urantia et en cite le texte",
  "sub": "Chaque thème résume l’enseignement du texte et le cite",
  "find": "Chercher un thème",
  "choose": "Choisir un thème",
  "prev": "Thème précédent",
  "next": "Thème suivant",
  "print": "Imprimer",
  "open": "Ouvrir {r} dans le texte",
  "count": "{n} thèmes · de A à Z",
  "related": "Thèmes connexes",
  "note": "Les références entre parenthèses indiquent fascicule:section.paragraphe du Livre d’Urantia. Cliquez sur l’une d’elles pour ouvrir ce paragraphe dans un nouvel onglet.",
 },
 "pt": {
  "title": "Estudos temáticos de O Livro de Urântia",
  "desc": "Cem temas; cada um resume o ensinamento de O Livro de Urântia e cita o texto",
  "sub": "Cada tema resume o ensinamento do texto e o cita",
  "find": "Procurar um tema",
  "choose": "Escolher um tema",
  "prev": "Tema anterior",
  "next": "Próximo tema",
  "print": "Imprimir",
  "open": "Abrir {r} no texto",
  "count": "{n} temas · de A a Z",
  "related": "Temas relacionados",
  "note": "As referências entre parênteses indicam documento:seção.parágrafo de O Livro de Urântia. Clique em uma delas para abrir esse parágrafo em uma nova aba.",
 },
}
ARTICLES = re.compile(r"^(los|las|el|la|les|le|l’|os|as|o|a)\s+", re.I)


def sort_key(s):
    s = ARTICLES.sub("", s)
    return unicodedata.normalize("NFD", s).encode("ascii", "ignore").decode().lower()


def fr_typo(s):
    # 프랑스어: ; : ! ? » 앞과 « 뒤는 줄바꿈 없는 공백
    s = re.sub(r" ([;:!?»])", "\u00a0\\1", s)
    return re.sub(r"« ", "«\u00a0", s)


def build(l, EN):
    SRC, QS = {}, json.load(open(os.path.join(H, "src", "quotes.json"), encoding="utf-8"))
    for f in sorted(glob.glob(os.path.join(H, "src", "c*.json"))):
        SRC.update(json.load(open(f, encoding="utf-8")))
    SRC = {k: v for k, v in SRC.items() if not k.endswith(".t")}
    TR = {}
    for f in sorted(glob.glob(os.path.join(H, l, "c*.json"))):
        for k, v in json.load(open(f, encoding="utf-8")).items():
            if not k.endswith(".t"): TR[k] = v
    QT = json.load(open(os.path.join(H, f"auto_{l}.json"), encoding="utf-8"))
    for f in sorted(glob.glob(os.path.join(H, l, "quotes_*.json"))):
        QT.update(json.load(open(f, encoding="utf-8")))

    missing = [k for k in SRC if not (isinstance(TR.get(k), str) and TR[k].strip())]
    extra = [k for k in TR if k not in SRC] + [k for k in QT if k not in QS]
    qmiss = [k for k in QS if not (isinstance(QT.get(k), str) and QT[k].strip())]
    badq = [f"{k} ({QS[k]['cit']})" for k in QS if k not in qmiss and not amq.check(l, QS[k]["cit"], QT[k])]
    hangul = [k for k, v in list(TR.items()) + list(QT.items()) if isinstance(v, str) and HANGUL.search(v)]
    same = [k for k in SRC if TR.get(k) == SRC[k] and len(SRC[k].split()) > 2]  # 번역 안 된 듯한 것(보고만)
    names = [name(l, n) for n in range(1, 101)]
    dup = sorted({x for x in names if names.count(x) > 1})
    print(f"[{l}] prose {len(SRC) - len(missing)}/{len(SRC)} · quotations {len(QS) - len(qmiss)}/{len(QS)}"
          f" · bad quotations {len(badq)} · extra keys {len(extra)} · Hangul {len(hangul)} · duplicate names {len(dup)}"
          f" · identical to English (info) {len(same)}")
    for lab, L in (("missing prose", missing), ("missing quotation", qmiss), ("bad quotation", badq),
                   ("extra key", extra), ("Hangul", hangul), ("duplicate name", dup), ("identical to English", same)):
        if L: print(f"  {lab}: " + ", ".join(L[:12]) + (" …" if len(L) > 12 else ""))
    failed = any((missing, qmiss, badq, extra, hangul, dup))
    if failed and not DRAFT:
        print(f"  CHECK FAILED - site/{l}/topics/ not written"); return False

    def T(k):
        v = TR.get(k)
        s = v if isinstance(v, str) and v.strip() else SRC[k]
        return fr_typo(s) if l == "fr" else s

    def Q(k):
        v = QT.get(k)
        return v if isinstance(v, str) and v.strip() else QS[k]["q"]

    EN_NAME, data = {}, []
    for n in range(1, 101):
        E = EN[n]; U = units(E, n)
        assert set(k for k in U if not k.endswith(".t")) == set(k for k in SRC if k.startswith(f"t{n:03d}.")) | \
            set(k for k in QS if k.startswith(f"t{n:03d}.")), f"t{n:03d}: src differs from English - run extract_src.py"
        EN_NAME[E["t"]] = name(l, n)
        D = {"n": n, "t": name(l, n), "en": E["t"], "sum": T(f"t{n:03d}.sum"), "sections": [], "see": E.get("see", [])}
        for k, s in enumerate(E["sections"], 1):
            S = {"h": T(f"t{n:03d}.s{k}.h"), "items": []}
            for j, it in enumerate(s["items"], 1):
                key = f"t{n:03d}.s{k}.i{j}"
                S["items"].append({"q": Q(key), "r": it["r"]} if "q" in it else {"x": T(key), "r": it["r"]})
            D["sections"].append(S)
        data.append(D)
    for D in data:
        bad = [x for x in D["see"] if x not in EN_NAME]
        if bad: raise SystemExit(f"t{D['n']:03d}: related topic not in list: {bad}")
        D["see"] = [EN_NAME[x] for x in D["see"]]
    # 구조가 영어와 같은가
    assert len(data) == 100
    for D in data:
        E = EN[D["n"]]
        assert len(D["sections"]) == len(E["sections"])
        for S, ES in zip(D["sections"], E["sections"]):
            assert len(S["items"]) == len(ES["items"])
            assert all(("q" in a) == ("q" in b) and a["r"] == b["r"] for a, b in zip(S["items"], ES["items"]))
    data.sort(key=lambda d: sort_key(d["t"]))  # 그 언어 이름의 가나다(A–Z) 순

    t = open(EN_PAGE, encoding="utf-8").read()
    U = UI[l]
    js = lambda s: s.replace("\\", "\\\\").replace("'", "\\'")
    ui = (lambda k: fr_typo(U[k])) if l == "fr" else (lambda k: U[k])
    R = [
        ('<html lang="en">', f'<html lang="{l}">'),
        ('<title>Topical Studies of The Urantia Book</title>', f'<title>{ui("title")}</title>'),
        ('content="Topical Studies of The Urantia Book"', f'content="{ui("title")}"'),
        ('content="One hundred topics, each summarizing the teaching of The Urantia Book and quoting the text"', f'content="{ui("desc")}"'),
        ('<header><h1>Topical Studies of The Urantia Book</h1><div class="sub">Each topic summarizes the teaching of the text and quotes it</div></header>',
         f'<header><h1>{ui("title")}</h1><div class="sub">{ui("sub")}</div></header>'),
        ('placeholder="Find a topic"', f'placeholder="{ui("find")}"'),
        ('aria-label="Choose a topic"', f'aria-label="{ui("choose")}"'),
        ('aria-label="Previous topic"', f'aria-label="{ui("prev")}"'),
        ('aria-label="Next topic"', f'aria-label="{ui("next")}"'),
        ('<button id="prt">🖨 Print</button>', f'<button id="prt">🖨 {ui("print")}</button>'),
        ("""'<a class="rl" href="/en/book/#'""", f"""'<a class="rl" href="/{l}/book/#'"""),
        ("""title="Open ' + esc(r) + ' in the text">'""", 'title="' + js(ui("open")).replace("{r}", "' + esc(r) + '") + '">\''),
        ("L.length + ' topics · A to Z'", "'" + js(ui("count")).replace("{n}", "' + L.length + '") + "'"),
        ("'<div class=\"see\"><b>Related topics</b>'", "'<div class=\"see\"><b>" + js(ui("related")) + "</b>'"),
        ("'<div class=\"note\">References in parentheses are paper:section.paragraph of The Urantia Book. Click one to open that paragraph in a new tab.</div>'",
         "'<div class=\"note\">" + js(ui("note")) + "</div>'"),
        ("document.title = x.t + ' · Topical Studies of The Urantia Book';", "document.title = x.t + ' · " + js(ui("title")) + "';"),
        # 검색: 악센트 없이도 찾게(영어 이름으로도 찾을 수 있게 x.en 은 그대로 둔다)
        ("var k = this.value.replace(/\\s+/g, '').toLowerCase()", "var k = fold(this.value)"),
        ("var t = (L[i].t + L[i].en).replace(/\\s+/g, '').toLowerCase();", "var t = fold(L[i].t + L[i].en);"),
        ("function esc(s){", "function fold(s){ return String(s).normalize('NFD').replace(/[\\u0300-\\u036f\\s]/g, '').toLowerCase(); }\n  function esc(s){"),
    ]
    for a, b in R:
        if t.count(a) != 1: raise SystemExit("not found once in English page: " + a[:80])
        t = t.replace(a, b)
    assert '<script src="/home-button.js"' in t and "/en/" not in t
    out = os.path.join(ROOT, "site", l, "topics")
    os.makedirs(out, exist_ok=True)
    blob = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    open(os.path.join(out, "data.js"), "w", encoding="utf-8").write("window.TOPICS=" + blob + ";\n")
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(t)
    left = sorted(set(HANGUL.findall(t + blob)))
    nq = sum(1 for d in data for s in d["sections"] for it in s["items"] if "q" in it)
    ni = sum(len(s["items"]) for d in data for s in d["sections"])
    ns = sum(len(d["sections"]) for d in data)
    print(f"  {l}/topics: {len(data)} topics, {ns} sections, {ni} items ({nq} quotations) → {out}"
          + (" (DRAFT)" if failed else "") + f" · Hangul in output: {''.join(left) or 'none'}")
    return not failed


if __name__ == "__main__":
    EN = load_en()
    ok = [build(l, EN) for l in LANGS]
    if not all(ok) and not DRAFT: sys.exit(1)
