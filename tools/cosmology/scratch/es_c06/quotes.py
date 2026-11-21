import json, os
H = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Q = {
 "w10.082": "1. La Trinidad Última, presentemente en evolución, finalmente consistirá en el Ser Supremo, las Personalidades Supremas Creadoras y los Arquitectos absonitos del Universo Maestro",
 "w10.099": "La Trinidad es una realidad de Deidad supersumativa que se eventúa de la conjunción de las tres Deidades del Paraíso.",
 "w10.136": "la Trinidad Última experiencial coordina lo trascendental como trascendental.",
 "w10.139": "La Trinidad Última se está unificando experiencialmente en cumplimiento",
 "w10.151": "no son sumables —son asociables pero no totalizables.",
 "w10.186": "la mente no cesa jamás de progresar —es la técnica experiencial del progreso sin fin.",
 "w11.046": "Un Hijo Creador no está impedido por el tiempo, pero está condicionado por el espacio. …",
 "w11.122": "De cuando en cuando, a medida que el número de conciliadores superuniversales aumenta, se los traslada al concilio de perfección en el Paraíso, del cual posteriormente emergen como cuerpo de coordinación evolucionado por el Espíritu Infinito para el universo de los universos …",
 "w11.135": "… el universo de los universos in toto está planificado por la mente, hecho por la mente, y administrado por la mente.",
 "w11.142": "Cada uno de estos planetas es una creación original, única y exclusiva …",
 "w11.164": "Los arquitectos absonitos eventúan el plan; los Creadores Supremos lo traen en la existencia; el Ser Supremo consumará su plenitud …",
}
json.dump(Q, open(os.path.join(H, "es", "quotes_c06.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(Q))
