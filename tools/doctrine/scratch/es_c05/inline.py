import json, re, sys, os
sys.stdout.reconfigure(encoding="utf-8")
base = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
src = json.load(open(os.path.join(base, "work", "src_c05.json"), encoding="utf-8"))
es = json.load(open(os.path.join(base, "..", "data", "es.json"), encoding="utf-8"))
ch = sys.argv[1] if len(sys.argv) > 1 else ""
def texts(v):
    if isinstance(v, str): yield v
    elif isinstance(v, dict):
        for r in v.get("rows", []):
            for c in r: yield c
        for i in v.get("items", []): yield i
for k, v in src.items():
    if not k.startswith(ch): continue
    for t in texts(v):
        for m in re.finditer(r"“([^”]+)”\s*\((\d+:\d+\.\d+)", t):
            print("==", k, m.group(2), "|", m.group(1))
            print("   ES:", es.get(m.group(2)))
