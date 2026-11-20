import json, os, sys, re
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
FR = json.load(open(os.path.join(root, '..', 'data', 'fr.json'), encoding='utf-8'))
EN = json.load(open(r'E:\OneDrive\유란시아 작업\theology-book\en.json', encoding='utf-8'))
# usage: look.py terms.txt  (lines: "fr:word" counts in FR, "en:word" shows FR verse snippets for EN matches)
lines = open(os.path.join(here, sys.argv[1]), encoding='utf-8').read().splitlines()
out = []
for ln in lines:
    ln = ln.strip()
    if not ln:
        continue
    kind, w = ln.split(':', 1)
    if kind == 'v':
        out.append(w + ' ' + FR.get(w, '?'))
        continue
    if kind == 'fr':
        hits = [k for k, v in FR.items() if w in v]
        out.append('FR %r: %d %s' % (w, len(hits), hits[:4]))
    else:
        hits = [k for k, v in EN.items() if w in v][:2]
        out.append('EN %r: %s' % (w, hits))
        for h in hits:
            out.append('   ' + h + ' ' + FR.get(h, '')[:400])
open(os.path.join(here, 'look_out.txt'), 'w', encoding='utf-8').write('\n'.join(out))
