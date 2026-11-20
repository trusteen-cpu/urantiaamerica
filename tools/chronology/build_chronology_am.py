# Urantia Book Chronology → site/es|fr|pt/chronology/  (Urantia America)
#   원본: 극동판 영어 원고  urantiafareast 홈페이지/tools/chronology_en/data_en.txt  (읽기만 함)
#   번역: events_<l>.txt  — 영어 원고의 사건 줄(월|사건|근거)마다 한 줄씩, 같은 순서로 옮긴 사건 문구
#   시기·월·시대 이름·'Paper N' 은 이 도구가 규칙대로 옮겨 data_<l>.txt 로 적은 뒤 페이지를 만든다.
#   인용(« » / “ ”)이 든 사건은 amq.check 로 공식 번역 본문에 글자 그대로 있는지 확인한다.
import html, os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.normpath(os.path.join(HERE, ".."))
SITE = os.path.normpath(os.path.join(TOOLS, "..", "site"))
sys.path.insert(0, TOOLS)
import amq  # noqa: E402

EN_SRC = os.path.normpath(os.path.join(TOOLS, "..", "..", "urantiafareast 홈페이지", "tools", "chronology_en", "data_en.txt"))
E = html.escape
NB = " "

# ---------------------------------------------------------------- 영어 원고 읽기
def parse(path):
    eras, cur, row = [], None, None
    for line in open(path, encoding="utf-8").read().splitlines():
        if not line.strip(): continue
        if line.startswith("# "): cur = dict(name=line[2:].strip(), rows=[]); eras.append(cur); continue
        m = re.match(r"^(\d+)\|(.+)$", line)
        if m and line.count("|") == 1: row = dict(no=m[1], when=m[2].strip(), ev=[]); cur["rows"].append(row); continue
        mo, ev, ref = (line.split("|") + ["", ""])[:3]
        row["ev"].append((mo.strip() if mo.strip() != "-" else "", ev.strip(), ref.strip()))
    return eras

# ---------------------------------------------------------------- 언어별 규칙
ERAS = {
 "es": ["La formación del universo y de la Tierra", "El comienzo y la evolución de la vida", "La aparición de la humanidad",
        "La civilización después de Adán (a. C.)", "La época de Jesús", "Después de Jesús"],
 "fr": ["La formation de l’univers et de la Terre", "L’apparition et l’évolution de la vie", "L’apparition de l’humanité",
        "La civilisation après Adam (av. J.-C.)", "L’époque de Jésus", "Après Jésus"],
 "pt": ["A formação do universo e da Terra", "O início e a evolução da vida", "O surgimento da humanidade",
        "A civilização depois de Adão (a.C.)", "A época de Jesus", "Depois de Jesus"],
}
MONTHS_EN = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
MONTHS = {
 "es": ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"],
 "fr": ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "aout", "septembre", "octobre", "novembre", "décembre"],
 "pt": ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"],
}
ABOUT = {"es": "Hacia ", "fr": "Vers ", "pt": "Por volta de "}
PAPER = {"es": ("Documento", "(completo)"), "fr": ("Fascicule", "(entier)"), "pt": ("Documento", "(completo)")}
SEP = {"es": ".", "fr": " ", "pt": " "}


def num(n, l):
    """정수 → 그 언어의 자릿수 표기 (네 자리 이하는 구분 없음)"""
    s = str(n)
    if len(s) <= 4: return s
    out = ""
    while len(s) > 3: out = SEP[l] + s[-3:] + out; s = s[:-3]
    return s + out


def dec(x, l):
    return (("%g" % x).replace(".", ","))


def when(w, l):
    m = re.match(r"^([\d.]+) billion years ago$", w)
    if m:
        x = float(m[1])
        if l == "es": return f"Hace {num(int(x * 1000), l)} millones de años"
        if l == "fr": return f"Il y a {dec(x, l)} milliard{'s' if x >= 2 else ''} d’années"
        return f"Há {dec(x, l)} {'bilhões' if x >= 2 else 'bilhão'} de anos"
    m = re.match(r"^([\d.]+) million years ago$", w)
    if m:
        x = float(m[1])
        if l == "es": return f"Hace {dec(x, l)} {'millón' if x == 1 else 'millones'} de años"
        if l == "fr": return f"Il y a {dec(x, l)} million{'s' if x >= 2 else ''} d’années"
        return f"Há {dec(x, l)} {'milhões' if x >= 2 else 'milhão'} de anos"
    m = re.match(r"^([\d,]+) years ago$", w)
    if m:
        n = num(int(m[1].replace(",", "")), l)
        return {"es": f"Hace {n} años", "fr": f"Il y a {n} ans", "pt": f"Há {n} anos"}[l]
    m = re.match(r"^([\d,]+)(?:–([\d,]+))? B\.C\.$", w)
    if m:
        a = num(int(m[1].replace(",", "")), l)
        b = "–" + num(int(m[2].replace(",", "")), l) if m[2] else ""
        return a + b + {"es": " a. C.", "fr": " av. J.-C.", "pt": " a.C."}[l]
    m = re.match(r"^A\.D\. (\d+)(?:–(\d+))?$", w)
    if m:
        return m[1] + ("–" + m[2] if m[2] else "") + {"es": " d. C.", "fr": " apr. J.-C.", "pt": " d.C."}[l]
    raise ValueError("시기 형식을 모름: " + w)


