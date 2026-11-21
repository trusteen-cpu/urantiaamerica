import json, sys
sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools"); import amq
B = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged\\"
todo = json.load(open(B + r"work\todo_fr_c19.json", encoding="utf-8"))
# (verse, start, end)
C = {
 "142.b14.q": ("142:2.2", "un p", "affectueux."),
 "142.b26.q": ("142:5.3", "quiconque", "foi elle-m"),
 "143.b5.q": ("143:1.4", "L\u2019amour est la plus", "relation supr\u00eame."),
 "143.b11.q": ("143:1.4", "Le but ultime", "des hommes."),
 "143.b27.q": ("143:5.6", "Dieu est esprit", "en v\u00e9rit\u00e9."),
 "144.b14.q": ("144:2.3", "La pri\u00e8re est le souffle", "du P\u00e8re."),
 "144.b37.q": ("144:8.4", "parmi ceux", "plus grand que lui"),
 "145.b18.q": ("145:3.11", "Ce qu\u2019un Fils", "EST."),
 "145.b32.q": ("145:5.4", "on ne pouvait", "physiques"),
 "146.b17.q": ("146:3.2", "l\u2019intol\u00e9rance", "que l\u2019on croit."),
 "147.b28.q": ("147:6.4", "le sabbat a \u00e9t\u00e9", "pour le sabbat."),
 "148.b5.q": ("148:6.10", "Dieu habite", "qu\u2019il est !"),
 "148.b20.q": ("148:4.8", "Il est exact", "p\u00e9cheurs."),
 "148.b44.q": ("148:6.11", "Le P\u00e8re qui est aux cieux n\u2019afflige", "des hommes."),
 "149.b35.q": ("149:6.5", "Je suis venu dans le monde", "par la confiance"),
 "149.b44.q": ("149:6.3", "C\u2019est pr\u00e9cis\u00e9ment", "sur terre."),
}
out = {}
for k in todo:
    v, a, b = C[k]
    t = amq.text("fr", v)
    i = t.index(a); j = t.index(b, i) + len(b)
    s = t[i:j]
    if b == "foi elle-m": s = t[i:t.index("\u00eame.", i)+5]
    s = s[0].upper() + s[1:] if False else s
    assert amq.check("fr", v, s), k
    out[k] = s
    print(k, s)
json.dump(out, open(B + r"fr\quotes_c19.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
