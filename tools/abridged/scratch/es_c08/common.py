import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
SRC = json.load(open(os.path.join(BASE, 'work', 'src_c08.json'), encoding='utf-8'))
OUT = os.path.join(BASE, 'es', 'c08.json')

# section headings (official titles; dashes added where the English heading has them)
H = {
 '56': ['1. Coordinación Física', '2. Unidad Intelectual', '3. Unificación Espiritual', '4. Unificación de la Personalidad',
        '5. La Unidad de la Deidad', '6. La Unificación de la Deidad Evolucionaria', '7. Las Repercusiones Evolucionarias Universales',
        '8. El Unificador Supremo', '9. La Unidad del Absoluto Universal', '10. La Verdad, la Belleza y la Bondad'],
 '57': ['1. La Nebulosa Andronóver', '2. La Etapa Nebular Primaria', '3. La Etapa Nebular Secundaria', '4. Las Etapas Terciaria y Cuaternaria',
        '5. El Origen de Monmatia — El Sistema Solar de Urantia', '6. La Etapa de Sistema Solar — La Era de Formación Planetaria',
        '7. La Era Meteórica — La Edad Volcánica — La Atmósfera Planetaria Primitiva',
        '8. La Estabilización de la Corteza — La Edad de los Terremotos — El Océano Global y el Primer Continente'],
 '58': ['1. Requisitos Previos para la Vida Física', '2. La Atmósfera de Urantia', '3. El Medio Ambiente Espacial', '4. La Era en los Albores de la Vida',
        '5. El Desplazamiento Continental', '6. El Período de Transición', '7. El libro Geológico de la Historia'],
 '59': ['1. La Vida Marina Primitiva en los Mares de Poca Profundidad — La Edad de los Trilobites',
        '2. La Primera Etapa de la Inundación Continental — La Edad de los Animales Invertebrados',
        '3. La Segunda Etapa de Grandes Inundaciones — El Período del Coral — La Edad de los Braquiópodos',
        '4. La Etapa del Gran Surgimiento Terrestre — El Período de Vida Terrestre Vegetativa — La Edad de los Peces',
        '5. La Etapa del Desplazamiento de la Corteza — El Período Carbonífero de Bosques de Helechos — La Edad de las Ranas',
        '6. La Etapa de la Transición Climática — El Período de las Plantas de Semilla — La Edad de la Tribulación Biológica'],
 '60': ['1. La Edad Primitiva de los Reptiles', '2. El Fin de la Edad de los Reptiles',
        '3. La Etapa Cretácea — El Período de las Plantas Floríferas — La Edad de las Aves', '4. El Fin del Período de la Greda'],
 '61': ['1. La Nueva Etapa Terrestre Continental — La Edad de los Mamíferos Primitivos',
        '2. La Etapa Reciente de las Inundaciones — La Edad de los Mamíferos Avanzados',
        '3. La Etapa de las Montañas Modernas — La Edad del Elefante y del Caballo',
        '4. La Etapa Reciente de la Elevación Continental — La Última Gran Emigración de los Mamíferos',
        '5. La Edad Glacial Primitiva', '6. El Hombre Primitivo Durante la Edad Glacial', '7. La Continuación de la Edad Glacial'],
 '62': ['1. Los Primeros Tipos de Lémures', '2. Los Mamíferos Protohumanos', '3. Los Mamíferos Intermedios', '4. Los Primates',
        '5. Los Primeros Seres Humanos', '6. La Evolución de la Mente Humana', '7. El Reconocimiento como un Mundo Habitado'],
 '63': ['1. Andón y Fonta', '2. La Huida de los Gemelos', '3. La Familia de Andón', '4. Los Clanes Andónicos',
        '5. La Dispersión de los Andonitas', '6. Onagar — El Primer Maestro de la Verdad', '7. La Supervivencia de Andón y Fonta'],
}
TITLES = {'56': 'Unidad Universal', '57': 'El Origen de Urantia', '58': 'El Establecimiento de la Vida en Urantia',
          '59': 'La Era de la Vida Marina en Urantia', '60': 'Urantia Durante la Era Primitiva de la Vida Terrestre',
          '61': 'La Era de los Mamíferos en Urantia', '62': 'Las Razas Protohumanas del Hombre Primitivo', '63': 'La Primera Familia Humana'}

FIXED = {'Overview': 'Panorama general', 'The Paper': 'El documento', 'Conclusion': 'Conclusión'}


def auto(paper):
    """headings, title, summary table first column."""
    T = {}
    T[paper + '.title'] = TITLES[paper]
    n = 0
    for k, v in SRC.items():
        if k.split('.')[0] != paper:
            continue
        if k.endswith('.h'):
            if v in FIXED:
                T[k] = FIXED[v]
            elif v.startswith('Key Points of Paper'):
                T[k] = 'Puntos clave del documento ' + paper
            elif v[:1].isdigit():
                T[k] = H[paper][n]; n += 1
    return T


def summary(paper, key, msgs):
    src = SRC[key]
    assert len(src) == len(msgs) + 1, (key, len(src), len(msgs))
    rows = [['Sección', 'Mensaje clave']]
    for i, m in enumerate(msgs):
        rows.append([H[paper][i], m])
    return rows


def save(T):
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    D.update(T)
    for k in D:
        assert k in SRC, k
        assert type(D[k]) == type(SRC[k]), k
        if isinstance(SRC[k], list):
            assert len(D[k]) == len(SRC[k]), k
            for a, b in zip(D[k], SRC[k]):
                assert len(a) == len(b), (k, a)
    out = {k: D[k] for k in SRC if k in D}
    json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(out), '/', len(SRC))
