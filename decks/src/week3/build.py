import re, sys, base64, os
# PART=2 builds Chapter 3, part two (decks/src/week3b/slides.py) with this same engine, styles and images.
PART = os.environ.get('PART', '1')
sys.path.insert(0, {'1': 'decks/src/week3', '2': 'decks/src/week3b', '4': 'decks/src/week4', '5': 'decks/src/week5', 'u': 'decks/src/unity'}[PART])
from slides import S, PATDEFS, CHRISTENDOM_CSS

body='\n\n'.join(S)
EGG = 'eggslide' in body
if EGG:
    sys.path.insert(0, 'decks/src/elements')
    from egg_anim import EGG_ANIM_CSS, EGG_ANIM_JS
for _k,_f in (('IMG_STONE','stone.jpg'),('IMG_SIGNING','signing.jpg'),('IMG_STUMP','stump.jpg'),('IMG_TCAMPBELL','tcampbell.jpg'),('IMG_SHIP','ship.jpg'),('IMG_MAP','map_marked.jpg'),('IMG_TOKEN','token.jpg'),('IMG_GROVE','grove.jpg'),('IMG_WORMSPIC','luther.jpg'),('IMG_MARBURGPIC','marburg.jpg'),('IMG_MANZ','anabaptist_drowning.jpg'),('IMG_EGG','recap_egg.jpg'),('IMG_ACAMPBELL','acampbell.jpg'),('IMG_BRUSHRUN','brushrun.jpg')):
    _dirs = {'4': ['decks/src/week4/'], '5': ['decks/src/week5/', 'decks/src/week2/']}.get(PART, []) + ['decks/src/week3/']   # a chapter's own images first
    _p = next((d+_f for d in _dirs if os.path.exists(d+_f)), 'decks/src/week3/'+_f)
    if _k in body: body=body.replace(_k, 'data:image/jpeg;base64,'+__import__('base64').b64encode(open(_p,'rb').read()).decode())
css=open('decks/src/week3/engine.css').read()
css+= ('\n  /* ---- Week 3 type scale (inherited from Week 2) ---- */\n'
       '  #deck .slide h1{font-size:clamp(52px,11vmin,140px);line-height:1.05}\n'
       '  #deck .slide h2{font-size:clamp(36px,7vmin,90px);line-height:1.12;max-width:22ch}\n'
       '  #deck .slide.sect h2{font-size:clamp(52px,11vmin,130px)}\n'
       '  #deck .slide .sub{font-size:clamp(22px,3.6vmin,44px);max-width:34ch;line-height:1.35}\n'
       '  #deck .slide .eyebrow{font-size:clamp(16px,2.6vmin,30px)}\n'
       + CHRISTENDOM_CSS +
       '  /* ---- the full flow diagram slide ---- */\n'
       '  #deck .flowslide{padding:2vmin 3vmin 6vmin;justify-content:center}#deck .flowslide .eyebrow{margin-bottom:1vmin}\n'
       '  #deck .flowslide svg{width:min(96vw,145vh);height:auto;display:block}\n'
       '  .flowslide .rib{fill:rgba(237,228,211,.13);stroke:rgba(237,228,211,.55);stroke-width:1.2;stroke-linejoin:round}\n'
       '  .flowslide .rib.dying{fill:url(#fade);stroke:none}\n'
       '  .flowslide .breach{fill:var(--ground);stroke:var(--gold-dim);stroke-width:1.5;stroke-dasharray:4 5}\n'
       '  .flowslide .fork{stroke:var(--gold);stroke-width:2.5;stroke-linecap:round}\n'
       '  .flowslide .node{fill:var(--ground);stroke:var(--gold);stroke-width:2.5}.flowslide .node.heal{fill:var(--gold-dim);stroke:var(--gold-dim)}\n'
       '  .flowslide .fx{font-family:"IM Fell English",Georgia,serif;font-size:28px;fill:var(--smoke)}\n'
       '  .flowslide .flab{font-size:19px;fill:var(--bone-dim);paint-order:stroke;stroke:var(--ground);stroke-width:8px;stroke-linejoin:round}\n'
       '  .flowslide .flab .yr{font-family:"IM Fell English SC",Georgia,serif;font-size:21px;letter-spacing:.14em;fill:var(--gold)}\n'
       '  .flowslide .flab .ttl{font-family:"IM Fell English",Georgia,serif;font-style:italic;font-size:27px;fill:var(--bone)}\n'
       '  .flowslide .flab .fsub{font-family:Spectral,Georgia,serif;font-size:19px;fill:var(--bone-dim)}\n'
       '  .flowslide .leaf{font-family:"IM Fell English",Georgia,serif;font-size:18px;fill:var(--bone)}.flowslide .leaf.dim{fill:var(--smoke);font-style:italic;font-size:17px}\n'
       '  .flowslide .trunk{font-family:"IM Fell English SC",Georgia,serif;font-size:19px;letter-spacing:.18em;fill:var(--smoke)}\n')

