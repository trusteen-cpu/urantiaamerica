# -*- coding: utf-8 -*-
# 「유란시아서 용어집」 스페인어·프랑스어·포르투갈어판 → site/<es|fr|pt>/glossary/index.html
#   극동판 영어판 site/en/glossary/index.html 의 화면(CSS·머리)을 읽어 오기만 하고(그 파일은 고치지 않음),
#   자료 G 를 [English, 공식 번역 표제어, 번역 풀이] 로 바꾼다.
#   원고: glossary_<l>.json (영어판과 같은 순서·같은 개수). 화면에서는 번역 표제어 기준으로 Intl.Collator(언어별) 정렬.
#   표제어는 Urantia Foundation 공식 번역(tools/data/<l>.json)에 나오는 용어. 영어 원어를 작게 함께 보인다.
#   용어집에는 유란시아서 인용문이 없다(풀이만). 인용을 넣게 되면 amq.cut/amq.check 로 검사할 것.
import json, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
H = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.dirname(H)
SITE = os.path.normpath(os.path.join(TOOLS, "..", "site"))
FE = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\glossary\index.html"

t0 = open(FE, encoding="utf-8").read()
i = t0.index("var G="); j = t0.index("];", i) + 2
EN = json.loads(t0[i + 6:j - 1])
HEAD = t0[:t0.index("<header>")]
STYLE_ADD = "dt small{display:block;font-weight:400;font-size:13px;color:var(--dim);margin-top:2px}"

UI = {
 "es": dict(
  title="Glosario de El libro de Urantia",
  desc="Glosario de términos, nombres y lugares de El libro de Urantia: busque o recorra de la A a la Z.",
  ph="Buscar términos y definiciones (en español o en inglés)",
  home="⌂ Inicio",
  src="Entradas del glosario: English Master Glossary of The Urantia Book (edición de voluntarios), traducidas al español. "
      "Los términos siguen la traducción oficial de la Fundación Urantia (El libro de Urantia); entre paréntesis, el término original en inglés. "
      "Orden alfabético según el término en español.",
  none="No se encontraron entradas.",
  of="de", entries="entradas"),
 "fr": dict(
  title="Glossaire du Livre d’Urantia",
  desc="Glossaire des termes, noms et lieux du Livre d’Urantia\u00a0: recherchez ou parcourez de A à Z.",
  ph="Rechercher un terme ou une définition (en français ou en anglais)",
  home="⌂ Accueil",
  src="Entrées du glossaire\u00a0: English Master Glossary of The Urantia Book (édition bénévole), traduites en français. "
      "Les termes suivent la traduction officielle de la Fondation Urantia (le Livre d’Urantia)\u00a0; entre parenthèses, le terme original anglais. "
      "Classement alphabétique selon le terme français.",
  none="Aucune entrée trouvée.",
  of="sur", entries="entrées"),
 "pt": dict(
  title="Glossário de O Livro de Urântia",
  desc="Glossário de termos, nomes e lugares de O Livro de Urântia: pesquise ou percorra de A a Z.",
  ph="Pesquisar termos e definições (em português ou em inglês)",
  home="⌂ Início",
  src="Verbetes do glossário: English Master Glossary of The Urantia Book (edição de voluntários), traduzidos para o português. "
      "Os termos seguem a tradução oficial da Fundação Urântia (O Livro de Urântia); entre parênteses, o termo original em inglês. "
      "Ordem alfabética segundo o termo em português.",
  none="Nenhum verbete encontrado.",
  of="de", entries="verbetes"),
}

