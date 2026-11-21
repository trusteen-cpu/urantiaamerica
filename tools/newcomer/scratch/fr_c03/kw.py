import json, sys, re
sys.stdout.reconfigure(encoding='utf-8')
FR = json.load(open(r'E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools\data\fr.json', encoding='utf-8'))
EN = json.load(open(r'E:\OneDrive\유란시아 작업\theology-book\en.json', encoding='utf-8'))
# usage: kw.py "en phrase" "fr regex"   -> shows fr windows for verses containing en phrase, or fr regex matches
mode = sys.argv[1]
for q in sys.argv[2:]:
    print('##', q)
    n = 0
    if mode == 'fr':
        c = {}
        for k, v in FR.items():
            for m in re.finditer(q, v):
                s = m.group(0)
                c[s] = c.get(s, 0) + 1
                if c[s] <= 1:
                    print(' ', k, '...' + v[max(0, m.start()-50):m.end()+50] + '...')
        print('  counts', c)
    else:
        for k, v in EN.items():
            if q.lower() in v.lower():
                i = v.lower().index(q.lower())
                print(' ', k, 'EN:', v[max(0, i-60):i+len(q)+60])
                f = FR.get(k, '')
                print('     FR:', f[max(0, int(i*len(f)/max(1, len(v)))-120):int(i*len(f)/max(1, len(v)))+160])
                n += 1
                if n >= 2:
                    break