# one shared gradient for the dying fork ribbons
defs = '<defs><linearGradient id="forkfade" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ede4d3" stop-opacity=".13"/><stop offset="1" stop-color="#ede4d3" stop-opacity="0"/></linearGradient></defs>'
body = body.replace('xmlns="http://www.w3.org/2000/svg"><path class="rib"', 'xmlns="http://www.w3.org/2000/svg">' + defs + '<path class="rib"')

css += ('\n  /* ---- quote litanies (evils, reception) ---- */\n'
        '  #deck .slide .litany{gap:2.2vmin;margin-top:2vmin;max-width:90vw}\n'
        '  #deck .slide .litany .no{font-family:"IM Fell English",Georgia,serif;font-size:clamp(24px,4.3vmin,54px);line-height:1.28;color:var(--bone)}\n'
        '  #deck .slide .litany .no b{color:var(--gold);font-weight:400}\n'
        '  #deck .slide .eyebrow{max-width:70ch;line-height:1.4}\n')

def b64(p):
    with open(p,'rb') as f: return 'data:image/jpeg;base64,'+base64.b64encode(f.read()).decode()
css += '\n  .bgimg.lutherbg{background-image:url("%s");background-position:center 30%%}\n' % b64('decks/src/week3/luther.jpg')
css += '  .slide.bleed .frag.sub{color:var(--bone)}\n'
css += '  #deck .dimbg .bg::after{content:"";position:absolute;inset:0;background:rgba(14,11,9,.78)}\n  #deck .dimbg .bigquote{text-shadow:0 1px 6px rgba(0,0,0,.9)}\n'
css += '  #deck .wormsfull .bigquote{line-height:1.2;font-size:clamp(30px,6.4vmin,78px);max-width:46ch}\n'
css += '  #deck .slide .sub.punch{font-family:"IM Fell English",Georgia,serif;font-style:normal;font-size:clamp(30px,5.4vmin,68px);line-height:1.2;color:var(--gold);max-width:none;margin-top:2.4vmin}\n'
css += '  #deck .rejslide{justify-content:center;gap:0}#deck .rejslide img{display:block;max-height:60vh;max-width:84vw;border-radius:.4vmin;box-shadow:0 1vmin 4vmin rgba(0,0,0,.6)}\n  #deck .rejslide figcaption{font-family:"IM Fell English SC",Georgia,serif;font-size:clamp(11px,1.5vmin,17px);letter-spacing:.1em;color:var(--smoke);margin-top:1vmin;text-align:center}\n  #deck .rejslide h2{max-width:none;margin-top:2.6vmin}\n'
css += '  #deck .slide h2.url{max-width:none;margin-left:auto;margin-right:auto;text-align:center}#deck .siteslide .small{max-width:none}\n'
css += ('  /* ---- larger type, 2026-10-11 ---- */\n'
        '  #deck .slide h2{font-size:clamp(40px,8vmin,104px)}\n'
        '  #deck .slide .sub{font-size:clamp(24px,4.3vmin,52px);max-width:38ch}\n'
        '  #deck .slide .eyebrow{font-size:clamp(17px,3vmin,36px)}\n'
        '  #deck .slide .bigquote.long{font-size:clamp(34px,7.2vmin,88px);max-width:38ch}\n'
        '  #deck .slide .bigquote.xlong{font-size:clamp(26px,5.2vmin,62px);max-width:48ch}\n'
        '  #deck .slide .cite{font-size:clamp(20px,3.3vmin,38px)}\n'
        '  #deck .slide .litany .no{font-size:clamp(26px,5vmin,62px)}\n'
        '  #deck .slide .small{font-size:clamp(19px,3vmin,34px)}\n'
        '  #deck .rejslide figcaption{font-size:clamp(13px,2vmin,24px)}\n'
        '  #deck .slide .litany.tbl .no{font-size:clamp(22px,4.3vmin,54px)}\n'
        '  #deck .slide.wormsfull .bigquote{font-size:clamp(32px,7vmin,86px);max-width:46ch}\n'
        '  #deck .slide .litany.bigl .no{font-size:clamp(30px,6.4vmin,80px);line-height:1.25}\n'
        '  #deck .slide .litany.ideasum .no{font-size:clamp(30px,6.2vmin,78px);line-height:1.2;position:relative;padding-left:1.6em}#deck .slide .litany.ideasum .no>span:first-child{position:absolute;left:0;top:0}\n'
        '  #deck .recapshots{flex-wrap:nowrap}#deck .recapshots .shot{width:min(34vmin,17vw)}#deck .recapshots .shot img{height:26vh!important}\n')