def day(d, l):
    if d == "1": return {"es": "1", "fr": "1er", "pt": "1º"}[l]
    return d


def date_part(p, l, carry_month=None):
    m = re.match(r"^([A-Z][a-z]+)(?: (\d+))?$", p)
    if m:
        mo = MONTHS[l][MONTHS_EN.index(m[1])]
        if not m[2]: return mo
        return f"{day(m[2], l)} {mo}" if l == "fr" else f"{day(m[2], l)} de {mo}"
    m = re.match(r"^(\d+)$", p)
    if m: return None  # 달 없는 날짜 — 앞 부분과 합친다
    raise ValueError("월 형식을 모름: " + p)


def month(s, l):
    if not s: return ""
    about = s.startswith("About ")
    if about: s = s[6:]
    parts = s.split("–")
    if len(parts) == 1:
        out = date_part(parts[0], l)
    else:
        a, b = parts
        if re.fullmatch(r"\d+", b):           # February 7–26 → 7–26 de febrero
            m = re.match(r"^([A-Z][a-z]+) (\d+)$", a)
            mo = MONTHS[l][MONTHS_EN.index(m[1])]
            d1 = day(m[2], l)
            out = f"{d1}–{b} {mo}" if l == "fr" else f"{d1}–{b} de {mo}"
        else:
            out = date_part(a, l) + "–" + date_part(b, l)
    out = (ABOUT[l] + out) if about else out
    return out[0].upper() + out[1:]


def ref_tr(ref, l):
    w, allw = PAPER[l]
    return ref.replace("Paper ", w + " ").replace("(all)", allw)


def typo(s, l):
    """fr: ; : ! ? 앞과 « 뒤·» 앞에 붙는 공백 / fr·pt: 자릿수 공백 → 줄바꿈 없는 공백"""
    if l in ("fr", "pt"): s = re.sub(r"(\d) (\d{3})\b", "\\1" + NB + "\\2", s)
    if l == "fr":
        s = re.sub(r" ([;:!?»])", NB + r"\1", s)
        s = s.replace("« ", "«" + NB)
    return s


UI = {
 "es": dict(title="Cronología de El libro de Urantia", crumb="Inicio", crumb2="Estudios de El libro de Urantia",
            lead="Desde la nebulosa de Andronóver, hace 987.000 millones de años, hasta la publicación de El libro de Urantia · {n} entradas · pulse una referencia (documento:sección.párrafo) para abrir el texto",
            th=("N.º", "Fecha", "Acontecimiento · Referencia"),
            foot="Las fechas y los días de la semana de la vida de Jesús siguen el relato de la Parte IV de El libro de Urantia.",
            desc="Las fechas que da El libro de Urantia, ordenadas por épocas: desde el comienzo de la nebulosa de Andronóver, hace 987.000 millones de años, hasta la publicación del libro."),
 "fr": dict(title="Chronologie du Livre d’Urantia", crumb="Accueil", crumb2="Études du Livre d’Urantia",
            lead="De la nébuleuse d’Andronover, il y a 987 milliards d’années, à la publication du Livre d’Urantia · {n} entrées · cliquez sur une référence (fascicule:section.paragraphe) pour ouvrir le texte",
            th=("N°", "Époque", "Événement · Référence"),
            foot="Les dates et les jours de la semaine de la vie de Jésus suivent le récit de la quatrième partie du Livre d’Urantia.",
            desc="Les dates données par le Livre d’Urantia, classées par époques : du début de la nébuleuse d’Andronover, il y a 987 milliards d’années, à la publication du livre."),
 "pt": dict(title="Cronologia do Livro de Urântia", crumb="Início", crumb2="Estudos do Livro de Urântia",
            lead="Da nebulosa de Andronover, há 987 bilhões de anos, até a publicação do Livro de Urântia · {n} itens · clique numa referência (documento:seção.parágrafo) para abrir o texto",
            th=("Nº", "Data", "Acontecimento · Referência"),
            foot="As datas e os dias da semana da vida de Jesus seguem o relato da Parte IV do Livro de Urântia.",
            desc="As datas dadas pelo Livro de Urântia, organizadas por épocas: do início da nebulosa de Andronover, há 987 bilhões de anos, até a publicação do livro."),
}

