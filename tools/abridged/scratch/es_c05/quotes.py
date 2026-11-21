import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
Q = {
 "33.b18.q": "Esto es, en obra y en verdad, el alto ideal de la familia y de la institución humana del casamiento voluntario.",
 "34.b38.q": "en las horas sombrías, en cada encrucijada de la lucha por progresar, el Espíritu de la Verdad siempre hablará, diciendo: «Éste es el camino».",
 "36.b5.q": "el concepto es inherente al Padre, expresado en el Hijo, y la realización de la vida en el Espíritu.",
 "37.b17.q": "Indudablemente esto presagia la concentración futura de otras actividades de ascensión en el mundo del autootorgamiento de Micael y presta enorme y solemne importancia a la promesa personal del Maestro: «Volveré de nuevo».",
 "37.b28.q": "la clave del entero sistema de instrucción es: adquisición del carácter mediante la experiencia esclarecida.",
 "38.b14.q": "Hacéis bien en amarlos, pero no debéis adorarlos; los ángeles no son objetos de adoración.",
 "39.b40.q": "estos ministros espirituales de consumación seráfica, juntamente con los fieles espíritus ministrantes del tiempo, son por siempre y para siempre vuestros verdaderos amigos y asistentes infalibles.",
 "40.b22.q": "todas las almas de toda fase posible de la existencia mortal sobrevivirán, siempre y cuando manifiesten el deseo de cooperar con sus Ajustadores residentes y exhiban el impulso de hallar a Dios y de lograr la perfección divina",
 "40.b39.q": "El Padre ama a cada uno de sus hijos, y ese afecto es nada menos que verdadero, sagrado, divino, ilimitado, eterno y único",
}
todo = json.load(open('work/todo_es_c05.json', encoding='utf-8'))
assert set(todo) == set(Q)
for k, v in Q.items():
    vv = todo[k]['verses'][todo[k]['cit'].split('|')[0]]
    assert ''.join(v.split()) in ''.join(vv.split()), k
json.dump({k: Q[k] for k in todo}, open('es/quotes_c05.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
