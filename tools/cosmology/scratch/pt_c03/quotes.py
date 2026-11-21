import json, os
BASE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(BASE, "..", ".."))
Q = {
 "w04.027": "Eles alcançaram o limite atual da perfeição da criatura, mas não a finalidade do serviço da criatura. Eles experienciaram a plenitude da adoração da Deidade, mas não a finalidade da realização da Deidade experiencial.",
 "w04.046": "…onde já estamos sendo capazes de identificar agrupamentos de, pelo menos, setenta mil agregações de matéria, cada uma delas maior do que qualquer um dos superuniversos atuais.",
 "w04.107": "Em outras palavras: no presente momento, cerca de noventa e cinco por cento da ação de gravidade cósmica ativa da Ilha do Paraíso, computados nessa teoria da totalidade, estão empenhados em controlar os sistemas materiais que se situam além das fronteiras dos universos organizados atualmente.",
 "w04.134": "…encaramos o universo-mestre como tendo limitações e sendo definitivamente delimitado e contido, nas suas margens externas, pelo espaço aberto.",
 "w05.040": "…o destino é consumado, provavelmente, por um ato do Consumador do Destino do Universo, e esse ato está, provavelmente, envolvido com o Supremo e o Último, no Absoluto da Trindade.",
 "w05.042": "A Trindade Última, atualmente em evolução, consistirá, finalmente, no Ser Supremo, nas Personalidades Criadoras Supremas e nos Arquitetos absonitos do universo-mestre…",
 "w05.045": "Entretanto, estamos certos quanto ao seguinte: enquanto a Trindade existencial do Paraíso é infinita, e enquanto a Ultimidade da Trindade experiencial é subinfinita, o Absoluto da Trindade não é tão fácil de se classificar.",
 "w05.086": "Entre todos os que ascendem à Ilha Eterna, apenas aqueles que chegam lá desse modo são filhos da eternidade…",
 "w05.099": "…mas à medida que o homem ascende e progride interiormente, a visão amplificada dessa sucessão de eventos é tal que ele pode discerni-la, cada vez mais, na sua totalidade.",
 "w05.120": "Ao admitirmos um cosmo infinito — algum cosmo ilimitado ultrapassando o universo-mestre — e se concebermos que os desenvolvimentos finais do Absoluto da Trindade acontecerão em um tal estágio superúltimo de ação…",
 "w05.164": "Essas três Deidades experienciais eram potenciais, na Trindade existencial, a Trindade do Paraíso, mas os seus surgimentos no universo, como personalidades de poder, dependem, em parte, dos seus próprios funcionamentos experienciais, nos universos do poder e da personalidade…",
 "w05.166": "…como é ilustrado pela síntese de poder-personalidade ora encaminhando-se junto com a evolução do Ser Supremo.",
 "w05.175": "Neste nível supracriador, a Deidade experiencia a exaustão do potencial personalizável, encontra Sua completude de divindade…",
 "w05.179": "A Trindade Última está unificando-se experiencialmente até completar-se, mas duvidamos verdadeiramente da possibilidade dessa unificação plena da Trindade Absoluta. O nosso conceito, contudo, da eterna Trindade do Paraíso, é mantido como uma lembrança, sempre presente, de que a trinitarização da Deidade pode realizar aquilo que, de outro modo, seria inatingível…",
}
todo = json.load(open(os.path.join(ROOT, "work", "todo_pt_c03.json"), encoding="utf-8"))
assert set(Q) == set(todo), set(todo) ^ set(Q)
json.dump({k: Q[k] for k in todo}, open(os.path.join(ROOT, "pt", "quotes_c03.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("quotes saved", len(Q))
