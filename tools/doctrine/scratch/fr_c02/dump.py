import json, os, sys
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
src = json.load(open(os.path.join(root, 'work', 'src_c02.json'), encoding='utf-8'))
ch = sys.argv[1]
out = []
for k, v in src.items():
    if k.startswith(ch + ':'):
        out.append('### ' + k)
        out.append(json.dumps(v, ensure_ascii=False, indent=1) if not isinstance(v, str) else v)
open(os.path.join(here, 'src_' + ch + '.txt'), 'w', encoding='utf-8').write('\n'.join(out))
