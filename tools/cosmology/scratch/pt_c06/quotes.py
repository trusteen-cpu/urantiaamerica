import json
Q = {
 "w10.022": "Essa ação constitui como que um título de posse física, um contrato cósmico de concessão;",
 "w10.082": "1. A Trindade Última, atualmente em evolução, consistirá, finalmente, no Ser Supremo, nas Personalidades Criadoras Supremas e nos Arquitetos absonitos do universo-mestre",
 "w10.136": "a Trindade Última experiencial coordena o transcendental, enquanto transcendental.",
 "w10.139": "A Trindade Última está unificando-se experiencialmente até completar-se",
 "w10.151": "elas não são somáveis — são associáveis, mas não totalizáveis.",
 "w10.186": "a mente nunca cessa de progredir — ela é a técnica experiencial do progresso sem fim.",
 "w10.196": "Esses seres alcançaram o limite atual da progressão espiritual, mas não a finalidade do último status do espírito.",
 "w10.202": "Será, indubitavelmente, função dos cidadãos evolucionários do grande universo compensar os habitantes dos espaços exteriores pelo fato de haverem sido privados do crescimento da Supremacia.",
 "w11.046": "Um Filho Criador não é limitado pelo tempo, mas é condicionado pelo espaço …",
 "w11.122": "De tempos em tempos, à medida que cresce o número de Conciliadores dos superuniversos, eles são transladados para o conselho de perfeição no Paraíso, do qual depois emergem como corporificações de coordenadores evolucionados por meio do Espírito Infinito, para o universo dos universos …",
 "w11.135": "… o universo dos universos é totalmente planejado pela mente, feito pela mente e administrado pela mente.",
 "w11.142": "Cada um desses planetas é uma criação original, única e exclusiva …",
 "w11.164": "Os arquitetos absonitos tornam possível o plano; os Criadores Supremos trazem-no à existência; o Ser Supremo consumará a sua plenitude …",
}
json.dump(Q, open("pt/quotes_c06.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(Q))
