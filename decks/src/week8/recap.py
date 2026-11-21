# Chapter 8 recap with pictures (Micah, 2026-11-21): one image slide per recap point. The layout: two scenes side by
# side, filling the slide, and a portrait superimposed in the middle; a caption band along the bottom.
# Images in decks/src/week8/images/ (see SOURCES.md).
import base64, os
_H = os.path.dirname(os.path.abspath(__file__))
def _b64(rel):
    return 'data:image/jpeg;base64,' + base64.b64encode(open(os.path.join(_H, 'images', rel), 'rb').read()).decode()

def pair(left, left_label, right, right_label, portrait, year, caption, notes, credit='', lpos='center', rpos='center'):
    half = ('<div style="position:relative;flex:1;overflow:hidden">'
            '<img src="%s" alt="" style="width:100%%;height:100%%;object-fit:cover;object-position:%s;filter:sepia(.25) brightness(.82)">'
            '<div style="position:absolute;z-index:3;left:0;right:0;bottom:24vh;text-align:center;font-family:\'IM Fell English\',Georgia,serif;font-style:italic;'
            'color:var(--bone);font-size:clamp(26px,4.6vmin,58px);text-shadow:0 2px 12px rgba(0,0,0,1)"><span style="background:rgba(14,11,9,.62);padding:.08em .6em;border-radius:.3em;color:#ede4d3">%s</span></div></div>')
    return ('<section class="slide" style="padding:0">'
            '<div style="position:absolute;inset:0;display:flex;gap:.5vmin;background:#0e0b09">'
            + half % (_b64(left), lpos, left_label) + half % (_b64(right), rpos, right_label) +
            '</div>'
            '<div style="position:absolute;inset:0;background:linear-gradient(to bottom,rgba(14,11,9,.15) 0%%,rgba(14,11,9,0) 40%%,rgba(14,11,9,.55) 72%%,rgba(14,11,9,.95) 100%%)"></div>'
            '<img src="%s" alt="" style="position:absolute;left:50%%;top:42%%;transform:translate(-50%%,-50%%);height:48vh;aspect-ratio:600/731;object-fit:cover;'
            'border-radius:50%%;border:.6vmin solid var(--gold);box-shadow:0 0 0 .5vmin #0e0b09,0 1.6vmin 5vmin rgba(0,0,0,.85)">' % _b64(portrait) +
            '<div style="position:absolute;left:0;right:0;bottom:3.5vh;text-align:center">'
            '<div style="font-family:\'IM Fell English SC\',Georgia,serif;color:var(--gold);letter-spacing:.12em;font-size:clamp(26px,4.6vmin,58px)">%s</div>'
            '<div style="font-family:\'IM Fell English\',Georgia,serif;color:var(--bone);font-size:clamp(26px,4.8vmin,60px);line-height:1.15">%s</div>'
            '%s</div>'
            '<aside class=notes>%s</aside></section>' % (year, caption,
                ('<div style="font-family:Spectral,Georgia,serif;color:var(--bone-dim);font-size:clamp(10px,1.5vmin,18px);margin-top:.8vmin">%s</div>' % credit) if credit else '',
                notes))

def slides():
    return [
        pair('recap-cane-ridge-revival-milbert-1819.jpg', 'Revival',
             'recap-cane-ridge-sacrament-1854.jpg', 'Communion',
             'stone-biography-1847.jpg', '1801 &middot; Cane Ridge', 'Thousands at one table',
             'Chapter 1. August 1801: a communion festival at Barton Stone&rsquo;s Cane Ridge meetinghouse, Bourbon County, Kentucky; thousands came, Presbyterians, Methodists and Baptists preached, and the Lord&rsquo;s Supper was served at the heart of it (Chapter 1: a Scottish-style communion season). Revival on the left, the sacrament on the right; Stone between them. Images: J. Milbert, &ldquo;Camp Meeting of the Methodists in N. America&rdquo; (1819); &ldquo;Sacramental Scene in a Western Forest&rdquo; (P. S. Duval, lith., 1854; Library of Congress); Stone, frontispiece of his <i>Biography</i> (1847), signed &ldquo;Once more, farewell.&rdquo; All public domain.',
             credit='Milbert, 1819 &middot; &ldquo;Sacramental Scene in a Western Forest,&rdquo; 1854 &middot; Stone, from his <i>Biography</i>, 1847',
             lpos='center 40%', rpos='center 55%'),
        pair('recap-ireland-ballynahinch-1798.jpg', 'Ulster, 1798',
             'recap-ireland-cruikshank-1845.jpg', 'Houses wrecked by night',
             'tcampbell-oval.jpg', 'Ireland &middot; 1790s', 'Thomas Campbell: union in a land at war',
             'Thomas Campbell, a Seceder minister at Ahorey near Rich Hill, County Armagh, worked to reunite the Burgher and Anti-Burgher Seceders while Ulster burned around him. Richardson: &ldquo;his ministry in Ireland extended through all the years of those civil commotions which issued in the rebellion of 1798.&rdquo; The Orange society, formed in Armagh in 1795, set out &ldquo;to drive by threats and nocturnal outrages the entire Catholic peasantry from the country&rdquo;; Defenders and Peep-o&rsquo;-Day Boys went about &ldquo;in the night searching houses for arms&rdquo;; the United Irishmen swore their members to a republic. He kept out of all of it. The story to tell: during the rebellion he was preaching when the meetinghouse &ldquo;was suddenly surrounded by a troop of Welsh horse, notorious for their severities.&rdquo; The captain marched up the aisle. An elder called out, &ldquo;Pray, sir!&rdquo; and Campbell began the forty-sixth Psalm: &ldquo;Thou, O God, art our refuge and strength, a very present help in trouble. Therefore will not we fear&hellip;&rdquo; The captain bowed his head, listened to the end, and rode away with his troop (Richardson, <i>Memoirs</i> I, pp. 42&ndash;44). Images: Thomas Robinson, <i>The Battle of Ballynahinch</i> (County Down, June 13, 1798; c. 1798&ndash;1800); George Cruikshank, &ldquo;Rebels destroying a house and furniture,&rdquo; for W. H. Maxwell, <i>History of the Irish Rebellion in 1798</i> (1845); Thomas Campbell, engraved portrait (Chapters 2&ndash;3). Public domain.',
             credit='Robinson, <i>Battle of Ballynahinch</i>, 1798 &middot; Cruikshank, for Maxwell&rsquo;s <i>Irish Rebellion</i>, 1845 &middot; Thomas Campbell',
             lpos='center 60%', rpos='center 45%'),
    ]
