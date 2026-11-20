import re, json, sys
src = json.load(open("work/src_c01.json", encoding="utf-8"))
for f in sys.argv[1:]:
    s = open(f, encoding="utf-8").read()
    ks = re.findall(r'^\s*"((?:ch\d\d|part|audio):[\w]+)"\s*:', s, re.M)
    print(f, len(ks), ks[0] if ks else None, ks[-1] if ks else None)
    print("  tail:", s[-300:].replace("\n", " | "))
