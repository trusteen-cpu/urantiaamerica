import sys,os,json
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0,r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools")
import amq
BASE=os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..')
Q={
"w12.009":"Esses pesquisadores chegam à conclusão espantosa de que o universo central e os sete superuniversos que o cercam estão, no presente, fazendo uso apenas de cerca de cinco por cento do funcionamento ativo da atração da gravidade absoluta do Paraíso.",
"w12.010":"onde já estamos sendo capazes de identificar agrupamentos de, pelo menos, setenta mil agregações de matéria, cada uma delas maior do que qualquer um dos superuniversos atuais.",
"w12.049":"O lapso relativo de tempo, do ponto de vista de Uversa, onde o litígio está pendente, poderia ser indicado, se disséssemos que o crime de Lúcifer foi levado a julgamento dois segundos e meio depois de cometido.",
"w12.109":"Mas, como agora o Supremo está presente, espiritual e pessoalmente, em Havona, do mesmo modo, o Último está presente ali, mas no sentido absonito e suprapessoal.",
"w12.111":"e agora o finalitor está face a face com o desafio de Deus, o Último.",
"w12.132":"A mente que é infinita ignora o tempo, a mente última transcende ao tempo, a mente cósmica é condicionada pelo tempo.",
"w12.150":"são onipessoais — eles existem antes da personalidade, eles são a personalidade, e existem após a personalidade.",
"w12.194":"enquanto a Trindade existencial do Paraíso é infinita, e enquanto a Ultimidade da Trindade experiencial é subinfinita, o Absoluto da Trindade não é tão fácil de se classificar.",
"w12.210":"o destino é consumado, provavelmente, por um ato do Consumador do Destino do Universo, e esse ato está, provavelmente, envolvido com o Supremo e o Último, no Absoluto da Trindade.",
"w13.027":"até onde sabemos, esses mundos estabelecidos em luz e vida estão destinados a prosseguir nas idades eternas em todo o tempo futuro.",
"w13.054":"Neste nível supracriador, a Deidade experiencia a exaustão do potencial personalizável, encontra Sua completude de divindade",
"w13.077":"e por isso cogitam de uma criação adicional e não revelada, que está além do quarto nível, o mais exterior do espaço, um universo possivelmente sempre em expansão, e sem fim, de infinitude.",
"w13.126":"Toda a realidade finita no tempo-espaço, sob o impulso diretivo do Ser Supremo em evolução, está empenhada em uma mobilização sempre-ascendente e em uma unificação perfeccionante (na síntese de poder-personalidade) entre todas as fases e valores da realidade finita",
"w13.147":"A evolução do poder da Supremacia do Todo-Poderoso, por meio de diversas sínteses de divindade, nos universos em evolução, factualizou-se em uma nova presença de poder da Deidade, que se coordenou com a pessoa espiritual do Supremo em Havona, por intermédio da Mente Suprema",
"w13.157":"Deus, o Supremo, é, por si próprio, um participante volitivo e criativo da sua própria realização na deidade.",
"w13.205":"Os filósofos dos universos postulam uma Trindade das Trindades, uma Trindade Infinita existencial-experiencial, mas não são capazes de visualizar a personalização dela",
"w13.226":"pois percebemos que a insondabilidade das relações cósmicas do Absoluto Universal tenderá a crescer, na proporção em que os universos materiais e a sua administração espiritual continuarem a expandir-se.",
"w13.231":"Esse é o momento estático hipotético da eternidade; os factuais estão ainda contidos dentro dos potenciais, e os potenciais ainda não apareceram dentro da infinitude do EU SOU.",
}
todo=json.load(open(os.path.join(BASE,'work','todo_pt_c07.json'),encoding='utf-8'))
assert set(todo)==set(Q),(set(todo)^set(Q))
for k,v in Q.items():
    print(k, amq.check('pt',todo[k]['cit'],v))
O={k:Q[k] for k in todo}
json.dump(O,open(os.path.join(BASE,'pt','quotes_c07.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('saved',len(O))
