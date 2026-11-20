# -*- coding: utf-8 -*-
"""다 만든 메뉴를 첫 화면에 연결한다: python tools/add_menu.py <메뉴id> [폴더이름]
   site/<l>/<폴더>/index.html 이 있는 언어만 i18n.js links.<l> 에 넣고, PROGRESS.md 에 ✅ 를 찍고, build_home.py 를 돌린다."""
import datetime, os, re, subprocess, sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.join(HERE, "..", "site")
mid = sys.argv[1]; folder = sys.argv[2] if len(sys.argv) > 2 else mid
p = os.path.join(SITE, "i18n.js")
s = open(p, encoding="utf-8").read()
assert len(s) > 5000, "i18n.js 가 비정상"
done = []
for l in ("es", "fr", "pt"):
    if not os.path.exists(os.path.join(SITE, l, folder, "index.html")): continue
    m = re.search(rf'\n    {l}: \{{ text: "{l}/book/",[^\n]*\}}', s)
    assert m, l
    line = m.group()
    if f' {mid}: "' not in line:
        line2 = line.replace(f'text: "{l}/book/",', f'text: "{l}/book/", {mid}: "{l}/{folder}/",')
        s = s.replace(line, line2)
    done.append(l)
open(p, "w", encoding="utf-8", newline="\n").write(s)
# 진행표
pg = os.path.join(HERE, "PROGRESS.md")
t = open(pg, encoding="utf-8").read()
today = datetime.date.today().isoformat()
def tick(m):
    cells = m.group(0).split("|")
    for i, l in ((3, "es"), (4, "fr"), (5, "pt")):
        if l in done: cells[i] = " ✅ "
    if done: cells[6] = f" {today} "
    return "|".join(cells)
t = re.sub(rf"^\| {re.escape(mid)} \|.*$", tick, t, flags=re.M)
open(pg, "w", encoding="utf-8", newline="\n").write(t)
subprocess.run([sys.executable, os.path.join(HERE, "build_home.py")], check=True)
print("연결:", mid, done)
