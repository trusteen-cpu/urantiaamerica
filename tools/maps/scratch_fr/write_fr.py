# -*- coding: utf-8 -*-
import json, os
T = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

maps = {
 "ui": {
  "site_title": "Cartes du Livre d’Urantia",
  "og_desc": "38 cartes qui suivent la vie de Jésus, de sa naissance aux apparitions morontielles",
  "sub": "De la naissance de Jésus aux apparitions morontielles — 38 cartes qui suivent ses pas",
  "search_ph": "Chercher un titre, un lieu, une année",
  "choose": "Choisir une carte",
  "prev": "Carte précédente",
  "next": "Carte suivante",
  "full": "Taille réelle",
  "print": "Imprimer",
  "map": "Carte",
  "sketch": "croquis de situation",
  "note": "Les noms de lieux, les dates et les itinéraires sont tirés du texte du Livre d’Urantia, avec ses propres graphies. Les itinéraires que le texte ne décrit pas sont en pointillé, et les petites zones, comme l’intérieur de Jérusalem, sont représentées par des croquis de situation. L’emplacement des villes est approximatif ; le relief de fond provient de Natural Earth (côtes et lacs actuels, domaine public).",
  "note_labels": "Les légendes des cartes sont en anglais, avec les graphies du texte anglais du Livre d’Urantia."
 },
 "maps": [
  ["La naissance de Jésus et la fuite en Égypte", "aout 7 av. J.-C. – octobre 4 av. J.-C."],
  ["Nazareth et ses environs pendant l’enfance", "3 av. J.-C. – 8 apr. J.-C."],
  ["Les villes galiléennes visitées avec son père", "1 av. J.-C. – 5 apr. J.-C."],
  ["Le premier voyage à Jérusalem", "4–7 avril 7 apr. J.-C."],
  ["Jérusalem et le temple", "avril 7 apr. J.-C., sa première Pâque"],
  ["L’ancienne Nazareth et la maison de Jésus", "4 av. J.-C. – vers 28 apr. J.-C."],
  ["La Pâque avec Jacques", "printemps 12 apr. J.-C."],
  ["La troisième visite de la Pâque à Jérusalem", "printemps 14 apr. J.-C."],
  ["La quatrième visite de la Pâque — avec son frère Joseph", "printemps 15 apr. J.-C."],
  ["La cinquième visite de la Pâque — avec son frère Simon", "printemps 17 apr. J.-C."],
  ["La sixième visite de la Pâque — avec son frère Jude", "printemps 19 apr. J.-C."],
  ["L’atelier de bateaux de Zébédée et Jérusalem", "janvier 21 apr. J.-C. – avril 22 apr. J.-C."],
  ["Le voyage à Rome, en Grèce et en Mésopotamie", "avril 22 apr. J.-C. – décembre 23 apr. J.-C."],
  ["Le lac Urmia et le voyage en caravane vers la mer Caspienne", "avril 24 apr. J.-C. – avril 25 apr. J.-C."],
  ["La Syrie et la côte méditerranéenne", "avril – été 25 apr. J.-C."],
  ["À travers la Palestine jusqu’au mont Hermon", "été 25 apr. J.-C."],
  ["Du mont Hermon à Jérusalem, puis retour en Galilée", "fin de l’été 25 apr. J.-C. – janvier 26 apr. J.-C."],
  ["Le baptême près de Pella et les quarante jours dans les collines de Pérée", "13 janvier – 23 février 26 apr. J.-C."],
  ["De Pella à Cana et Bethsaïde, en passant par Nazareth", "24 février – 2 mars 26 apr. J.-C."],
  ["L’appel et l’ordination des apôtres — Bethsaïde et la mer de Galilée", "février 26 apr. J.-C. – janvier 27 apr. J.-C."],
  ["Le long de la vallée du Jourdain jusqu’en Judée", "janvier – avril 27 apr. J.-C."],
  ["Premier travail avec les apôtres — Judée, Samarie et Décapole", "avril 27 apr. J.-C. – janvier 28 apr. J.-C."],
  ["La première tournée de prédication publique en Galilée", "janvier – mars 28 apr. J.-C."],
  ["Le voyage de la Pâque à Jérusalem", "mars – mai 28 apr. J.-C."],
  ["Le camp de Zébédée et la deuxième tournée de prédication en Galilée", "mai – décembre 28 apr. J.-C."],
  ["La troisième tournée de prédication et la visite à Nazareth", "janvier – mars 29 apr. J.-C."],
  ["La montée à Jérusalem, puis vers le nord", "mars – juin 29 apr. J.-C."],
  ["De Sidon le long de la côte, et jusqu’au parc de Magadan", "juin – aout 29 apr. J.-C."],
  ["La transfiguration sur le mont Hermon et la tournée de la Décapole", "aout – septembre 29 apr. J.-C."],
  ["Le quartier général transféré à Pella, et les visites à Jérusalem", "septembre – décembre 29 apr. J.-C."],
  ["La tournée de Pérée, et à Béthanie pour ressusciter Lazare", "janvier – mars 30 apr. J.-C."],
  ["Du camp de Pella à Jérusalem", "mars – 2 avril 30 apr. J.-C."],
  ["De Béthanie au temple et au camp de Gethsémani", "3–5 avril 30 apr. J.-C."],
  ["Le camp de Gethsémani et la chambre du haut", "jeudi 6 avril 30 apr. J.-C."],
  ["De l’arrestation à Gethsémani au procès devant Pilate", "nuit du 6 avril – matin du 7 avril 30 apr. J.-C."],
  ["Du prétoire au Golgotha", "vendredi 7 avril 30 apr. J.-C."],
  ["Le jour de la résurrection : apparitions à Jérusalem et à Béthanie", "dimanche 9 avril 30 apr. J.-C."],
  ["Les apparitions morontielles, de la dixième à la dix-neuvième", "11 avril – 18 mai 30 apr. J.-C."],
 ],
}

