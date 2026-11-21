import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
todo = json.load(open(os.path.join(BASE, 'work', 'todo_es_c08.json'), encoding='utf-8'))
Q = {
 '58.b13.q': 'vuestra vida amena en Urantia se debe a la influencia «fortuita» de más de dos veintenas de operaciones protectoras, aparentemente casuales, similares a la acción de esta capa de ozono única.',
 '58.b38.q': 'Resulta ser verdad al pie de la letra, como dijo vuestro poeta: «El polvo que pisamos estuvo otrora vivo.»',
 '59.b5.q': 'el mar protegía y nutría la vida primitiva del reino.',
 '61.b30.q': 'vuestros primeros antepasados nacieron y se procrearon en un medio ambiente estimulante, vigorizante y difícil.',
 '62.b5.q': 'Ésta es la primera decisión de la mente —del tipo humano de mente— en Urantia y automáticamente establece el circuito de comunicación',
 '62.b38.q': 'La evolución biológica nuevamente había conseguido los niveles humanos de dignidad volitiva; el hombre ya había llegado al planeta 606 de Satania.',
 '63.b5.q': 'la historia de la evolución, las luchas de la vida, la muerte y supervivencia eterna de los singulares padres de todo el género humano.',
}
assert set(Q) == set(todo)
for k, v in Q.items():
    for c in todo[k]['cit'].split('|'):
        if v.replace(' ', '') in todo[k]['verses'][c].replace(' ', ''):
            break
    else:
        raise SystemExit('not verbatim ' + k)
json.dump(Q, open(os.path.join(BASE, 'es', 'quotes_c08.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('quotes ok', len(Q))
