# -*- coding: utf-8 -*-
# 'Jay Han' 저자 표기 빼기 (2026-11-27 사용자 지시: America 판은 전부, 극동판은 한국어판만 남기고 전부)
#   python strip_byline.py am|fe [--dry]
#   빌더가 다시 만들면 표기가 되살아날 수 있으니, 메뉴를 다시 빌드한 뒤 배포 전에 꼭 다시 돌린다.
#   (같은 파일이 두 폴더 tools/ 에 있다: urantiaamerica 홈페이지\tools, urantiafareast 홈페이지\tools)
import os, re, sys

sys.stdout.reconfigure(encoding="utf-8")
ROOTS = {"am": r"E:\OneDrive\내 문서\유란시아\urantiaamerica 홈페이지\site",
         "fe": r"E:\OneDrive\내 문서\유란시아\urantiafareast 홈페이지\site"}
# 극동판에서 손대는 곳(한국어판이 아닌 곳)
FE_PREFIX = ("en/", "zh/", "ja/", "core-en/", "reader-en/", "audiobook/en/", "mirror/audiobook-en/", "eng-kor/en/")
HANGUL = re.compile(r"[가-힣]")
JH = r"Jay Han"
SP = r"(?:\s|&nbsp;)*"
RULES = [
    # 공유 그림(canvas) 서명 줄과 대체 제목
    (r"\n?[ \t]*ctx\.fillText\('(?:ORGANIZED BY|ORGANIZADO POR|ORGANISÉ PAR) JAY HAN'[^;]*;", ""),
    (r"'(?:Organized by|Organizado por|Organisé par) Jay Han'", "''"),
    # 통째로 이름만 담은 요소
    (r'[ \t]*<div class="welcome-credit">[^<]*Jay Han</div>\n?', ""),
    (r'<div class="by">[^<]*Jay Han[^<]*</div>', ""),
    (r'[ \t]*<div class="byline">[^<가-힣]*Jay Han[^<가-힣]*</div>\n?', ""),
    (r'[ \t]*<div class="cover-author">[^<]*<span>Jay Han</span></div>\n?', ""),
    (r'[ \t]*<div (?:id|class)="(?:credit|jayhan|title-credit)">[^<]*Jay Han[^<]*</div>\n?', ""),
    (r'<p>© \d+ Jay Han[.。]</p>', ""),
    # 저작권 문장
    (r"\s*(?:版权所有\s*)?(?:Copyright\s*)?©\s*\d+\s*Jay Han[.。]\s*(?:All rights reserved\.|Todos los derechos reservados\.|Tous droits réservés\.|Todos os direitos reservados\.|保留一切权利。)?", ""),
    # 책 머리말 끝 서명 ["p", "Jay Han"]
    (r',\s*\["p",\s*"Jay Han"\]', ""),
    # JSON/JS 필드 통째
    (r'"(by|author|copy_card_by)":\s*"[^"]*Jay Han[^"]*"', r'"\1": ""'),
    (r'(\bbyline:\s*)"[^"가-힣]*Jay Han[^"가-힣]*"', r'\1""'),
    # 제목 끝 " — Jay Han"
    (r"\s*—\s*Jay Han(?=</title>|\")", ""),
    # 출처 줄 " | Jay Han"
    (r"\s*\|\s*Jay Han(?=\\n|\n|<)", ""),
    # 앞에 붙은 "Jay Han · " / "By Jay Han\n"
    (r"Jay Han" + SP + r"·" + SP, ""),
    (r"By Jay Han\\n", ""),
    (r"(?:by|por|par|By|Por|Par) Jay Han · ", ""),
    (r"(?:produced|Produced) by Jay Han" + SP + r"(?:·|&middot;)" + SP, ""),
    # 뒤에 붙은 " · Jay Han", " &middot; Produced by Jay Han"
    (SP + r"(?:·|&middot;)" + SP + r"(?:(?:by|por|par|Produced by|produced by) )?Jay Han(?:\s*著)?", ""),
    # 문장 속 "…, by Jay Han." / "Organized by Jay Han." / "作者：Jay Han。" / "Edited and made by Jay Han."
    (r"\.?\s*(?:Edited and made by|Organized by|organized by|Organizado por|organizado por|Organisé par|organisé par|By|by|Por|por|Par|par|Produced by|produced by) Jay Han(?: with help of AI)?\.", "."),
    (r",?\s*(?:Edited and made by|Organized by|organized by|Organizado por|Organisé par|By|by|Por|por|Par|par) Jay Han(?=[<\"'])", ""),
    (r"作者：Jay Han。", ""),
    (r"作者：Jay Han", ""),
]
RULES = [(re.compile(a), b) for a, b in RULES]
CHECK = re.compile(r"jay\s*han", re.I)


def wanted(site, rel):
    if site == "am": return True
    return rel == "i18n.js" or rel.startswith(FE_PREFIX)


def main():
    site = sys.argv[1]; dry = "--dry" in sys.argv
    root = ROOTS[site]; changed = 0; left = []
    for dp, dn, fn in os.walk(root):
        for f in fn:
            if not f.endswith((".html", ".js", ".json", ".txt", ".xml", ".md", ".webmanifest")): continue
            p = os.path.join(dp, f); rel = os.path.relpath(p, root).replace("\\", "/")
            if not wanted(site, rel): continue
            try: t = open(p, encoding="utf-8", newline="").read()
            except Exception: continue
            if not CHECK.search(t): continue
            u = t
            for rx, rep in RULES: u = rx.sub(rep, u)
            for m in CHECK.finditer(u):
                ctx = u[max(0, m.start() - 60):m.end() + 30].replace("\n", "⏎")
                if site == "fe" and rel == "i18n.js" and HANGUL.search(ctx): continue   # 한국어 byline 은 남김
                if "t==='Jay Han'" in ctx or "#jayhan" in ctx.lower() or 'id="jayhan"' in ctx: continue  # 쓰이지 않는 코드·CSS
                left.append((rel, ctx))
            if u != t:
                changed += 1
                if not dry: open(p, "w", encoding="utf-8", newline="").write(u)
    print(f"[{site}] files changed: {changed}{' (dry run)' if dry else ''}; leftovers: {len(left)}")
    for r, c in left[:60]: print("  ", r, "|", c)


main()
