# Build fr/quotes_c02.json by cutting official text with (start, end) snippets.
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
T = json.load(open(os.path.join(ROOT, "work", "todo_fr_c02.json"), encoding="utf-8"))
E = "…"
# key: (lead_ellipsis, [(start, end), ...], trail_ellipsis)
S = {
 "w05:91": (0, [("Au cours de la longue lutte", "a vu le Père.")], 0),
 "w05:109": (1, [("et c’est alors que fut émise", "mondes de l’espace.")], 0),
 "w05:173": (0, [("Chez tout mortel", "pleinement conciliées")], 0),
 "w05:229": (0, [("L’ordre de filiation", "leur univers natal.")], 0),
 "w05:241": (0, [("Les Lanonandeks appartiennent", "gouvernement d’univers.")], 0),
 "w06:58": (1, [("la véritable reconstitution", "matinées de résurrection.")], 0),
 "w06:120": (1, [("maisonnia numéro un est", "le plus accentué.")], 0),
 "w06:148": (0, [("Mais la personnalité et les relations", "se souviendront de vous.")], 0),
 "w06:154": (0, [("Dans la vie physique", "niveaux s’élèvent.")], 0),
 "w06:180": (0, [("Les choses que vous auriez pu", "passer sur une autre.")], 1),
 "w06:220": (0, [("Pendant toute cette magnifique", "séparer l’homme et l’Ajusteur")], 1),
 "w06:271": (0, [("Depuis le moment où vous quittez", "sphères de Salvington.")], 0),
 "w06:284": (0, [("Le plan de survie des mortels", "âge de l’univers.")], 0),
 "w07:23": (0, [("Satania lui-même", "d’êtres humains.")], 0),
 "w07:37": (0, [("Le cerveau et le système nerveux", "ordres à trois cerveaux.")], 0),
 "w07:73": (0, [("Alors, l’Avonal d’effusion", "monde de l’effusion."),
                ("et simultanément a lieu", "choix spirituel.")], 0),
 "w07:89": (0, [("Le Fils d’effusion est le Prince de Paix.", "Prince de Paix."),
                ("Mais ces influences salutaires", "procession planétaire.")], 0),
 "w07:120": (0, [("LUCIFER était", "et son efficacité."),
                 ("Partant de ce début", "relations cosmiques.")], 0),
 "w07:124": (0, [("Il est très difficile", "et peut-être de l’univers."),
                 ("On lui fournit longtemps", "la miséricorde offerte.")], 0),
 "w07:158": (0, [("Les ascendeurs mortels", "aux sophismes de la rébellion."),
                 ("Mais nul citoyen ascendant", "plan d’ascension.")], 0),
 "w07:162": (0, [("« Aucun citoyen de Jérusem", "contre le péché.")], 0),
 "w07:178": (0, [("La folie de Lucifer", "univers expérientiel."),
                 ("En résumé, Lucifer", "mondes habités.")], 0),
 "w07:245": (0, [("Mais il est bon de clarifier une chose", "une chose :"),
                 ("vous pouvez vous fier", "d’atteindre Dieu.")], 0),
 "w07:263": (0, [("Sur Jérusem, les ascendeurs", "qu’ils sont seuls.")], 0),
 "w07:267": (0, [("Dans un univers dominé", "elle est certaine.")], 0),
 "w07:305": (0, [("Durant cet âge de lumière", "cet âge n’est pas parfait.")], 0),
 "w08:26": (0, [("Cette grande colonne", "du système solaire.")], 0),
 "w08:142": (0, [("Imaginez notre joie", "avec celui du jumeau."),
                 ("Environ un an plus tard", "reconnus comme tels.")], 0),
 "w08:160": (0, [("chaque jour, le couple", "l’eut atteint.")], 0),
 "w08:249": (0, [("Je ne comprenais pas alors", "orgueil de la personnalité.")], 0),
 "w08:253": (0, [("La présentation de cette ahurissante", "Souverain du Système de Satania")], 0),
 "w08:269": (0, [("Amadon est le héros", "assistant humain.")], 0),
 "w09:25": (0, [("Le site choisi pour le Jardin", "alors idéal."),
                ("L’élite de la civilisation", "point lumineux d’Urantia.")], 0),
 "w09:33": (0, [("ADAM ET ÈVE arrivèrent", "l’ère chrétienne"),
                ("Les Fils et Filles Matériels servent", "séparément leurs fonctions.")], 0),
 "w09:70": (0, [("Il y a lieu de souligner", "Caligastia et de Daligastia.")], 0),
 "w09:74": (0, [("les Melchizédeks, avant leur départ", "leurs entreprises communes.")], 0),
 "w09:110": (0, [("Il n’y a pas eu de", "biologique antérieure.")], 0),
 "w09:112": (0, [("Adam et Ève furent vraiment", "la race humaine fut élevée.")], 0),
 "w09:128": (0, [("Peu après leur réduction", "de les habiter.")], 0),
 "w09:132": (0, [("Ils avaient quitté Jérusem", "fils de l’homme.")], 0),
 "w09:136": (0, [("Ainsi se termine l’histoire", "assaillis par le mal.")], 0),
 "w09:140": (0, [("Ce n’est pas parce qu’Urantia", "Père du Paradis.")], 0),
 "w09:157": (0, [("Adam et Ève exercèrent", "nouvelle sur Urantia.")], 0),
 "w09:173": (0, [("Le mariage qui s’épanouit", "essentiellement humain")], 0),
 "w09:183": (0, [("Les différences de nature", "et collectivement.")], 0),
 "w09:185": (0, [("Les hommes et les femmes ont besoin", "carrière de mortel."),
                 ("Même dans Havona", "montée au Paradis.")], 0),
 "w09:222": (0, [("mais, pendant toute cette période", "aient pu être.")], 0),
 "w09:262": (0, [("Dieu répond à la prière", "expérience humaine")], 0),
 "w09:284": (0, [("C’est 1", "témoin de sa matérialisation."),
                 ("« Je suis Melchizédek", "seul et unique Dieu. »")], 0),
 "w09:298": (0, [("même cette courte et simple", "nés déchus par rapport aux dieux.")], 0),
}
out = {}
bad = []
for k, v in T.items():
    if k not in S: bad.append("no spec " + k); continue
    lead, pairs, trail = S[k]
    txt = v["verse"]; pos = 0; pieces = []
    for a, b in pairs:
        i = txt.find(a, pos)
        if i < 0: bad.append(f"{k}: start not found {a!r}"); break
        j = txt.find(b, i)
        if j < 0: bad.append(f"{k}: end not found {b!r}"); break
        pieces.append(txt[i:j + len(b)]); pos = j + len(b)
    s = f" {E} ".join(pieces)
    if lead: s = E + " " + s
    if trail: s = s + " " + E
    out[k] = s
for b in bad: print(b)
p = os.path.join(ROOT, "fr", "quotes_c02.json")
json.dump(out, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(out), "written")
