import json, re, sys
B = 'E:/OneDrive/내 문서/유란시아/urantiaamerica 홈페이지/tools/days365/'
src = json.load(open(B + 'work/src_c13.json', encoding='utf-8'))
inl = json.load(open(B + 'work/inline_es_c13.json', encoding='utf-8'))
ref = json.load(open(B + 'work/ref_es_c13.json', encoding='utf-8'))
out = open(B + 'scratch/es_c13/dump.txt', 'w', encoding='utf-8')
for day, u in src.items():
    r = ref.get(day, {})
    out.write('\n===== %s _ref=%s  T: %s\n' % (day, u['_ref'], u['t']))
    out.write('REF_ES: ' + ' / '.join(r.get('es', [])) + '\n')
    shown = set()
    for i, p in enumerate(u['msg']):
        out.write('[%d] %s\n' % (i, p))
        for q in inl.get(day, []):
            if q['at'].startswith('%s.msg[%d].' % (day, i)):
                if q['auto']:
                    out.write('   %s AUTO: %s\n' % (q['at'], q['auto']))
                else:
                    if q['cit'] in shown or ' / '.join(r.get('es', [])).find(q['verse'][:60]) >= 0:
                        out.write('   %s HAND %s (verse shown above)\n' % (q['at'], q['cit']))
                    else:
                        out.write('   %s HAND %s VERSE: %s\n' % (q['at'], q['cit'], q['verse']))
                    shown.add(q['cit'])
    out.write('PR: ' + u['pr'] + '\n')
    other = [k for k in u if k not in ('_ref', 't', 'msg', 'pr')]
    if other:
        out.write('OTHER KEYS: %s\n' % other)
