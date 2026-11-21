import json, os
BASE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
Q = {
 "w06.108": "Caso o terceiro membro da Trindade das Trindades seja concebido como sendo o Absoluto Universal, provavelmente isso irá representar um mínimo de distorção da verdade …",
 "w06.135": "… e ambos estão assim destinados à futura suprapersonalidade eterna de ministério transcendental dos reinos absonitos do Último, do Último-Supremo, até os níveis mesmo do Absoluto-Último.",
 "w06.142": "As Deidades do Paraíso alcançam esse nível, existencialmente, por meio da Trindade; mas esse terceiro nível de expressão unificadora da Deidade não está plenamente unificado experiencialmente.",
 "w06.150": "A improbabilidade de alcançar-se o destino infinito em nada impede que idéias sejam alimentadas sobre esse destino …",
 "w06.154": "A infinitude é preenchida pelo Infinito; o Infinito abrange a infinitude. Esse é o momento estático hipotético da eternidade …",
 "w07.050": "Esse é o momento estático hipotético da eternidade; os factuais estão ainda contidos dentro dos potenciais, e os potenciais ainda não apareceram dentro da infinitude do EU SOU. Mas, mesmo nessa situação de conjectura, devemos assumir que exista a possibilidade da vontade própria.",
}
json.dump(Q, open(os.path.join(BASE, 'pt', 'quotes_c04.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('ok')
