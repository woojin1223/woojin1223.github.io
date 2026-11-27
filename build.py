#!/usr/bin/env python3
"""Build the guest invitation page for GitHub Pages.

Reads  src/index.html      (the editable invitation page, same code as the claude.ai artifact)
       data/invite.json    (saved content: texts, photo order, positions/sizes from edit mode)
       photos/<id>.jpg     (photos referenced by id in data/invite.json; og.jpg = link preview)
       src/fonts, src/bg, src/frames
Writes site/index.html + site/og.jpg + site/.nojekyll  -> copy these three to the main branch root.

Usage: python3 build.py [--base https://woojin1223.github.io/]
"""
import json, re, base64, os, sys, shutil, mimetypes

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = "https://woojin1223.github.io/"
if "--base" in sys.argv:
    BASE = sys.argv[sys.argv.index("--base") + 1].rstrip("/") + "/"

def p(*a): return os.path.join(HERE, *a)
def data_uri(path):
    mime = {".woff2": "font/woff2", ".webp": "image/webp"}.get(os.path.splitext(path)[1]) or mimetypes.guess_type(path)[0]
    return f"data:{mime};base64," + base64.b64encode(open(path, "rb").read()).decode()

s = open(p("src", "index.html"), encoding="utf-8").read()
db = json.load(open(p("data", "invite.json"), encoding="utf-8"))

# 1) bake saved content into the page's seed (same merge the page does at runtime)
m = re.search(r'<script id="seed" type="application/json">(.*?)</script>', s, re.S)
seed = json.loads(m.group(1))
labels = {**seed.get("labels", {}), **db.get("labels", {})}
cover = {**seed.get("cover", {}), **db.get("cover", {})}
seed.update(db); seed["labels"] = labels; seed["cover"] = cover
seed["shareUrl"] = BASE
s = s[:m.start(1)] + json.dumps(seed, ensure_ascii=False).replace("<", "\\u003c") + s[m.end(1):]

# 2) inline every photo the content references (cover reel, middle, gallery, hero)
ids = set(seed["cover"].get("reel", [])) | {seed.get("middle"), seed.get("hero")} | set(seed.get("gallery", []))
blobs = {}
for i in filter(None, ids):
    f = p("photos", i + ".jpg")
    if not os.path.exists(f):
        sys.exit(f"missing photo: photos/{i}.jpg (add the file or remove the id from data/invite.json)")
    blobs[i] = data_uri(f)

def rep(a, b, count=None):
    global s
    n = s.count(a)
    if n == 0 or (count is not None and n != count):
        sys.exit(f"build: pattern not found as expected ({n}x): {a[:60]}")
    s = s.replace(a, b)

rep('/_blob/${esc(id)}', '${blob(id)}')
rep('"/_blob/"+id', 'blob(id)')
rep('const MON=[', 'const BLOB=' + json.dumps(blobs) + ';\nconst blob=id=>BLOB[id]||("/_blob/"+id);\nconst MON=[', 1)
rep('url("fonts/Pretendard-Regular.subset.woff2")', 'url("' + data_uri(p("src", "fonts", "Pretendard-Regular.subset.woff2")) + '")', 1)
rep('url("bg/paper.jpg")', 'url("' + data_uri(p("src", "bg", "paper.jpg")) + '")', 1)
rep('"frames/instax-wide.webp?v=2"', '"' + data_uri(p("src", "frames", "instax-wide.webp")) + '"', 1)

# 3) guest cleanup: drop the temporary P01.. section numbers
s, n = re.subn(r'/\* TEMP page numbers.*?\n\[data-n\]::after\{[^}]*\}\n\.cover\[data-n\]::after\{[^}]*\}\n', '', s, flags=re.S)

# 4) title + link-preview meta
meta = f'''<title>안우진 ♥ 박유리 결혼합니다</title>
<meta name="description" content="2027년 3월 7일(일) 낮 12시, 롯데호텔 월드 에메랄드룸 — 안우진 · 박유리의 결혼식에 초대합니다.">
<meta property="og:type" content="website">
<meta property="og:url" content="{BASE}">
<meta property="og:title" content="안우진 ♥ 박유리 결혼합니다">
<meta property="og:description" content="2027년 3월 7일(일) 낮 12시 · 롯데호텔 월드 에메랄드룸">
<meta property="og:image" content="{BASE}og.jpg">
<meta name="robots" content="noindex">'''
s = re.sub(r'<title>.*?</title>', lambda _: meta, s, count=1)

os.makedirs(p("site"), exist_ok=True)
open(p("site", "index.html"), "w", encoding="utf-8").write(s)
shutil.copy(p("photos", "og.jpg"), p("site", "og.jpg"))
open(p("site", ".nojekyll"), "w").close()
print(f"site/index.html {os.path.getsize(p('site','index.html'))/1e6:.2f} MB, {len(blobs)} photos inlined, page numbers removed: {bool(n)}")
