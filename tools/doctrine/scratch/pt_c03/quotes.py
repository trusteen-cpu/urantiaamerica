import json, os
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
V = json.load(open('../data/pt.json', encoding='utf-8'))

def cut(ref, start, end):
    t = V[ref]
    i = t.index(start)
    j = t.index(end, i) + len(end)
    return t[i:j]

Q = {}
Q['ch12:9'] = cut('111:2.8', 'o impulso da mente finita', 'experiência da criatura.')
Q['ch12:11'] = cut('111:2.2', 'A mente material do homem mortal', 'as significações divinas')
Q['ch12:16'] = cut('111:2.9', 'Essa transação superna', 'realidades supra-animais')
Q['ch12:18'] = cut('111:2.10', 'o nascimento gradual de uma alma', 'o Monitor Misterioso.')
Q['ch12:32'] = cut('111:3.7', 'Na mesma medida', 'torna-se indestrutível.')
Q['ch12:34'] = cut('111:3.2', 'Durante a vida, a vontade mortal', 'da alma moroncial emergente')
Q['ch13:16'] = cut('62:6.5', 'quando, cerca de um ano depois', 'como mentes humanas.')
Q['ch13:24'] = cut('62:5.9', 'Embora estivéssemos', 'arbitrariamente as suas decisões')
Q['ch15:10'] = cut('53:2.5', 'Deve ter havido um orgulho', 'se não do universo.')
Q['ch15:19'] = cut('53:5.7', 'a vida material fica em perigo', 'a vida eterna.')
Q['ch15:23'] = cut('54:1.6', 'A verdadeira liberdade é derivada', 'pretensão da afirmação do ego.')
Q['ch15:29'] = cut('54:3.1', 'A capacidade do homem', 'liberdade divinamente outorgada')
Q['ch15:49'] = cut('67:7.5', 'mas o pecado de um ser qualquer', 'do próprio indivíduo.')
Q['ch16:49'] = cut('76:5.7', 'mas antes porque o mal', 'Pai do Paraíso.')
os.makedirs('pt', exist_ok=True)
json.dump(Q, open('pt/quotes_c03.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(len(Q))
