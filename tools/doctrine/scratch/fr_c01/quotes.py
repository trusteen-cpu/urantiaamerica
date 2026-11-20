# -*- coding: utf-8 -*-
import json, os
H = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(H, "..", "..")
FR = json.load(open(os.path.join(D, "..", "data", "fr.json"), encoding="utf-8"))
todo = json.load(open(os.path.join(D, "work", "todo_fr_c01.json"), encoding="utf-8"))

# key: (verse, start, end-inclusive)
C = {
 "ch00:3": ("0:12.13", "Mais nous savons", "significations de l’univers."),
 "ch01:3": ("0:3.23", "Le concept du JE SUIS", "la cause primordiale des causes."),
 "ch01:12": ("105:1.5", "Pour le mental fini", "certaines relations de source."),
 "ch01:14": ("0:3.21", "Une créature de l’espace-temps", "son libre arbitre inhérent et éternel"),
 "ch01:16": ("0:3.22", "Avec l’apparition", "aurait été inévitable."),
 "ch01:42": ("0:3.25", "La primauté absolue", "l’exercice de la foi."),
 "ch01:46": ("105:2.11", "en lui nous vivons", "de ce qui a été."),
 "ch02:9": ("104:2.4", "Cette même Trinité", "du Fils et de l’Esprit."),
 "ch02:16": ("10:1.3", "La personnalité divine", "libre arbitre divin."),
 "ch02:43": ("10:4.6", "La Trinité fonctionne", "en tant que Trinité."),
 "ch02:47": ("104:2.3", "En reconnaissant", "l’univers matériel."),
 "ch02:49": ("0:12.4", "Les Trinités sont", "inévitabilités divines."),
 "ch03:19": ("4:1.6", "Le Père Universel ne", "effondrement universel."),
 "ch03:37": ("111:5.5", "Ce choix de la créature", "un perfectionnement de la volonté"),
 "ch03:39": ("111:5.6", "Ce choix ne consiste", "ta volonté soit faite »."),
 "ch03:43": ("110:7.1", "la fusion dépend", "l’Ajusteur de Pensée."),
 "ch04:15": ("116:0.3", "La croissance expérientielle", "pas eu de croissance de Havona"),
 "ch04:29": ("117:4.9", "Il est vrai que les créatures", "de la volonté des mortels."),
 "ch05:7": ("12:1.16", "L’univers central", "l’ultimité de la création."),
 "ch05:16": ("12:1.12", "Les sept superunivers", "une unité créative primordiale."),
 "ch05:37": ("32:4.2", "Mais, malgré ce retrait", "personnalités assignés."),
 "ch05:47": ("50:1.1", "Il est vrai que le Fils Créateur", "jusqu’aux enfants des hommes."),
 "ch05:49": ("33:7.1", "Le Maitre-Fils Micaël", "pour juger leurs créatures"),
}
out = {}
keys = list(todo.keys()) if isinstance(todo, dict) else [t if isinstance(t, str) else t[0] for t in todo]
for k in keys:
    ref, a, b = C[k]
    v = FR[ref]
    i = v.index(a); j = v.index(b, i) + len(b)
    out[k] = v[i:j]
assert set(out) == set(C), set(C) ^ set(out)
os.makedirs(os.path.join(D, "fr"), exist_ok=True)
json.dump(out, open(os.path.join(D, "fr", "quotes_c01.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out))
