# -*- coding: utf-8 -*-
import json, os, re, sys
sys.stdout.reconfigure(encoding="utf-8")
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\doctrine"
sys.path.insert(0, os.path.join(H, ".."))
import amq

TODO = json.load(open(os.path.join(H, "work", "todo_fr_c04.json"), encoding="utf-8"))

# key: list of (start, end) snippets, inclusive
SPEC = {
 "ch17:3": [("La vérité révélée", "perdaient lentement du terrain.")],
 "ch17:8": [("C’est 1", "témoin de sa matérialisation.")],
 "ch17:15": [("Ils n’étaient pas encore capables", "par rapport aux dieux.")],
 "ch17:23": [("L’alliance de Melchizédek", "suivre ses instructions.")],
 "ch17:25": [("qu’il décrivait d’une manière", "au sujet du Père du Paradis.")],
 "ch17:27": [("La décision de Melchizédek", "comme un être surnaturel")],
 "ch17:36": [("Mais l’erreur des éducateurs", "par une révolution soudaine.")],
 "ch17:42": [("Durant cette époque", "la future effusion de Micaël.")],
 "ch17:44": [("L’un des buts de l’incarnation", "puisse apparaitre.")],
 "ch17:46": [("Ainsi, en perdant de vue", "du Fils d’effusion promis.")],
 "ch18:5": [("Le but de ces incarnations", "expériences successives d’effusion.")],
 "ch18:25": [("Je te recommande", "un Fils Créateur du Père du Paradis.")],
 "ch18:27": [("Tout au long de ton effusion", "ton Père du Paradis.")],
 "ch18:32": [("La grande mission", "spécialement aux créatures de chair.")],
 "ch18:36": [("comme constituant, en un seul", "satisfaisant complètement le Créateur Infini.")],
 "ch18:41": [("Un après-midi de fin d’été", "la souveraineté indiscutée de son univers.")],
 "ch19:3": [("le Christ Micaël, tout en étant", "précisément cet être composé.")],
 "ch19:11": [("Joshua ben Joseph savait", "le Fils de l’Homme.")],
 "ch19:13": [("Le Fils de l’Homme expérimenta", "d’une rare bonne humeur")],
 "ch19:19": [("Les Juifs n’avaient pas enseigné", "le Fils de Dieu ».")],
 "ch19:34": [("Il aborda cette tâche", "Jésus de Nazareth.")],
 "ch19:41": [("En tant que Fils de Dieu", "aime les mortels comme un frère")],
 "ch19:51": [("De la manière la plus touchante", "« Suis-moi. »")],
 "ch20:3": [("LE charme et la droiture", "par un seul d’entre eux.")],
 "ch20:11": [("leur expliqua que, plus tard", "avec leurs semblables.")],
 "ch20:22": [("C’est moins par les paroles", "les réalités du royaume.")],
 "ch20:33": [("ils vécurent et moururent", "créateur souverain d’un univers.")],
 "ch20:43": [("en tant que personnalité, il était isolé.", "incapable de pardonner.")],
 "ch20:46": [("Le fait qu’il n’était pas nécessaire", "les cas de Thomas et Nathanael")],
 "ch20:52": [("Pierre représentait l’une", "réellement et sincèrement Jésus")],
 "ch20:54": [("Alors, Jean, renonce", "chercher le salut.")],
 "ch20:56": [("N’oubliez jamais que", "ne peut être ordinaire.")],
 "ch21:6": [("jamais, avant la venue de Jésus", "à la maison du Père.")],
 "ch21:8": [("mais je suis venu vous montrer", "cherche également à vous trouver.")],
 "ch21:11": [("mais je vous assure que le Père", "du progrès spirituel.")],
 "ch21:19": [("Quand vous vous trouvez devant", "dons intellectuels et spirituels.")],
 "ch21:29": [("Ils pourraient ainsi commencer", "d’une affection paternelle.")],
 "ch21:35": [("La mansuétude authentique", "l’homme coopérant avec Dieu")],
 "ch21:42": [("mais plutôt que ses disciples", "le mal le plus pernicieux.")],
 "ch22:14": [("L’ancienne Pâque", "symbolisant la nouvelle dispensation")],
 "ch22:16": [("car, en toutes ces occasions", "du croyant avec Micaël.")],
 "ch22:23": [("En conséquence, Jésus choisit", "sa mort ignominieuse.")],
 "ch22:24": [("Ce fut l’homme, et non Dieu", "évènements humains sur Urantia")],
 "ch22:27": [("L’esprit avait triomphé", "entretenir des doutes.")],
 "ch22:34": [("Ce fut juste avant trois heures", "entre tes mains. »")],
 "ch22:36": [("Jésus mourut royalement", "durant toute la journée tragique.")],
}

def pat(s):
    return r"\s+".join(re.escape(w) for w in s.split())

out = {}
bad = 0
for k, v in TODO.items():
    verse = amq.text("fr", v["cit"])
    pieces = []
    pos = 0
    for a, b in SPEC[k]:
        m1 = re.compile(pat(a)).search(verse, pos)
        if not m1:
            print("START NOT FOUND", k, a); bad += 1; break
        m2 = re.compile(pat(b)).search(verse, m1.start())
        if not m2:
            print("END NOT FOUND", k, b); bad += 1; break
        pieces.append(verse[m1.start():m2.end()])
        pos = m2.end()
    q = " … ".join(pieces)
    out[k] = q
    if not amq.check("fr", v["cit"], q):
        print("CHECK FAIL", k); bad += 1
missing = set(TODO) - set(SPEC)
print("missing", missing, "bad", bad, "n", len(out))
json.dump(out, open(os.path.join(H, "fr", "quotes_c04.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
