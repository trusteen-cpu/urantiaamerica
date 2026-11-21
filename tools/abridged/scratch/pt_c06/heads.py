# -*- coding: utf-8 -*-
import json, os
from save import save, BASE, SRC
src = json.load(open(SRC, encoding='utf-8'))
H = json.load(open(os.path.join(BASE, 'work', 'title_hints_pt.json'), encoding='utf-8'))
FIX = {"Overview": "Visão geral", "The Paper": "O documento", "Conclusion": "Conclusão"}
D = {}
for k, v in src.items():
    if k.endswith('.title'):
        D[k] = H[k]
    elif k.endswith('.h'):
        if k in H: D[k] = H[k]
        elif v in FIX: D[k] = FIX[v]
        elif v.startswith('Key Points of Paper '): D[k] = 'Pontos-chave do documento ' + v.split()[-1]
        else: print('?', k, v)
save(D)
