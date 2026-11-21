import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
Q = {
 "50.b35.q": "agondonters, lo cual significa criaturas volitivas evolucionarias que pueden creer sin ver, perseverar cuando están aisladas, y triunfar sobre dificultades insuperables aun cuando están a solas.",
 "51.b5.q": "En estos Hijos e Hijas Materiales inmortales hallamos el último e indispensable eslabón que conecta a Dios con el hombre",
 "51.b35.q": "Y si los urantianos pudiesen tan sólo observar la vida en tal planeta, apreciarían inmediatamente el valor de aquellas cosas que su mundo ha perdido al involucrarse en el mal y participar en la rebelión.",
 "52.b25.q": "su vida es una encarnación de la verdad paradisiaca en la carne mortal, esa misma verdad —aún el Espíritu de la Verdad— por cuyo conocimiento los hombres serán libres.",
 "52.b34.q": "tarde o temprano, la gracia de Dios y el ministerio de los ángeles inaugurarán el día del advenimiento de los Hijos Instructores Trinitarios; y su partida, después de su misión final, inaugurará esta maravillosa era de luz y vida.",
 "53.b5.q": "la fe es una armadura eficaz contra el pecado y la iniquidad.",
 "53.b21.q": "gobierno de los Hijos en nombre del Padre tan sólo deseaba lealtad y devoción voluntarias, sinceras y a prueba de sofismas",
 "54.b30.q": "Ninguna de estas consecuencias relacionadas de la mala conducta en el grupo puede poner jamás en peligro tu futuro eterno ni privarte en lo más mínimo de tu derecho divino a la ascensión al Paraíso y al logro de Dios.",
}
V = json.load(open('../data/es.json', encoding='utf-8'))
T = json.load(open('work/todo_es_c07.json', encoding='utf-8'))
for k, v in Q.items():
    vs = T[k]['cit'].split('|')
    ok = any(v.replace(' ', '') in V[r].replace(' ', '') for r in vs)
    print(k, ok)
json.dump(Q, open('es/quotes_c07.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