JS = r"""
var LANG=document.documentElement.lang;
var $=function(i){return document.getElementById(i)};
function esc(t){return t.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;')}
function f1(c){var d=c.normalize('NFD').replace(/[\u0300-\u036f]/g,'');return d.length===1?d.toLowerCase():c.toLowerCase()}
function fold(t){var o='';for(var k=0;k<t.length;k++)o+=f1(t.charAt(k));return o}
function letter(t){var c=f1(t.replace(/^[^A-Za-z\u00C0-\u024F]+/,'').charAt(0)).toUpperCase();return /[A-Z]/.test(c)?c:'#'}
var COL=new Intl.Collator(LANG,{sensitivity:'base',numeric:true});
G.forEach(function(r){r.f=fold(r[1]+' \u0001 '+r[0]);r.d=fold(r[2])});
G.sort(function(a,b){return COL.compare(a[1],b[1])||COL.compare(a[0],b[0])});
var ALL='ABCDEFGHIJKLMNOPQRSTUVWXYZ'.split('');
function hl(t,q){t=String(t);if(!q)return esc(t);var f=fold(t),o='',p=0,k;
  while((k=f.indexOf(q,p))>=0){o+=esc(t.slice(p,k))+'<mark>'+esc(t.slice(k,k+q.length))+'</mark>';p=k+q.length}
  return o+esc(t.slice(p))}
function render(q){
  q=fold((q||'').trim());
  var rows=q?G.filter(function(r){return r.f.indexOf(q)>=0||r.d.indexOf(q)>=0}):G;
  if(q)rows=rows.slice().sort(function(a,b){return (b.f.indexOf(q)>=0)-(a.f.indexOf(q)>=0)});
  var h='',cur='',have={};
  rows.forEach(function(r){var L=letter(r[1]);have[L]=1;
    if(!q&&L!==cur){if(cur)h+='</dl>';h+='<h2 id="L'+L+'">'+L+'</h2><dl>';cur=L}
    var en=fold(r[0])===fold(r[1])?'':' <small>('+hl(r[0],q)+')</small>';
    h+='<div class="e"><dt>'+hl(r[1],q)+en+'</dt><dd>'+hl(r[2],q)+'</dd></div>'});
  if(q)h='<dl>'+h+'</dl>'; else if(cur)h+='</dl>';
  $('list').innerHTML=rows.length?h:'<div class="none">__NONE__</div>';
  $('count').textContent=q?rows.length+' __OF__ '+G.length+' __ENT__':G.length+' __ENT__';
  $('az').innerHTML=ALL.map(function(L){return '<a href="#L'+L+'"'+(have[L]||q?'':' class="off"')+' data-l="'+L+'">'+L+'</a>'}).join('');
}
$('q').oninput=function(){render(this.value)};
$('az').onclick=function(e){var a=e.target.closest('a');if(!a)return;if($('q').value){e.preventDefault();$('q').value='';render('');location.hash='L'+a.dataset.l}};
render('');
"""


def fr_typo(s):
    s = s.replace("« ", "«\u00a0").replace(" »", "\u00a0»")
    s = re.sub(r"«(?=\S)", "«\u00a0", s); s = re.sub(r"(?<=\S)»", "\u00a0»", s)
    return re.sub(r"(?<=\S) ?([;:!?])(?=\s|$|\))", "\u00a0\\1", s)


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


def build(l):
    D = json.load(open(os.path.join(H, f"glossary_{l}.json"), encoding="utf-8"))
    assert len(D) == len(EN), f"[{l}] 개수 다름: {len(D)} != {len(EN)}"
    for a, b in zip(D, EN):
        assert a[0] == b[0], f"[{l}] 순서·원어 다름: {a[0]!r} != {b[0]!r}"
        assert len(a) == 3 and a[1].strip() and a[2].strip(), f"[{l}] 빈 칸: {a[0]}"
    U = UI[l]
    rows = []
    for e, term, d in D:
        if l == "fr": d = fr_typo(d); term = fr_typo(term)
        rows.append([e, term.strip(), d.strip()])
    data = json.dumps(rows, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")
    head = HEAD
    R = [('<html lang="en">', f'<html lang="{l}">'),
         ("<title>Urantia Book Glossary</title>", f"<title>{esc(U['title'])}</title>"),
         ('content="A glossary of Urantia Book terms, names, and places — search or browse A to Z."', f'content="{esc(U["desc"])}"'),
         ("</style>", STYLE_ADD + "\n</style>\n<script src='/home-button.js' defer></script>")]
    for a, b in R:
        assert a in head, "못 찾음: " + a[:60]
        head = head.replace(a, b, 1)
    js = JS.replace("__NONE__", U["none"]).replace("__OF__", U["of"]).replace("__ENT__", U["entries"])
    page = (head + "<header>\n"
            f' <div class="top"><h1>{esc(U["title"])}</h1><input id="q" type="search" placeholder="{esc(U["ph"])}" autocomplete="off"><a href="/{l}/">{U["home"]}</a></div>\n'
            ' <nav class="az" id="az"></nav>\n</header>\n<main>\n <div class="count" id="count"></div>\n <div id="list"></div>\n'
            f' <p class="src">{esc(U["src"])}</p>\n</main>\n<script>\nvar G={data};\n{js}</script>\n</body></html>\n')
    # 검사
    assert not re.search(r"[가-힣]", page), f"[{l}] 한글이 남음"
    for bad in ("Urantia Book Glossary", "No entries found", "/?lang=en", "Search terms"):
        assert bad not in page, f"[{l}] 영어 화면 글자 남음: {bad}"
    if l == "es":
        hits = [r[0] for r in rows if re.search(r"\bMiguel\b", r[1] + " " + r[2])]
        assert not hits, f"[es] 'Miguel' 대신 'Micael': {hits[:5]}"
    out = os.path.join(SITE, l, "glossary"); os.makedirs(out, exist_ok=True)
    open(os.path.join(out, "index.html"), "w", encoding="utf-8").write(page)
    print(f"{l}/glossary: {len(rows)} entries, {len(page)//1024} KB")


if __name__ == "__main__":
    for l in (sys.argv[1:] or ["es", "fr", "pt"]):
        build(l)
