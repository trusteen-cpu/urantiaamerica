import sys, os, re, json
sys.stdout.reconfigure(encoding='utf-8')
FEJ = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\tools\jesus"
sys.path.insert(0, FEJ)
import build_teachings_ko as BT
BT.SRC = r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site\en\jesus\teachings\index.html"
U = {}
class B2(BT.Build):
    def __init__(self):
        super().__init__(); self.tr = {}
    def T(self, en, hint_cits=(), ctx=''):
        en = BT.norm_space(en)
        if not en: return ''
        if not re.search(r'[A-Za-z]', en): return en
        if BT.is_bible_only(en): return '⟦B⟧' + en
        k = BT.key_of(en); U.setdefault(k, (en, ctx)); return '⟦T ' + k + '⟧'
b = B2()
arts, ids = b.run()
print(len(U), sum(len(v[0].split()) for v in U.values()))
print(b.stats)
s = '\n'.join(arts)
print(len(re.findall('[가-힣]+', s)), set(re.findall('[가-힣][가-힣 ]*', s)))
bw = [v[0] for v in U.values() if re.search(r'\b(Matt|Mark|Luke|John)\b\.? ?\d', v[0])]
print(len(bw)); print(bw[:15])
json.dump(U, open('teach_units.json','w',encoding='utf-8'), ensure_ascii=False, indent=0)
open('teach_arts.html','w',encoding='utf-8').write(s)
