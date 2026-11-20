from save import save

Q = "Por favor, dê-me as explicações de livro didático sobre o elétron, o quantum, o nêutron, o átomo e o elemento, com as suas características e relações."
P = [
"\n".join([
"1. Definições e características de cada conceito",
"Elemento",
"Definição: um tipo (constituinte) de matéria que não pode ser decomposto por meios químicos (por exemplo, hidrogênio, oxigênio, carbono, ferro).",
"Características: o seu tipo é determinado pelo número de prótons no núcleo atômico (o número atômico), e as suas propriedades se repetem com uma periodicidade regular na tabela periódica.",
"Átomo",
"Definição: a menor unidade física e química de partícula que constitui um elemento.",
"Características: consiste num núcleo atômico denso no centro e em elétrons que circulam ao seu redor, uma estrutura semelhante a um sistema solar.",
"Próton versus quantum",
"Próton: uma partícula com carga positiva (+) que compõe o núcleo atômico. É cerca de 2.000 vezes mais pesado do que o elétron, de carga negativa (-), e o número de prótons é o número atômico do átomo e determina o tipo de elemento.",
"Quantum: não é o nome de uma partícula, mas a unidade física básica de energia, significando que a energia é absorvida ou emitida em pacotes mínimos descontínuos. (Nos livros didáticos coreanos e no uso cotidiano, a palavra para “próton” às vezes é abreviada na palavra para “quantum”, mas, como conceito físico, o quantum é a unidade mínima de energia.)",
"Nêutron",
"Definição: uma partícula sem carga elétrica (neutra) que existe no núcleo atômico junto com os prótons.",
"Características: entre os prótons, cujas cargas positivas (+) se repelem mutuamente, ele mantém o núcleo coeso para que não se desfaça, conservando a estabilidade do núcleo atômico.",
"Elétron",
"Definição: uma partícula diminuta, de carga negativa (-), que gira em alta velocidade ao redor do núcleo atômico.",
"Características: é extremamente leve, cerca de 1/2.000 do peso do átomo de hidrogênio, o átomo mais leve, e o movimento e a revolução dos elétrons externos do átomo dão origem às reações químicas e aos fenômenos elétricos da matéria.",
]),
"\n".join([
"2. A sua relação orgânica",
"Tipo macroscópico e partícula microscópica: um elemento é o nome que designa um tipo químico de matéria, e a unidade de partícula real que constitui esse elemento é o átomo.",
"A estrutura interna do átomo: no centro do átomo encontra-se o núcleo atômico, formado por prótons e nêutrons fortemente ligados entre si.",
"O movimento dos elétrons: nas órbitas externas ao redor do núcleo atômico, giram os elétrons.",
"A transferência de energia (o quantum): quando um elétron se move entre órbitas ou absorve ou emite energia, a energia é transferida não como um fluxo contínuo, mas em pacotes unitários específicos chamados quanta",
]),
]
save("q098", Q, P)
