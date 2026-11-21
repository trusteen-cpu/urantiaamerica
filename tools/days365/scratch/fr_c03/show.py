import json, sys, os
os.chdir(os.path.join(os.path.dirname(__file__), '..', '..'))
src = json.load(open('work/src_c03.json', encoding='utf-8'))
inl = json.load(open('work/inline_fr_c03.json', encoding='utf-8'))
ref = json.load(open('work/ref_fr_c03.json', encoding='utf-8'))
out = []
for day in sys.argv[1:]:
    u = src[day]
    out.append('=== %s ref %s' % (day, u['_ref']))
    out.append('REF FR: ' + ' / '.join(ref[day]['fr']))
    out.append('T: ' + u['t'])
    for i, p in enumerate(u['msg']):
        out.append('P%d: %s' % (i, p))
    out.append('PR: ' + u['pr'])
    seen=set()
    for q in inl.get(day, []):
        out.append('Q %s %s AUTO=%s' % (q['at'], q['cit'], q['auto']))
        if not q['auto']:
            out.append('   EN: ' + q['en'])
            if q['cit'] not in seen and q['verse'] not in ref[day]['fr']:
                out.append('   VERSE: ' + q['verse'])
            seen.add(q['cit'])
sys.stdout.reconfigure(encoding='utf-8')
print('\n'.join(out))
