import json, os
from common import BASE
Q = {
 "128.b26.q": "A casa de José nunca recebeu esmolas e nós não podemos comer o pão dos outros, enquanto eu tiver braços fortes e os meus irmãos puderem trabalhar",
 "130.b5.q": "nenhum homem é estranho para aquele que conhece a Deus.",
 "130.b38.q": "O teu problema não é que não consigas encontrar Deus, pois o Pai já te encontrou",
 "131.b38.q": "Deus não recompensa o homem pelo que ele faz, mas pelo que ele é",
 "131.b47.q": "Pois afinal tenho uma religião com um Deus, um Deus maravilhoso, e um Deus de salvação eterna",
 "134.b5.q": "A vontade do meu Pai no Paraíso seja feita",
}
todo = json.load(open(os.path.join(BASE, 'work', 'todo_pt_c17.json'), encoding='utf-8'))
assert set(todo) == set(Q)
json.dump(Q, open(os.path.join(BASE, 'pt', 'quotes_c17.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
