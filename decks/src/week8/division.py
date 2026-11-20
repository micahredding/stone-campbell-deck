# Chapter 8, "Every historic division at one table" (Micah, 2026-11-20): a replay of Chapter 3's egg (Christendom's
# search for unity, 325 to today), then three picture slides, God / clergy and authority / the sacraments, each
# answered by the matching point of contention at Lexington.
# Images (decks/src/week8/images/, see SOURCES.md): egg frames from decks/elements/egg-frames (our own, Chapter 3);
# the rest from Chapter 6's set (decks/src/chapter6/images/credits_conflict.md) and the Nicaea icon (Wikimedia Commons).
import base64, os
_H = os.path.dirname(os.path.abspath(__file__))
def _b64(rel):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(_H, 'images', rel), 'rb').read()).decode()

EGG = ['egg/egg-%02d.jpg' % i for i in (0, 1, 2, 3, 5, 7, 9, 11, 13, 14, 15, 16)]
STEP = 1.0   # seconds per frame

def egg_replay():
    frames = ''.join('<img class=eggf src="%s" alt="" style="z-index:%d;animation-delay:%.1fs">' % (_b64(f), i + 1, i * STEP) for i, f in enumerate(EGG))
    return ('<section class="slide" style="padding:0"><style>'
            '.eggbox{position:relative;width:min(96vw,170vh);aspect-ratio:16/9}'
            '.eggbox .eggf{position:absolute;inset:0;width:100%;height:100%;opacity:0}'
            '.eggbox .eggf:first-child{opacity:1}'
            '.slide.on .eggbox .eggf{animation:eggshow .35s ease forwards}'
            '@keyframes eggshow{to{opacity:1}}</style>'
            '<div class=eggbox>' + frames + '</div>'
            '<aside class=notes>Plays by itself (about %d seconds): Chapter 3&rsquo;s egg, Christendom&rsquo;s search for unity, from one church through Nicaea, Chalcedon, 1054, Worms, the Reformation and the Scottish splits, to today: too many divisions to count. Every split was made by an instrument meant to secure unity (a creed, a council, a confession). Now: the same three kinds of division, one at a time, and what each looked like at Lexington.</aside></section>' % int(len(EGG) * STEP))

def _pic(img, year, cap, h='46vh'):
    return ('<div class=frag style="flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;padding:0 1vw">'
            '<img src="%s" alt="" style="height:%s;width:auto;max-width:100%%;object-fit:cover;border:1px solid rgba(201,162,74,.55);box-shadow:0 6px 24px rgba(0,0,0,.6)">'
            '<div style="font-family:\'IM Fell English\',Georgia,serif;color:var(--gold);font-size:clamp(24px,4.2vmin,52px);margin-top:1.6vmin;line-height:1.1">%s</div>'
            '<div style="font-family:Spectral,Georgia,serif;color:var(--bone);font-size:clamp(16px,2.6vmin,32px);line-height:1.25;margin-top:.6vmin;max-width:28vw">%s</div></div>' % (_b64(img), h, year, cap))

def _div(eyebrow, title, pics, lex, notes, h='46vh'):
    return ('<section class="slide" style="padding:3vmin 3vw 6vmin"><div class=eyebrow>%s</div>'
            '<h2 style="max-width:none;margin-bottom:1.6vmin">%s</h2>'
            '<div style="display:flex;align-items:flex-start;justify-content:center;width:94vw">%s</div>'
            '<div class="sub frag" style="margin-top:2.4vmin;max-width:80vw;font-size:clamp(20px,3.4vmin,42px);color:var(--bone)"><span style="color:var(--gold)">At Lexington:</span> %s</div>'
            '<aside class=notes>%s</aside></section>' % (eyebrow, title, ''.join(_pic(*p, h=h) for p in pics), lex, notes))

def slides():
    return [
        egg_replay(),
        _div('Two thousand years of division &middot; 1', 'God',
             [('nicaea-icon.jpg', '325 &middot; Nicaea', 'The creed that divided Arius&rsquo;s followers from the church')],
             '&ldquo;Some Reformers still looked upon the Christians as <i>Arians</i>&rdquo;; and some Christians thought the Reformers &ldquo;denied the influence of the Spirit.&rdquo;',
             'Two clicks: the icon, then Lexington. Nicaea (325) condemned Arius: the first great division over who God is, and over Christ. Fifteen centuries later, the same word in Kentucky: the Reformers suspected Stone&rsquo;s Christians of Arianism, because Stone would speak of Christ only in Scripture&rsquo;s words and not the Trinitarian formulas (Williams, p. 450). The Spirit: the Christians feared the Reformers denied the Spirit&rsquo;s work in conversion. Icon: the Fathers of Nicaea with the Nicene Creed, a modern Orthodox icon (Wikimedia Commons, &ldquo;Nicaea icon.jpg&rdquo;); class use, rights to check before the public site.',
             h='54vh'),
        _div('Two thousand years of division &middot; 2', 'Authority and clergy',
             [('hus_degraded.jpg', '1415', 'Hus stripped of his priesthood at Constance'),
              ('luther_bull.jpg', '1520', 'Luther burns the pope&rsquo;s bull'),
              ('ejection.jpg', '1662', 'England ejects some two thousand ministers')],
             'whether &ldquo;no person but a preacher has a right to administer the ordinances,&rdquo; or &ldquo;us common folks&rdquo; too.',
             'Four clicks: three pictures, then Lexington. Who has authority, and who may serve: the question behind 1054 (pope and patriarch) and every Reformation split. Hus degraded (Wylie, <i>History of Protestantism</i>, c. 1870s); Luther burning the bull (Vinkeles, 1783; Rijksmuseum); the Great Ejection, St Bartholomew&rsquo;s Day 1662 (<i>Cassell&rsquo;s</i>, 1865): ministers without episcopal ordination put out. At Lexington: the two congregations split in February 1832 over choosing an elder and who may serve the loaf (H. C. C., MH 1832, p. 192). Stone, 1830: &ldquo;the church may elect, but not ordain.&rdquo;',
             h='40vh'),
        _div('Two thousand years of division &middot; 3', 'The sacraments',
             [('manz_drowning.jpg', '1527 &middot; Zurich', 'Felix Manz drowned for believers&rsquo; baptism'),
              ('marburg.jpg', '1529 &middot; Marburg', 'Luther and Zwingli divide over the Supper')],
             'whether &ldquo;baptism was for the remission of sins&rdquo;; and &ldquo;free or restricted communion.&rdquo;',
             'Three clicks: two pictures, then Lexington. Baptism: the Reformed of Zurich drowned the Anabaptist Felix Manz (Jan Luyken, <i>Martyrs Mirror</i>, 1685). The table: at Marburg Luther and Zwingli agreed on fourteen articles and divided on the fifteenth, the presence in the Supper (Noack, 1867&ndash;69). At Lexington: &ldquo;all did not hold in the same sense that baptism was for the remission of sins&rdquo;; &ldquo;they still differed on the question of free or restricted communion&rdquo; (Williams, p. 450); and how often (Stone: the Reformers &ldquo;insisted also upon weekly communion, which we had neglected&rdquo;).',
             h='46vh'),
    ]