# ---------------------------------------------------------------- 페이지 (극동판 build_chronology.py 와 같은 틀)
def target(part):
    m = re.match(r"^(\d+):(\d+)\.(\d+)", part)
    if m: return f"{m[1]}:{m[2]}.{m[3]}"
    m = re.match(r"^(\d+):(\d+)(?:-\d+)?$", part)
    if m: return f"{m[1]}:{m[2]}.1" if m[2] != "0" else f"{m[1]}:0.1"
    m = re.match(r"^(?:Paper|Documento|Fascicule)\s*(\d+)", part)
    if m: return f"{m[1]}:0.1"
    return None


def refs_html(ref, l):
    out = []
    for part in [p.strip() for p in re.split(r",\s*", ref) if p.strip()]:
        t = target(part)
        out.append(f'<a class=rf href="{amq.link(l, t)}">{E(part)}</a>' if t else f"<span class=rf>{E(part)}</span>")
    return "".join(out)


CSS = """:root{--navy:#14213D;--gold:#B8925A;--gold2:#D9BF8C;--bg:#FBF9F4;--card:#fff;--ink:#23272F;--dim:#6b7280;--line:#e6dfcf;--tint:#f6f1e6;--chip:#eee6d4}
@media (prefers-color-scheme:dark){:root{--bg:#12141a;--card:#181b22;--ink:#dfe3ea;--dim:#98a0ae;--line:#2b3040;--tint:#1d212a;--chip:#2a2f3b}}
*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.6 "Segoe UI",system-ui,sans-serif}
a{color:inherit}header{background:linear-gradient(160deg,#14213D,#1C2E4A);color:#F7F3EA;border-bottom:3px solid var(--gold)}
header .in{max-width:1000px;margin:0 auto;padding:46px 16px 18px}.crumb{font-size:13px;color:#aebbd2}.crumb a{text-decoration:none;border-bottom:1px solid rgba(255,255,255,.25)}
header h1{margin:8px 0 4px;font-size:28px}header p{margin:0;color:#c9ced8;font-size:14.5px}
nav.era{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line)}
nav.era .in{max-width:1000px;margin:0 auto;padding:8px 16px;display:flex;gap:6px;overflow-x:auto;white-space:nowrap}
nav.era a{font-size:13.5px;text-decoration:none;padding:4px 11px;border-radius:999px;border:1px solid var(--line);background:var(--card)}
nav.era a:hover{border-color:var(--gold);color:var(--gold)}
main{max-width:1000px;margin:0 auto;padding:6px 16px 60px}
section{scroll-margin-top:52px}h2{display:flex;align-items:center;gap:10px;font-size:20px;margin:30px 0 10px;color:var(--navy)}
@media (prefers-color-scheme:dark){h2{color:var(--gold2)}}
h2 span{display:inline-flex;flex:0 0 30px;width:30px;height:30px;border-radius:50%;background:var(--gold);color:#fff;align-items:center;justify-content:center;font-size:15px}
h2 em{font-style:normal;font-size:13px;color:var(--dim);font-weight:400}
.tw{overflow-x:auto;border:1px solid var(--line);border-radius:12px;background:var(--card)}
table{border-collapse:collapse;width:100%;font-size:15px}
thead th{background:var(--navy);color:#F7F3EA !important;font-weight:600;font-size:13.5px;padding:9px 10px;text-align:left}
td{border-top:1px solid var(--line);padding:9px 10px;vertical-align:top}tbody tr:nth-child(even){background:var(--tint)}
.no{width:48px;text-align:center;color:var(--dim);font-size:13px}.wh{width:170px;font-weight:700;color:var(--navy)}
@media (prefers-color-scheme:dark){.wh{color:var(--gold2)}}
ul{list-style:none;margin:0;padding:0}li{display:flex;flex-wrap:wrap;align-items:baseline;gap:4px 8px;padding:2px 0}li+li{border-top:1px dashed var(--line);padding-top:5px;margin-top:3px}
.mo{font-size:12.5px;font-weight:700;color:var(--gold);min-width:90px}.tx{flex:1;min-width:180px}
.rf{font:12.5px Georgia,serif;color:var(--dim);background:var(--chip);padding:1px 8px;border-radius:999px;white-space:nowrap;text-decoration:none}
a.rf:hover{background:var(--gold);color:#fff}
@media (max-width:640px){.wh{width:104px;font-size:14px}.no{width:34px}td{padding:8px 6px}.mo{min-width:auto}}
footer{max-width:1000px;margin:0 auto;padding:0 16px 40px;color:var(--dim);font-size:13px}"""


