# Build the animated egg as a standalone element: decks/elements/christendom-egg-animated.html
# Run from the repo root:  python3 decks/src/elements/build_egg_anim.py
import sys, os
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from christendom import PATDEFS, CHRISTENDOM_CSS
from egg_anim import egg_anim_slide, EGG_ANIM_CSS, EGG_ANIM_JS

ENGINE = os.path.join(HERE, '..', 'week3')
css = open(os.path.join(ENGINE, 'engine.css')).read() + CHRISTENDOM_CSS + EGG_ANIM_CSS
js = open(os.path.join(ENGINE, 'engine.js')).read()
js = js.replace("'w1cur'", "'eacur'").replace("'w1mode'", "'eamode'").replace("'w1strip'", "'eastrip'").replace("'w1presenter'", "'eapresenter'")
js = js.replace("||'read')", "||'present')")

html = ('<!doctype html><html><head><meta charset=utf8>'
 '<meta name=viewport content="width=device-width,initial-scale=1">'
 '<title>The Egg, Animated</title>'
 '<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&family=Spectral:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap">'
 '<style>\n/* The egg, animated. Source: decks/src/elements/egg_anim.py */\n' + css + '</style></head>\n<body>\n'
 '<svg width=0 height=0 style="position:absolute;visibility:visible" aria-hidden=true>' + PATDEFS + '</svg>\n<div id=deck>\n\n'
 + egg_anim_slide() +
 '\n\n</div>\n<div id=bar></div><div id=count></div>'
 '<div id=hint>&rarr; / space / click &middot; f fullscreen &middot; n read/present &middot; p presenter window &middot; s notes on THIS screen</div>'
 '<div id=mode></div><div id=strip></div><div id=pres></div>\n' + js + EGG_ANIM_JS + '</html>')
out = os.path.join(HERE, '..', '..', 'elements', 'christendom-egg-animated.html')
open(out, 'w').write(html)
print('wrote', os.path.relpath(out), len(html), 'bytes')
