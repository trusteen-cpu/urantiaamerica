import json, os, re, sys, collections
here = os.path.dirname(os.path.abspath(__file__))
root = os.path.abspath(os.path.join(here, '..', '..'))
V = json.load(open(os.path.join(root, '..', 'data', 'pt.json'), encoding='utf-8'))
vocab = collections.Counter()
for t in V.values():
    for w in re.findall(r"[^\W\d_]+(?:-[^\W\d_]+)*", t):
        vocab[w.lower()] += 1
sys.path.insert(0, here)
import importlib
for name in sys.argv[1:]:
    T = importlib.import_module(name).T
    txt = json.dumps(T, ensure_ascii=False)
    miss = set()
    for w in re.findall(r"[^\W\d_]+(?:-[^\W\d_]+)*", txt):
        if w.lower() not in vocab:
            miss.add(w)
    print(name, sorted(miss))
