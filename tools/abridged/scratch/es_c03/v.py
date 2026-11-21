import sys, json
sys.path.insert(0, r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\tools")
import amq
for c in sys.argv[1:]:
    print(c, amq.text("es", c)); print()
