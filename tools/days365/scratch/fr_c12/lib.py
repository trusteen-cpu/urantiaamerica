import json, os
B = 'E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/days365/'
OUT = B + 'fr/c12.json'
SRC = json.load(open(B + 'work/src_c12.json', encoding='utf-8'))


def add(units):
    D = {}
    if os.path.exists(OUT):
        D = json.load(open(OUT, encoding='utf-8'))
    for d, (t, msg, pr) in units.items():
        assert len(msg) == len(SRC[d]['msg']), (d, len(msg), len(SRC[d]['msg']))
        D[d] = {'_ref': SRC[d]['_ref'], 't': t, 'msg': msg, 'pr': pr}
    O = {k: D[k] for k in SRC if k in D}
    json.dump(O, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(O), 'units')
