import json, sys
sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools"); import amq
B = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\abridged\\"
todo = json.load(open(B + r"work\todo_fr_c23.json", encoding="utf-8"))
C = {
"177.b5.q": ("177:1.3", "Même un adolescent", "du Dieu d’un univers"),
"177.b25.q": ("177:4.10", "Dans son mental, Judas", "de tout son cœur."),
"178.b14.q": ("178:1.15", "il ressemble au germe", "en de nouvelles expressions"),
"179.b18.q": ("179:3.8", "un serviteur n’est pas", "celui qui l’envoie."),
"180.b11.q": ("180:1.6", "c’est la fidélité", "que Jésus demande."),
"180.b32.q": ("180:6.2", "Il est réellement profitable", "venir dans votre cœur."),
"181.b10.q": ("181:1.6", "Vous aurez des tribulations", "du service perpétuel."),
"181.b20.q": ("181:2.25", "Vous n’êtes que des êtres finis", "ayez bon courage"),
"182.b5.q": ("182:3.4", "Et maintenant, ô Père", "et non la mienne."),
"182.b25.q": ("182:3.11", "L’esprit avait triomphé", "entretenir des doutes."),
"183.b11.q": ("183:1.1", "Ces épreuves inhumaines", "la volonté divine du Père"),
"184.b24.q": ("184:4.6", "Après avoir vécu", "nouvelle et inouïe."),
"185.b5.q": ("185:3.4", "mon royaume est la famille", "qui est aux cieux."),
"185.b31.q": ("185:7.2", "Tu n’aurais aucun pouvoir", "autorisé d’en haut."),
}
out = {}
for k in todo:
    v, a, b = C[k]
    t = amq.text("fr", v)
    i = t.index(a); j = t.index(b, i) + len(b)
    s = t[i:j]
    assert amq.check("fr", v, s), k
    out[k] = s
    print(k, s)
assert set(out) == set(todo)
json.dump(out, open(B + r"fr\quotes_c23.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
