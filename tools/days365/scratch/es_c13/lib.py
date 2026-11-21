import json, re, os
B = 'E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/days365/'
OUT = B + 'es/c13.json'
src = json.load(open(B + 'work/src_c13.json', encoding='utf-8'))
inl = json.load(open(B + 'work/inline_es_c13.json', encoding='utf-8'))


def conv(s):
    return re.sub(r'\{\{([^|{}]+)\|(.*?)\}\}', lambda m: '\u27e6Q ' + m.group(1) + '\u27e7' + m.group(2) + '\u27e6/Q\u27e7', s)


def norm(s):
    return re.sub(r'\s+', '', s)


def save(units):
    D = json.load(open(OUT, encoding='utf-8')) if os.path.exists(OUT) else {}
    for k, u in units.items():
        s = src[k]
        assert len(u['msg']) == len(s['msg']), (k, len(u['msg']), len(s['msg']))
        D[k] = {'_ref': s['_ref'], 't': u['t'], 'msg': [conv(p) for p in u['msg']], 'pr': conv(u['pr'])}
        # quick quote check
        qs = []
        for i, p in enumerate(D[k]['msg']):
            for j, m in enumerate(re.finditer('\u27e6Q ([^\u27e7]+)\u27e7(.*?)\u27e6/Q\u27e7', p)):
                qs.append(('%s.msg[%d].%d' % (k, i, j + 1), m.group(1), m.group(2)))
        exp = inl.get(k, [])
        if len(qs) != len(exp):
            print('COUNT MISMATCH', k, len(qs), len(exp))
        for (at, cit, txt), e in zip(qs, exp):
            if at != e['at'] or cit != e['cit']:
                print('POS MISMATCH', at, cit, e['at'], e['cit'])
            for piece in txt.split(' \u2026 '):
                if norm(piece) not in norm(e['verse']):
                    print('NOT VERBATIM', at, '|', piece)
    O = {k: D[k] for k in src if k in D}
    json.dump(O, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('saved', len(O), 'units')
