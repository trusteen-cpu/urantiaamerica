# -*- coding: utf-8 -*-
"""Urantia America 언어별 첫 화면 만들기 — site/index.html 과 i18n.js 로 /en/ /es/ /fr/ /pt/ 를 만든다.
   (극동판 tools/build_home_i18n.py 를 줄인 것) index.html 이나 i18n.js 를 고친 뒤 다시 돌린다: python build_home.py"""
import html, json, os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.normpath(os.path.join(HERE, "..", "site"))
BASE = "https://america.urantiareaders.com"
VER = "20261120a"
LOCALE = {"en": "en_US", "es": "es_ES", "fr": "fr_FR", "pt": "pt_BR"}
DESC = {
    "en": "Study resources for The Urantia Book in one place: the full text, paper-by-paper commentary, topical studies, glossary, maps, chronology, and questions and answers.",
    "es": "Recursos para leer y estudiar El libro de Urantia: el texto completo, comentarios por documento, estudios temáticos, glosario, mapas, cronología y preguntas y respuestas.",
    "fr": "Ressources pour lire et étudier le Livre d’Urantia : texte intégral, commentaires par fascicule, études thématiques, glossaire, cartes, chronologie et questions-réponses.",
    "pt": "Recursos para ler e estudar O Livro de Urântia: o texto integral, comentários por documento, estudos temáticos, glossário, mapas, cronologia e perguntas e respostas.",
}

js = r"""
const fs=require('fs'),vm=require('vm');const c={window:{}};vm.createContext(c);
vm.runInContext(fs.readFileSync(process.argv[1],'utf8'),c);
process.stdout.write(JSON.stringify({ui:c.window.SITE.ui,menu:c.window.SITE.menu,links:c.window.SITE.links,langs:c.window.SITE.langs,hl:c.window.HTML_LANG}));
"""
S = json.loads(subprocess.check_output(["node", "-e", js, os.path.join(SITE, "i18n.js")]).decode("utf-8"))
tpl = open(os.path.join(SITE, "index.html"), encoding="utf-8").read().replace("\r\n", "\n")
tpl = re.sub(r'(</title>\n)<meta name="description"[\s\S]*?<meta property="og:locale"[^\n]*\n', r"\1", tpl, count=1)


def alternates():
    out = [f'<link rel="alternate" hreflang="{S["hl"][l["code"]]}" href="{BASE}/{l["code"]}/">' for l in S["langs"]]
    out.append(f'<link rel="alternate" hreflang="x-default" href="{BASE}/">')
    return "\n".join(out)


def sub(s, a, b):
    assert s.count(a) == 1, a
    return s.replace(a, b)


def head_meta(lang, title, url):
    d, t = html.escape(DESC[lang]), html.escape(title)
    return (f'<meta name="description" content="{d}">\n<link rel="canonical" href="{url}">\n{alternates()}\n'
            f'<meta property="og:type" content="website">\n<meta property="og:title" content="{t}">\n'
            f'<meta property="og:description" content="{d}">\n<meta property="og:url" content="{url}">\n'
            f'<meta property="og:locale" content="{LOCALE[lang]}">\n')


def page(lang):
    ui = S["ui"][lang]
    title = ui["brand"] + " | Urantia America"
    s = sub(tpl, '<html lang="en">', f'<html lang="{S["hl"][lang]}">')
    s = sub(s, '<meta charset="utf-8">\n', '<meta charset="utf-8">\n<base href="/">\n')
    s = re.sub(r"<title>.*?</title>\n", lambda m: f"<title>{html.escape(title)}</title>\n" + head_meta(lang, title, f"{BASE}/{lang}/"), s, count=1)
    s = re.sub(r'<h1 id="brand">.*?</h1>', lambda m: f'<h1 id="brand">{html.escape(ui["brand"])}</h1>', s, count=1)
    s = sub(s, '<p id="tagline"></p>', f'<p id="tagline">{html.escape(ui["tagline"])}</p>')
    s = sub(s, '<h2 id="menuTitle">Menu</h2>', f'<h2 id="menuTitle">{html.escape(ui["menu"])}</h2>')
    items = []
    for i, m in enumerate(m for m in S["menu"] if lang in m.get("only", [lang])):
        href = S["links"][lang].get(m["id"]) or f'soon.html?p={m["id"]}&amp;lang={lang}'
        items.append(f'<li><a href="{href}"><span class="num">{i + 1}</span><span class="name">{html.escape(m[lang])}</span></a></li>')
    s = sub(s, '<ol class="menu" id="menu"></ol>', '<ol class="menu" id="menu">\n' + "\n".join(items) + "\n</ol>")
    s = sub(s, f'<script src="i18n.js?v={VER}"></script>', f'<script>window.FORCE_LANG = "{lang}";</script>\n<script src="i18n.js?v={VER}"></script>')
    return s


for l in S["langs"]:
    code = l["code"]
    os.makedirs(os.path.join(SITE, code), exist_ok=True)
    open(os.path.join(SITE, code, "index.html"), "w", encoding="utf-8", newline="\n").write(page(code))
    print("만듦", code, S["ui"][code]["brand"])
