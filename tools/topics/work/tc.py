import sys,re,collections,json
sys.path.insert(0,'.'); import amq
EN=json.load(open(r'E:\OneDrive\유란시아 작업\theology-book\en.json',encoding='utf-8'))
# usage: tc.py "English phrase" -> show first verse in each lang with snippet around
for ph in sys.argv[1:]:
    cs=[c for c,v in EN.items() if ph.lower() in v.lower()][:2]
    print('##',ph,cs)
    for c in cs[:1]:
        e=EN[c]; i=e.lower().find(ph.lower()); print('  en:',e[max(0,i-60):i+90])
        for l in ('es','fr','pt'):
            t=amq.text(l,c); r=i/len(e); j=int(r*len(t)); print('  ',l+':',t[max(0,j-120):j+160])