reading = {
 "index": {
  "title": "Lire le Livre d’Urantia en un an",
  "sub": "De l’Introduction au Fascicule 196, dans l’ordre — cochez ce que vous avez lu et la date est enregistrée",
  "start": "Date de début",
  "goal": "Objectif",
  "g260": "1 an · 5 jours par semaine (260 jours)",
  "g365": "1 an · tous les jours (365 jours)",
  "g182": "6 mois (182 jours)",
  "next": "Aller à la prochaine lecture ▶",
  "c1": "Achevé",
  "c2": "Sections lues",
  "c4": "Jours restants",
  "ahead": "En avance sur le plan",
  "behind": "En retard sur le plan",
  "onpace": "Conforme au plan",
  "notyet": "Pas encore commencé",
  "fore": "Introduction",
  "parts": ["Introduction", "Partie I", "Partie II", "Partie III", "Partie IV"],
  "intro": "Préambule",
  "quotes": "Passages mémorables",
  "qph": "Écrivez le passage",
  "add": "Ajouter",
  "memo": "Notes personnelles",
  "mph": "Écrivez vos réflexions sur ce fascicule",
  "saved": "Enregistré",
  "dbtn": "📔 Journal quotidien du Livre d’Urantia",
  "graph": "Progression",
  "l1": "Ma progression",
  "l2": "Objectif (plan)",
  "export": "Exporter (enregistrer dans un fichier)",
  "import": "Importer",
  "reset": "Tout effacer",
  "store": "Votre suivi est enregistré dans ce navigateur, sur cet appareil. Exportez-le de temps en temps dans un fichier pour le transférer ou le mettre en sécurité.",
  "resetQ": "Effacer toutes les coches, tous les passages et toutes les notes ? Cette action est irréversible.",
  "editDate": "Date de lecture (par ex. 2026-10-30). Laissez vide pour décocher.",
  "st_ahead1": "Vous avez {d} jour d’avance sur le plan.",
  "st_ahead": "Vous avez {d} jours d’avance sur le plan.",
  "st_behind1": "Vous avez {d} jour de retard. Lire jusqu’à {p} % aujourd’hui vous remet à jour.",
  "st_behind": "Vous avez {d} jours de retard. Lire jusqu’à {p} % aujourd’hui vous remet à jour.",
  "st_on": "Vous suivez le plan.",
  "day1": "{n} jour",
  "days": "{n} jours",
  "today_graph": "aujourd’hui",
 },
 "diary": {
  "title": "📔 Journal quotidien du Livre d’Urantia",
  "prev": "◀ Jour précédent",
  "next": "Jour suivant ▶",
  "today": "Aujourd’hui",
  "verse": "✦ Passage du jour",
  "other": "Un autre passage ↻",
  "think": "✎ Évènements et réflexions du jour",
  "ph": "Écrivez ce qui s’est passé dans votre journée",
  "saved": "Enregistré",
  "past": "Entrées précédentes",
  "hint": "Votre journal est enregistré dans ce navigateur. Il est inclus dans le fichier d’exportation de la page Lire le Livre d’Urantia en un an.",
 },
}

for rel, D in (("maps/strings_fr.json", maps), ("reading/strings_fr.json", reading)):
    p = os.path.join(T, rel)
    old = json.load(open(p, encoding="utf-8"))
    def shape(x):
        if isinstance(x, dict): return {k: shape(v) for k, v in x.items()}
        if isinstance(x, list): return [shape(v) for v in x]
        return 0
    assert shape(old) == shape(D) and list(old) == list(D), rel
    for k in old:
        if isinstance(old[k], dict): assert list(old[k]) == list(D[k]), (rel, k)
    json.dump(D, open(p, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print("wrote", rel)
