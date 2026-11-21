# -*- coding: utf-8 -*-
import json, os
H = r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\cosmology"
SRC = json.load(open(os.path.join(H, "work", "src_c01.json"), encoding="utf-8"))
OUT = os.path.join(H, "pt", "c01.json")
D = json.load(open(OUT, encoding="utf-8")) if os.path.exists(OUT) else {}

T = {
"w01.169": "5. A Trindade como tese eterna (orig., pp. 19–20)",
"w01.170": "A tese existencial da perfeição",
"w01.171": "Tomadas em conjunto, a Trindade e a Havona perfeita mostram-nos a perfeição como tese existencial. Havona dá forma factual ao que era potencial no Paraíso. Da Trindade, e das Deidades pessoais que residem no Paraíso, brotam os ideais da perfeição divina, e esses ideais são aquilo a que todo crescimento evolucionário visa finalmente em todos os níveis abaixo do absoluto, a saber, o finito e o absonito. Quando Havona reaparecer no Capítulo 5 como a “tese da perfeição”, será como uma extensão deste relato.",
"w01.172": "Três níveis de realidade",
"w01.173": "Sadler expõe aqui três níveis de realidade. A realidade **finita** é a realidade de tempo e espaço que nos é familiar. A realidade finita pós-Havona é experiencial e tem uma origem no tempo; pode continuar no futuro eterno, mas não existiu desde o passado eterno. A realidade **absonita** é um conceito introduzido pela primeira vez por O Livro de Urântia, uma “realidade intermediária” entre o finito e o absoluto. É também chamada transcendental: transcende o tempo e o espaço sem ignorá-los. A realidade **absoluta** é sem tempo e sem espaço. O tempo e o espaço nem sequer entram na consciência dos Absolutos.",
"w01.175": "Como exemplo de ausência de tempo, Sadler aponta o Ajustador que havia residido em Jesus. Esse Ajustador, agora personalizado, explicou a Jesus que as hostes sob o seu comando podiam ser limitadas no espaço, mas não no tempo.",
"w01.177": "A realidade absoluta é existencial e eterna, embora certas realidades absolutas tenham também um lado experiencial. Sadler cita o Absoluto da Deidade como exemplo de uma realidade ao mesmo tempo existencial e experiencial.",
"w01.178": "A Trindade em ação nos três níveis",
"w01.179": "A Trindade do Paraíso parece funcionar em todos esses três níveis e iniciar atividade em cada um deles. As personalidades que dão início a todo o processo evolucionário originam-se na Trindade, assim como a administração do universo central e dos superuniversos. Embora o Pai e o Filho tenham dado origem à criação central por meio do Espírito, as três Deidades são, na prática, a fonte de Havona, e por isso Sadler chama Havona de “criação” de origem trinitária.",
"w01.180": "6. A singularidade de Havona (orig., pp. 20–21)",
"w01.181": "Um universo que desafia a classificação",
"w01.182": "O último item do inventário da realidade existencial e eterna é Havona, o universo central e divino. Sadler considera Havona a região mais fascinante de todo o universo-mestre, precisamente porque é tão singular que resiste à classificação.",
"w01.183": "Havona nunca foi de fato criada. Para fins práticos, porém, chamamo-la de “criação central”, e na presente segunda idade ela funciona como uma verdadeira criação. Durante a primeira idade, Havona existia em completa solidão. Além dela não havia nada senão espaço vazio, de modo que não tinha relações exteriores; tinha apenas as suas relações internas e a sua relação interior com o Paraíso.",
"w01.185": "Havona é difícil de classificar também segundo o nível funcional de realidade. Não é finita, nem absonita, nem absoluta. Em Havona, seres vivem e acontecimentos ocorrem nos três níveis funcionais. Havona é uma criação incriada, e os seres que ali vivem também nunca foram criados. No espaço ela é finita: tem exatamente o tamanho que tem e nada mais. Contudo, quando se considera o que acontece nos seus um bilhão de mundos perfeitos, ela ultrapassa em muito o finito.",
"w01.186": "O universo modelo",
"w01.187": "Sadler resume Havona como um universo que contém “um pouco de tudo”. Havona é o universo modelo que Deus fez, e bem pode servir de modelo para todo universo local, para os superuniversos, para o universo-mestre como um todo e até para qualquer coisa que possa surgir além da criação-mestra. Esta última sugestão é especulação do próprio Sadler.",
"w01.188": "Em linhas simples, Havona está organizada assim. No centro fica a Ilha do Paraíso. Entre a Ilha e Havona propriamente dita giram três circuitos de sete mundos cada, pertencentes ao Pai, ao Filho e ao Espírito. Além deles, um bilhão de mundos giram em sete circuitos planetários.",
"w01.190": "Diagrama simplificado do universo central: o Paraíso, os três circuitos de vinte e um satélites e os sete circuitos de um bilhão de mundos",
"w01.191": "7. Os Arquitetos do Universo-Mestre (orig., p. 22)",
"w01.192": "Seres que emergiram, não criados",
"w01.193": "Antes de deixar a primeira idade, Sadler apresenta um grupo singular, os Arquitetos do Universo-Mestre. Eles não foram criados; “emergiram”. A emergência tem um sentido especial em O Livro de Urântia. Como a criação, designa um modo pelo qual um ser vem a existir, mas não é criação. Significa algum ato iniciador de status pré-temporal, pré-criativo ou de eternidade. Os Transcendentores, que são seres absonitos, não são criados, mas emergem.",
"w01.195": "Sadler está convencido de que os Arquitetos Mestres já existiam e funcionavam na primeira idade. Ele deixa aberta a possibilidade de que tenham existido ainda antes, na Idade Zero. Sobre o mais elevado deles, o Arquiteto sênior, O Livro de Urântia diz:",
"w01.197": "Plantas vivas",
"w01.198": "Os Arquitetos Mestres são seres absonitos, nem finitos nem absolutos; pertencem aos Transcendentores. Não são nem criadores nem criaturas. Sadler considera-os algo próximo das plantas vivas e inteligentes do universo-mestre, seres que personalizam o plano de Deus para toda a criação-mestra.",
"w01.200": "Eles começam o seu trabalho na criação pós-Havona antes de qualquer outro, preparando o palco espacial para novos desenvolvimentos. Esse trabalho está em andamento muito antes de aparecerem os criadores e os administradores dos universos pós-Havona. Estão organizados em sete corpos, correspondendo ao desenho geográfico do cosmo: a Ilha central do Paraíso e os seis níveis espaciais concêntricos.",
"w01.201": "Sadler e o texto",
"w01.202": "A afirmação em 31:9.3 de que o Arquiteto sênior emergiu “no alvorecer da eternidade” apoia a conjectura de Sadler de que os Arquitetos podem ter existido antes da primeira idade. A mesma expressão aparece em 8:0.2, onde marca o momento em que o Pai e o Filho entram no seu pacto eterno, o acontecimento ligado ao aparecimento do Espírito Infinito. Este comentário lê as duas passagens como referentes ao mesmo ponto. Sadler também faz corresponder os sete corpos ao Paraíso e aos seis níveis espaciais, o que concorda com 31:9, onde os Arquitetos Mestres estão distribuídos por sete níveis: o Paraíso, Havona, os superuniversos e os quatro níveis do espaço exterior.",
"w01.203": "A Primeira Idade do Universo é a idade de Havona, e Havona é uma existência eterna que nunca foi criada.",
"w01.204": "No final da Idade Zero, apenas o Pai, o Filho e o Paraíso eram factuais; uma única trinitarização das duas Deidades deu origem ao Espírito Infinito, a Havona e à Trindade do Paraíso.",
"w01.205": "Sadler divide os Sete Absolutos da Infinitude em absoluto primordial (o Pai), absoluto factual (Filho, Paraíso, Espírito) e absoluto potencial (os Absolutos da Deidade, Inqualificável e Universal), e vê todo crescimento como a passagem do potencial ao factual.",
"w01.206": "A Trindade não é três pessoas, mas uma entidade semelhante a uma sociedade anônima formada por elas; a sua função, a administração da justiça, é distinta do amor, da misericórdia e da ministração das pessoas.",
"w01.207": "Por meio da Trindade, Deus preserva a unidade da Deidade enquanto escapa, como pessoa, das limitações da infinitude.",
"w01.208": "A Trindade e Havona formam a tese existencial da perfeição; Havona é um universo modelo que não pode ser atribuído a um único nível, finito, absonito ou absoluto.",
"w01.209": "Os Arquitetos do Universo-Mestre são seres absonitos, que emergiram em vez de serem criados, e que desde a primeira idade preparam o palco espacial em sete corpos.",
"w01.210": "O universo-mestre como palco",
"w01.211": "Guia de *A Study of the Master Universe* (p. 23) · Introdução (pp. 25–29)",
"w01.212": "Terminado o prólogo, Sadler prepara o palco antes de entrar no corpo principal. Ele esclarece as diferentes maneiras pelas quais O Livro de Urântia usa a palavra “universo” e propõe ver o universo-mestre por meio de um esquema de seis níveis espaciais concêntricos e de seis idades do universo correspondentes. Formula depois sete grupos de perguntas, que abrangem o tamanho dos níveis espaciais, a duração das idades do universo, o crescimento da Deidade experiencial, o futuro dos finalitores mortais, o que pode haver além do universo-mestre e outras questões, e convida o leitor a começar a investigação com humildade e coragem.",
"w01.213": "1. Um guia para as três histórias (orig., p. 23)",
"w01.214": "Na abertura do corpo principal, Sadler condensa todo o estudo numa única frase. É a história da extensão criativa e evolucionária da divindade do Paraíso-Havona no tempo e no espaço, uma extensão consolidada no Supremo, no nível finito, e no Último, no nível absonito. Ela também começa, sem terminar, a história que continua além do Último.",
"w01.215": "O corpo principal está, portanto, organizado em três partes: “A História Finita”, “A História Absonita” e “O Início da História Final”. O estudo propriamente dito começa quando a idade de Havona do passado eterno dá lugar a uma idade com uma origem no tempo, a segunda idade, na qual vivemos. E terminará pouco depois que a idade final do universo-mestre tiver completado o seu curso no tempo e der lugar à idade do futuro eterno.",
"w01.216": "2. Os muitos usos da palavra “universo” (orig., pp. 25–26)",
"w01.217": "O que é o universo-mestre?",
"w01.218": "Sadler abre a sua introdução com perguntas. O que é, realmente, o universo-mestre? Quando O Livro de Urântia usa o termo, quanto do seu significado captamos? Sabemos como o propósito de Deus se desdobra dentro do universo-mestre, ou qual pode ser o propósito do próprio universo-mestre?",
"w01.219": "Primeiro é preciso pôr em ordem o vocabulário. O Livro de Urântia usa a palavra “universo” de vários modos: universo local, superuniverso, universo central, grande universo e universo-mestre. Havona é o universo central, a criação que fica mais perto em torno do Paraíso. O próprio Paraíso, observa Sadler, não pertence a universo algum; é o centro absoluto de todas as coisas materiais e é, ele próprio, sem movimento.",
"w01.221": "Havona é rodeada por sete superuniversos, o sétimo dos quais é o nosso próprio superuniverso, Orvonton. Cada superuniverso está destinado a conter exatamente cem mil universos locais, e o nosso universo local chama-se Nébadon.",
"w01.222": "O grande universo e o universo-mestre",
"w01.223": "Quando se refere ao universo central e aos sete superuniversos em conjunto, O Livro de Urântia usa o nome “grande universo”. O grande universo é a criação agora organizada e habitada, em contraste com as regiões não organizadas e não habitadas do espaço além dela, os quatro níveis do espaço exterior. O grande universo, junto com esses quatro níveis do espaço exterior, forma o “universo-mestre”.",
"w01.225": "Quando Sadler quer referir-se apenas aos quatro níveis do espaço exterior, fala dos “universos exteriores”. A expressão de O Livro de Urântia “universo dos universos” não é definida com rigor; refere-se de modo geral ao grande universo, às vezes incluindo os níveis do espaço exterior e às vezes não.",
"w01.226": "Os seis níveis espaciais concêntricos do universo-mestre e as idades do universo correspondentes (novo diagrama simplificado, fora de escala)",
"w01.227": "3. Seis níveis espaciais e seis idades do universo (orig., p. 27)",
"w01.228": "Seis elipses concêntricas",
"w01.229": "Sadler considera que a melhor descrição geral do universo-mestre é a do documento 12, seção 1, “Níveis Espaciais do Universo-mestre”. Ali a criação-mestra é representada como seis níveis espaciais elípticos concêntricos.",
"w01.231": "Cada nível espacial tem dois nomes, usados quase indistintamente; o primeiro nível do espaço exterior, por exemplo, também se chama Nível Espacial Primário. A Introdução de O Livro de Urântia menciona esses nomes em conexão com o futuro de Deus, o Sétuplo.",
"w01.233": "Fazendo corresponder idades e níveis espaciais",
"w01.234": "Outro conceito que Sadler aproveita bem é o de seis idades do universo sucessivas. Ele lê O Livro de Urântia como ligando cada idade do universo ao período em que um novo nível espacial é aberto e desenvolvido. Os níveis espaciais e as idades do universo correspondem assim um a um.",
"w01.235": "Os seis níveis espaciais e as seis idades do universo-mestre",
"w01.236": ["Ordem", "Nível espacial", "Outro nome", "Idade do universo correspondente"],
"w01.237": ["1", "Nível espacial de Havona", "Universo central", "Primeira Idade do Universo"],
"w01.238": ["2", "Nível espacial dos superuniversos", "Sete superuniversos", "Segunda Idade do Universo (atual)"],
"w01.239": ["3", "Primeiro nível do espaço exterior", "Nível Espacial Primário", "Terceira Idade do Universo"],
"w01.240": ["4", "Segundo nível do espaço exterior", "Nível Espacial Secundário", "Quarta Idade do Universo"],
"w01.241": ["5", "Terceiro nível do espaço exterior", "Nível Espacial Terciário", "Quinta Idade do Universo"],
"w01.242": ["6", "Quarto nível do espaço exterior", "Nível Espacial Quaternário", "Sexta Idade do Universo"],
"w01.243": "Seguindo esse esquema, Sadler propõe acompanhar o crescimento do universo-mestre com atenção cuidadosa à sequência dos acontecimentos. O seu objetivo é ver como as idades do universo acompanham o passo da extensão, para fora, da criatividade e das personalidades do Paraíso através dos níveis espaciais concêntricos. O Livro de Urântia afirma que esses níveis espaciais são destinados a criações de caráter diferente.",
"w01.245": "Sadler e o texto: o esquema das “seis idades do universo”",
"w01.246": "O Livro de Urântia fala muitas vezes da “presente idade do universo”, das “idades futuras do universo” e da “idade dos universos exteriores”, mas em parte alguma oferece uma lista numerada de seis idades emparelhadas uma a uma com os níveis espaciais. A correspondência na tabela acima é um esquema que Sadler construiu reunindo afirmações dispersas. Nomes como “Primeira Idade do Universo” e “Terceira Idade do Universo” devem, portanto, ser lidos em grande parte como terminologia de Sadler. Ainda assim, como o texto distingue Havona como a criação da eternidade, os superuniversos como as criações do tempo e os níveis do espaço exterior como futuras criações da ultimidade, a sua ideia básica de que os níveis espaciais se abrem em ordem, de dentro para fora, ajusta-se bem ao texto.",
"w01.247": "4. A forma da investigação e sete perguntas (orig., pp. 28–29)",
"w01.248": "Interpolação e extrapolação",
"w01.249": "Sadler reafirma a intenção do seu estudo: examinar cuidadosamente o universo-mestre e ver o que se pode aprender sobre o propósito de Deus. Se reunirmos tudo o que O Livro de Urântia diz sobre a criação-mestra, os seus níveis espaciais e as suas idades do universo, e depois preenchermos as lacunas entre esses dados (interpolação) e os estendermos além do seu alcance (extrapolação), poderemos chegar a compreender um pouco melhor o plano de Deus para a criação-mestra e para os criadores e as criaturas dos seus vastos domínios.",
"w01.250": "Sete grupos de perguntas",
"w01.251": "Ele expõe em sete grupos as perguntas que o estudo examinará. Elas servem de sumário para todo o livro e voltam no capítulo de conclusão.",
"w01.252": "Qual é o tamanho dos níveis espaciais? Qual é o tamanho dos níveis do espaço exterior em comparação com o grande universo, e qual é o tamanho do universo-mestre como um todo?",
"w01.253": "Qual é a duração das idades do universo? Elas diferem em duração? As idades relacionam-se de outros modos além da mera sequência? Diferem apenas em duração, ou também em qualidade?",
"w01.254": "Como o crescimento da Deidade experiencial está ligado às idades do universo? Como está relacionado com os níveis espaciais em expansão? Como o desenvolvimento das duas Trindades experienciais corresponde às idades e aos níveis espaciais?",
"w01.255": "Ao longo das idades sucessivas e do palco cada vez mais amplo do espaço, que temas e princípios criativos surgiram no passado, estão surgindo agora e surgirão mais tarde? É possível identificar os princípios básicos que lhes estão subjacentes?",
"w01.256": "Como os seres humanos que se tornaram finalitores se relacionarão com todos esses desenvolvimentos, no palco do grande universo da idade presente e no palco dos universos exteriores das idades futuras?",
"w01.257": "O universo-mestre é a criação final? No futuro remoto entrará ele em relação com algo ainda maior?",
"w01.258": "Qual é o limite final, e qual é a meta final?",
"w01.259": "Uma unificação da ignorância",
"w01.260": "Sadler diz que tratará dessas perguntas examinando as idades do universo uma após a outra. Antes da idade presente houve apenas uma, a idade de Havona, que o prólogo já tratou. Agora ele considerará a segunda idade, quando os superuniversos são desenvolvidos, e depois passará às idades futuras dos quatro níveis do espaço exterior.",
"w01.261": "Onde os dados têm lacunas, diz ele, ele as transporá pelo raciocínio. Admite também que tal especulação não pode escapar dos limites impostos pela ignorância humana. Ainda assim, espera ao menos alcançar uma melhor “unificação da ignorância”. Simplesmente pôr em ordem o que não sabemos já é um passo adiante. A introdução termina com um convite a partir com espírito de aventura, levando consigo humildade intelectual sem perder a coragem.",
"w01.262": "O corpo principal conta como a divindade do Paraíso-Havona se estende no tempo e no espaço e se consolida no Supremo e no Último; está organizado em três partes, a história finita, a absonita e a final.",
"w01.263": "Havona mais os sete superuniversos é o grande universo; o grande universo mais os quatro níveis do espaço exterior é o universo-mestre. A Ilha do Paraíso é o centro absoluto e não pertence a universo algum.",
"w01.264": "O universo-mestre consiste em seis níveis espaciais elípticos concêntricos que rodeiam o Paraíso [12:1.3].",
"w01.265": "Sadler faz corresponder um a um os seis níveis espaciais com seis idades do universo; essa correspondência é um esquema dele próprio, montado a partir de afirmações dispersas no texto.",
"w01.266": "O tamanho dos níveis espaciais, a duração das idades, o crescimento da Deidade experiencial, os princípios criativos, o futuro dos finalitores, o que está além do universo-mestre e a meta final formam os sete grupos de perguntas que o estudo formula.",
"w01.267": "Sadler preenche lacunas pelo raciocínio, reconhecendo os seus limites, e propõe uma investigação marcada ao mesmo tempo por humildade intelectual e por coragem.",
}
for k, v in T.items():
    assert k in SRC, k
    D[k] = v