if EGG: css += EGG_ANIM_CSS
if PART == '4':
    css += '  .bgimg.farmbg{background-image:url("%s");background-position:center 55%%}\n' % b64('decks/src/week4/farm.jpg')
    css += '  .bgimg.synodbg{background-image:url("%s");background-position:center 40%%}\n' % b64('decks/src/week4/synod.jpg')
    css += '  .bgimg.justicesbg{background-image:url("%s");background-position:center}\n' % b64('decks/src/week4/justices.jpg')
    css += '  #deck .slide:has(.justicesbg) .bg::after{background:rgba(14,11,9,.58)}\n  #deck .slide:has(.justicesbg) .bigquote{text-shadow:0 1px 8px rgba(0,0,0,.95),0 0 3vmin rgba(0,0,0,.8)}\n'
    css += '  .bgimg.roadbg4{background-image:url("%s");background-position:center 60%%}\n' % b64('decks/src/week4/road.jpg')
    css += '  .bgimg.househbg{background-image:url("%s");background-position:center 40%%;filter:sepia(.35) brightness(.75)}\n' % b64('decks/src/week4/meetinghouse.jpg')
    css += ('  .wmap.all .th{opacity:.85}\n'
            '  #deck .slide .wmap .ms-christ .th{font-size:clamp(22px,4vmin,48px)}#deck .slide .wmap .ms-pri .th{font-size:clamp(36px,7.4vmin,88px)}\n'
            '  #deck .slide .wmap .ms-sec .th,#deck .slide .wmap .ms-pra .th{font-size:clamp(16px,2.8vmin,32px)}#deck .slide .ideasmap .small{font-size:clamp(14px,2.1vmin,24px)}\n')
