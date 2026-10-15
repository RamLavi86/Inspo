"""Build the hosted inspo app from the single-file source (inspo.html).
Usage: python3 build.py  -> writes index.html next to manifest.webmanifest and sw.js."""
import re, pathlib, time
root = pathlib.Path(__file__).parent
src = (root / 'inspo.html').read_text(encoding='utf8')
head = ('<!doctype html><html lang="en"><head><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">'
        '<meta name="theme-color" content="#1b1d20"><meta name="color-scheme" content="light">'
        '<link rel="manifest" href="manifest.webmanifest"><link rel="icon" href="icons/icon-192.png">'
        '<link rel="apple-touch-icon" href="icons/icon-180.png">'
        '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">'
        '<meta name="apple-mobile-web-app-title" content="inspo">'
        '<style>html,body{height:100%;margin:0}[hidden]{display:none!important}body{font:14px system-ui,sans-serif}</style>'
        '</head><body>')
sw = ("<script>if('serviceWorker' in navigator){addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));}</script>")
(root / 'index.html').write_text(head + src + sw + '</body></html>', encoding='utf8')
# bump the service-worker cache version so installed apps pick up the new build
swp = root / 'sw.js'; s = swp.read_text(encoding='utf8')
swp.write_text(re.sub(r"const V='inspo-[^']*'", f"const V='inspo-{int(time.time())}'", s), encoding='utf8')
print('built index.html')
