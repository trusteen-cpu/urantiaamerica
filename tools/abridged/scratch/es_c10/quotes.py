# -*- coding: utf-8 -*-
import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
Q = {
 "71.b35.q": "La educaci\u00f3n es la tarea de la vida; ha de continuar toda la vida",
 "72.b5.q": "Se han civilizado hasta tal punto que pueden defender vigorosamente la civilizaci\u00f3n",
 "73.b5.q": "Ed\u00e9n era el \u00fanico punto risue\u00f1o en Urantia",
 "73.b19.q": "M\u00e1s all\u00e1 de sus confines, el mundo estaba sumido en la oscuridad, la ignorancia y el salvajismo. Ed\u00e9n era el \u00fanico punto risue\u00f1o en Urantia",
 "73.b35.q": "habr\u00edan de movilizarse para la otorgaci\u00f3n altruista a las razas necesitadas de la tierra.",
 "75.b22.q": "constituy\u00f3 un acto del mal porque representaba el camino errado para lograr fines justos, porque se desvi\u00f3 del camino acertado, el designio divino.",
 "76.b27.q": "ser\u00e9is llamados del abrazo del sue\u00f1o mortal, al llegar yo a Urantia, si los Hijos subordinados de mi reino no os llaman antes de este momento",
}
todo = json.load(open('work/todo_es_c10.json', encoding='utf-8'))
assert set(todo) == set(Q)
for k, v in Q.items():
    vv = todo[k]['verses'][todo[k]['cit'].split('|')[0]]
    assert ''.join(v.split()) in ''.join(vv.split()), k
json.dump({k: Q[k] for k in todo}, open('es/quotes_c10.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