if PART == '5':
    css += '  .bgimg.wreckbg5{background-image:url("%s");background-position:center 45%%}\n' % b64('decks/src/week2/wreck.jpg')
    css += '  .bgimg.grovebg5{background-image:url("%s");background-position:center 35%%}\n' % b64('decks/src/week3/grove.jpg')
    css += '  .bgimg.synodbg5{background-image:url("%s");background-position:center 40%%}\n' % b64('decks/src/week4/synod.jpg')
    css += '  .bgimg.brushbg{background-image:url("%s");background-position:center 45%%}\n' % b64('decks/src/week5/brushrun.jpg')
    css += '  .bgimg.islaybg{background-image:url("%s");background-position:center 60%%}\n' % b64('decks/src/week2/indaal.jpg')
css += '  #deck .litany .lcite{display:block;font-family:"IM Fell English SC",Georgia,serif;font-style:normal;font-size:.55em;letter-spacing:.1em;color:var(--smoke);margin-top:.3vmin}\n'
import os
if os.path.exists('decks/src/week3/marburg.jpg'):
    css += '  .bgimg.marburgbg{background-image:url("%s");background-position:center 20%%}\n' % b64('decks/src/week3/marburg.jpg')
    css += '  #deck .slide:has(.marburgbg) .credit{background:rgba(14,11,9,.72);padding:.35em .6em;border-radius:.3em}\n'
else:
    css += '  #deck .slide:has(.marburgbg) .credit{display:none}\n'
    print('note: decks/src/week3/marburg.jpg missing; the Marburg slide builds without its painting')

js=open('decks/src/week3/engine.js').read()
K = {'1': 'w3', '2': 'w3b', '4': 'w4', '5': 'w5', 'u': 'wu'}[PART]
js=js.replace("'w1cur'","'%scur'" % K).replace("'w1mode'","'%smode'" % K).replace("'w1strip'","'%sstrip'" % K)
js=js.replace("'w1presenter'","'%spresenter'" % K)
js=js.replace("||'read')","||'present')")

html=('<!doctype html><html><head><meta charset=utf8>'
 '<meta name=viewport content="width=device-width,initial-scale=1">'
 '<title>Our Wild Democracy &middot; ' + {'1': 'Chapter 3 &middot; The Declaration and Address', '2': 'Chapter 3 &middot; The Declaration and Address, part two', '4': 'Chapter 4 &middot; The Last Will and Testament', '5': 'Chapter 5 &middot; Wherever Two or Three Are Gathered', 'u': 'Union, All His Life'}[PART] + '</title>'
 '<link rel=stylesheet href="https://fonts.googleapis.com/css2?family=IM+Fell+English:ital@0;1&family=IM+Fell+English+SC&family=Spectral:ital,wght@0,300;0,400;0,500;1,300;1,400&display=swap">'
 '<style>\n/* ============================================================\n'
 '   THE DECLARATION AND ADDRESS — Week 3 deck\n'
 '   Engine, palette and type inherited from the Week 2 deck.\n'
 '   Started 2026-10-06 with the Christendom sequence (issue / attempt / fork).\n'
 '   ============================================================ */\n'
 + css + '</style></head>\n<body>\n<svg width=0 height=0 style="position:absolute;visibility:visible" aria-hidden=true>' + PATDEFS + '</svg>\n<div id=deck>\n\n' + body +
 '\n\n</div>\n<div id=bar></div><div id=count></div>'
 '<div id=hint>&rarr; / space / click &middot; f fullscreen &middot; n read/present &middot; p presenter window &middot; s notes on THIS screen</div>'
 '<div id=mode></div><div id=strip></div><div id=pres></div>\n' + js + (EGG_ANIM_JS if EGG else '') + '</html>')

out={'1': 'decks/week3-declaration-address.html', '2': 'decks/week3b-declaration-address-part-two.html', '4': 'decks/week4-last-will.html', '5': 'decks/week5-brush-run.html', 'u': 'decks/union-all-his-life.html'}[PART]
open(out,'w').write(html)
print("wrote", out)
print("bytes:", len(html), "=", round(len(html)/1048576,2), "MB")
print("sections:", html.count('<section'))
print("frags:", html.count('class="failure frag')+html.count('class="frag healer')+html.count('class="sub frag'))
