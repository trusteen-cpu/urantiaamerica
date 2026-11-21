import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
Q = {
 "43.b21.q": "Las puertas de los corazones de toda Edentia se cerraron contra Satán; fue rechazado unánimemente por los Soberanos de Sistema reunidos",
 "44.b37.q": "la verdadera alma de la expresión estará ausente a menos que estas realidades de la verdad, significados de la belleza, y valores de la bondad, estén unificados en la experiencia de vida del artesano, del científico o del filósofo.",
 "46.b5.q": "Y Jerusem no es sino el primer paso en el camino a la perfección excelsa de la belleza del Paraíso.",
 "47.b5.q": "Comienzas allí donde te interrumpes aquí.",
 "47.b28.q": "Un verdadero nacimiento de la conciencia cósmica toma lugar en el mundo de estancia número cinco",
 "48.b31.q": "Ninguna acción de bondad se pierde totalmente",
}
todo = json.load(open('work/todo_es_c06.json', encoding='utf-8'))
assert set(todo) == set(Q)
for k, v in Q.items():
    vv = todo[k]['verses'][todo[k]['cit'].split('|')[0]]
    assert ''.join(v.split()) in ''.join(vv.split()), k
json.dump({k: Q[k] for k in todo}, open('es/quotes_c06.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
