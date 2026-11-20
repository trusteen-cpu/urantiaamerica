import sys,os
sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools")
import amq
for r in sys.argv[1:]:
    print(r, amq.text("es", r)); print()