order = [k for k in SRC if k in D]
D = {k: D[k] for k in order}
json.dump(D, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(D), "of", len(SRC), "missing:", [k for k in SRC if k not in D])

Q = {
"w01.045": "É o núcleo eterno da perfeição; e em torno dele gira a procissão interminável de universos que constituem os experimentos evolucionários formidáveis, a aventura audaciosa…",
"w01.060": "…em outras palavras, que nunca existiu um tempo em que o EU SOU não tivesse sido o Pai do Filho e, junto com Este, Pai do Espírito.",
"w01.091": "Pela técnica da trinitarização, o Pai despoja-se daquela personalidade espiritual inqualificável, que é o Filho, mas, fazendo assim, Ele constitui-se como o Pai deste mesmo Filho…",
"w01.158": "Deus é amor, o Filho é misericórdia, o Espírito é o ministério…",
"w01.159": "A aplicação da lei, a justiça, cai no domínio da Trindade do Paraíso, e é levada avante por certos Filhos da Trindade.",
"w01.189": "A órbita mais interna consiste nas sete esferas secretas do Pai Universal; a segunda órbita é composta dos sete mundos luminosos do Filho Eterno…",
"w01.194": "Deus, enquanto suprapessoa, manifesta; Deus, enquanto pessoa, cria; Deus, enquanto pré-pessoa, fragmenta-se…",
"w01.199": "A Trindade Última, atualmente em evolução, consistirá, finalmente, no Ser Supremo, nas Personalidades Criadoras Supremas e nos Arquitetos absonitos do universo-mestre…",
}
TODO = json.load(open(os.path.join(H, "work", "todo_pt_c01.json"), encoding="utf-8"))
assert set(Q) == set(TODO), set(TODO) ^ set(Q)
json.dump({k: Q[k] for k in TODO}, open(os.path.join(H, "pt", "quotes_c01.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("quotes", len(Q))
