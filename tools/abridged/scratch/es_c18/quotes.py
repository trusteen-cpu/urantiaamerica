import json, os
BASE = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
Q = {
"135.b5.q": "El debe aumentar, yo, disminuir.",
"135.b35.q": "Éste es mi hijo amado en quien tengo complacencia",
"136.b5.q": "Y en todos los demás asuntos, así como en estas decisiones ya registradas, te prometo que me someteré a la voluntad de mi Padre",
"136.b33.q": "venía para revelar su Padre celestial a sus hijos terrenales, mientras trataba de conducir a estos hijos para que con él hicieran el esfuerzo sincero de vivir haciendo la voluntad del Padre celestial.",
"137.b11.q": "Debéis aprender a buscar el secreto del nuevo reino en vuestro corazón y no en las colinas.",
"138.b17.q": "¿Es necesario recordaros que los sanos no necesitan de médico, sino más bien los que están enfermos? Yo he venido, no a llamar a los justos, sino a los pecadores",
"139.b19.q": "Hijitos míos, amaos los unos a los otros",
"140.b5.q": "este reino del que predicaréis es Dios dentro de vosotros.",
"140.b45.q": "Sí, Simón, todos los hombres son hijos de Dios, y ésa es la buena nueva que vais a proclamar",
"141.b5.q": "cuando la voluntad del Padre se hace verdaderamente vuestra voluntad, entonces estaréis vosotros en verdad en el reino",
"141.b25.q": "No hace falta que veáis las cosas de la misma manera ni que las sintáis de la misma manera ni tampoco que penséis de la misma manera para ser iguales espiritualmente.",
}
todo = json.load(open(os.path.join(BASE, 'work', 'todo_es_c18.json'), encoding='utf-8'))
assert set(todo) == set(Q), set(todo) ^ set(Q)
json.dump({k: Q[k] for k in todo}, open(os.path.join(BASE, 'es', 'quotes_c18.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('quotes', len(Q))
