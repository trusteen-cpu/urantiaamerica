import json, sys, os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
s = json.load(open('work/src_c17.json', encoding='utf-8'))
q = json.load(open('work/quotes_es_c17.json', encoding='utf-8'))
h = json.load(open('work/headings_es_c17.json', encoding='utf-8'))
out = open('scratch/es_c17/dump.txt', 'w', encoding='utf-8')
for k, v in s.items():
    out.write('=== %s\n%s\n' % (k, v))
    if k in h:
        out.write('  H: %s\n' % h[k]['official'])
    for x in q.get(k, []):
        out.write('  Q#%s %s how=%s\n   EN: %s\n   AUTO: %s\n   VERSE: %s\n' % (x['n'], x['cit'], x['how'], x['en'], x['auto'], x['verse']))
out.close()
# also Introduction headings in other es chunks
for f in sorted(os.listdir('es')):
    d = json.load(open('es/' + f, encoding='utf-8'))
    src = json.load(open('work/src_' + f, encoding='utf-8')) if os.path.exists('work/src_' + f) else {}
    for k, v in src.items():
        if v in ('Introduction', 'Conclusion', 'Closing', 'Summary') and k in d:
            print(f, k, v, '->', d[k]); break