def translate(en_eras, l):
    evs = [x for x in open(os.path.join(HERE, f"events_{l}.txt"), encoding="utf-8").read().splitlines() if x.strip()]
    n_en = sum(len(r["ev"]) for e in en_eras for r in e["rows"])
    if len(evs) != n_en: raise SystemExit(f"[{l}] 사건 줄 수가 영어와 다름: {len(evs)} ≠ {n_en}")
    it = iter(evs); eras = []; lines = []
    for i, e in enumerate(en_eras):
        ne = dict(name=ERAS[l][i], rows=[]); eras.append(ne); lines.append("# " + ne["name"])
        for r in e["rows"]:
            nr = dict(no=r["no"], when=when(r["when"], l), ev=[]); ne["rows"].append(nr)
            lines.append(f"{nr['no']}|{nr['when']}")
            for mo, _ev, ref in r["ev"]:
                t = (month(mo, l), next(it).strip(), ref_tr(ref, l)); nr["ev"].append(t)
                lines.append(f"{t[0] or '-'}|{t[1]}|{t[2]}")
    open(os.path.join(HERE, f"data_{l}.txt"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    return eras


def check_quotes(eras, l):
    n = 0
    for e in eras:
        for r in e["rows"]:
            for _mo, ev, ref in r["ev"]:
                for q in re.findall(r"«\s*(.+?)\s*»|“(.+?)”", ev):
                    q = q[0] or q[1]
                    cit = target(ref.split(",")[0].strip())
                    if not amq.check(l, cit, q): raise SystemExit(f"[{l}] 인용이 공식 번역 {cit} 에 없음: {q}")
                    n += 1
    return n


def build(l, eras):
    U = UI[l]; T = lambda s: E(typo(s, l))
    nav = "".join(f"<a href='#e{i}'>{T(e['name'])}</a>" for i, e in enumerate(eras, 1))
    body = ""
    for i, e in enumerate(eras, 1):
        trs = ""
        for r in e["rows"]:
            lis = "".join(f"<li>{('<span class=mo>' + T(mo) + '</span>') if mo else ''}<span class=tx>{T(ev)}</span>{refs_html(ref, l)}</li>"
                          for mo, ev, ref in r["ev"])
            trs += f"<tr><td class=no>{r['no']}</td><td class=wh>{T(r['when'])}</td><td><ul>{lis}</ul></td></tr>"
        body += (f"<section id='e{i}'><h2><span>{i}</span>{T(e['name'])}<em>{len(e['rows'])}</em></h2>"
                 f"<div class=tw><table><thead><tr><th class=no>{T(U['th'][0])}</th><th class=wh>{T(U['th'][1])}</th><th>{T(U['th'][2])}</th></tr></thead><tbody>{trs}</tbody></table></div></section>")
    total = sum(len(e["rows"]) for e in eras)
    page = (f'<!DOCTYPE html>\n<html lang="{l}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
            f'<title>{T(U["title"])}</title>\n<meta name="description" content="{T(U["desc"])}">\n'
            f'<style>{CSS}</style><script src="/home-button.js" data-pos="left" defer></script></head><body>\n'
            f'<header><div class="in"><div class="crumb"><a href="/{l}/">{T(U["crumb"])}</a> › {T(U["crumb2"])}</div><h1>{T(U["title"])}</h1>\n'
            f'<p>{T(U["lead"].format(n=total))}</p></div></header>\n<nav class="era"><div class="in">{nav}</div></nav>\n<main>{body}</main>\n'
            f'<footer>{T(U["foot"])}</footer>\n</body></html>\n')
    out = os.path.join(SITE, l, "chronology")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "index.html")
    open(path, "w", encoding="utf-8").write(page)
    return path, page, total


shape = lambda eras: [(r["no"], len(r["ev"]), [ref for *_, ref in r["ev"]]) for e in eras for r in e["rows"]]
norm_ref = lambda s: re.sub(r"^(Paper|Documento|Fascicule) ", "", s).replace(" (all)", "").replace(" (completo)", "").replace(" (entier)", "")

en_eras = parse(EN_SRC)
for l in ("es", "fr", "pt"):
    eras = translate(en_eras, l)
    again = parse(os.path.join(HERE, f"data_{l}.txt"))          # 적어 둔 원고를 다시 읽어 구조 확인
    diff = [a[0] for a, b in zip(shape(again), shape(en_eras)) if a[:2] != b[:2] or [norm_ref(x) for x in a[2]] != [norm_ref(x) for x in b[2]]]
    if diff or len(again) != len(en_eras): raise SystemExit(f"[{l}] 구조가 영어 원고와 다름: {diff}")
    nq = check_quotes(again, l)
    path, page, total = build(l, again)
    ko = re.findall(r"[가-힣]", page)
    if ko: raise SystemExit(f"[{l}] 한글이 남음")
    nev = sum(len(r["ev"]) for e in again for r in e["rows"])
    print(f"{l}: eras {len(again)} · entries {total} · events {nev} · links {page.count('class=rf href')} · quotes ok {nq} · {path}")
