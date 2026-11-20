import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
TH = os.path.dirname(os.path.dirname(HERE))
V = json.load(open(os.path.join(TH, '..', 'data', 'fr.json'), encoding='utf-8'))
todo = json.load(open(os.path.join(TH, 'work', 'todo_fr_c03.json'), encoding='utf-8'))

def piece(ref, a, b):
    t = V[ref]
    i = t.index(a)
    j = t.index(b, i) + len(b)
    return t[i:j]

C = {
 "ch13.s2.u2.q2#0": ("119:0.4", [("Le but de ces", "nouvelle manière.")]),
 "ch13.s2.u3.q1#0": ("21:4.5", [("Il est de notoriété", "littéralement fini.")]),
 "ch13.s3.u1.q1#0": ("120:2.8", [("La grande mission", "aux créatures de chair.")]),
 "ch13.s3.u2.q1#0": ("120:4.2", [("Mais ne vous méprenez", "Dieu incarné dans l’homme"), ("Le seul facteur", "Dieu et homme.")]),
 "ch13.s3.u3.q1#0": ("120:4.5", [("Les mortels d’Urantia", "dépassent notre entendement")]),
 "ch13.s4.u1.q1#0": ("120:0.5", [("Dans sa souveraineté", "son univers local."), ("Son pouvoir est illimité", "du temps et de l’espace.")]),
 "ch14.s2.u2.q1#0": ("33:3.6", [("Après ce vœu", "Proclamation finale d’Égalité »")]),
 "ch15.s1.u2.q1#0": ("35:2.1", [("Les Melchizédeks sont le premier", "la vie la plus humble.")]),
 "ch15.s1.u3.q1#0": ("35:2.3", [("L’ordre de filiation", "entièrement à eux-mêmes."), ("De leur propre initiative", "leur univers natal."), ("Ils sont par nature", "d’êtres intelligents.")]),
 "ch15.s2.u3.q1#0": ("35:2.8", [("La sagesse des Melchizédeks", "approuvées ultérieurement.")]),
 "ch15.s3.u3.q1#0": ("35:8.15", [("Les Lanonandeks appartiennent", "gouvernement d’univers.")]),
 "ch16.s1.u1.q1#0": ("26:1.1", [("Les anges sont les esprits", "hautement individualisées."), ("Au même titre", "celle des êtres humains.")]),
 "ch16.s1.u2.q1#0": ("38:2.1", [("Les anges n’ont pas", "des hommes."), ("Ils aiment beaucoup", "les aimer.")]),
 "ch16.s2.u1.q1#0": ("38:1.1", [("Le Fils Créateur et la représentante", "d’un univers local.")]),
 "ch16.s3.u4.q1#0": ("113:5.1", [("Les anges ne forcent", "de la volonté humaine.")]),
 "ch17.s1.u2.q1#0": ("29:0.11", [("Avec votre connaissance", "les directeurs de pouvoir."), ("En quelques rares", "les mondes des maisons.")]),
 "ch17.s1.u3.q1#0": ("42:1.2", [("La matière — l’énergie", "dépendent du Paradis.")]),
 "ch17.s1.u3.q2#0": ("42:1.5", [("La création de l’énergie", "dans tout l’espace."), ("Les organisateurs de force", "les mondes matériels.")]),
 "ch18.s1.u2.q1#0": ("43:7.1", [("Les natifs de chacune", "numéro soixante-dix.")]),
 "ch18.s2.u2.q1#0": ("45:5.3", [("Ces Fils Matériels représentent", "univers en évolution."), ("Ces Fils Matériels sont le chainon", "créatures matérielles des royaumes.")]),
 "ch18.s3.u3.q1#0": ("77:9.9", [("Les générations d’hommes", "leurs cousins dans la chair.")]),
}
out = {}
keys = list(todo.keys()) if isinstance(todo, dict) else list(todo)
for k in keys:
    ref, ps = C[k]
    out[k] = " … ".join(piece(ref, a, b) for a, b in ps)
missing = [k for k in C if k not in keys]
print("todo", len(keys), "cut", len(out), "extra", missing)
json.dump(out, open(os.path.join(TH, 'fr', 'quotes_c03.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
