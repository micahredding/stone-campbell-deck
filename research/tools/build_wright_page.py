#!/usr/bin/env python3
"""Build research/wright-working-model.md from the research database's
'Wright and Stone-Campbell Side by Side.md'. Each ## and ### section becomes a
collapsed <details> block so the page opens on the outline of the argument.
Usage: python3 research/tools/build_wright_page.py [path-to-database-note]"""
import os, re, sys

DB = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/Documents/3/research/"
    "stone-campbell-research/10 Research Projects/The Church as Working Model (Wright)/"
    "Wright and Stone-Campbell Side by Side.md")
OUT = os.path.join(os.path.dirname(__file__), "..", "wright-working-model.md")

INTRO = '''# The church as working model of new creation: Wright and Stone-Campbell, side by side

N. T. Wright argues that the church is "the small working model of new creation"; that its substance is unity; that unity has to be visible; that a visibly united, many-coloured church is the sign to the principalities and powers (Eph 3:10); and that it draws the world. Below, his language is set beside the matching language of Thomas and Alexander Campbell, Barton Stone, the *Last Will and Testament*, and Cane Ridge. Most practices (singing, gathering, scripture, the table) are sub-points under the step they serve; a closing Practices section holds the Supper as foretaste and the one loaf.

Wright's sources: *God's Homecoming* (HarperOne, 2025), especially ch. 13, "The Polychrome Church as the Sign to the Powers"; *The Vision of Ephesians* (SPCK, 2025); *Simply Christian* (HarperOne, 2006). The full research notes, with every quotation in context, are in the class research database (`10 Research Projects/The Church as Working Model (Wright)/`).

<style>
details.sec { border-top: 1px solid #d0d7de; padding: .4em 0; }
details.sec > summary { cursor: pointer; font-size: 1.35em; font-weight: 600; }
details.sub { margin: .3em 0 .3em 1em; }
details.sub > summary { cursor: pointer; font-size: 1.1em; font-weight: 600; }
details table { margin-top: .6em; }
</style>
<p><button onclick="var o=this.dataset.open!=='1';document.querySelectorAll('details').forEach(function(d){d.open=o});this.dataset.open=o?'1':'0';this.textContent=o?'Collapse all':'Expand all';">Expand all</button></p>

'''

def build(src):
    body = src[src.index("**Citations.**"):].replace("Full Wright context is in [[Quotations]].", "")
    # move the citations key and status note to a collapsed section at the end,
    # so the page opens straight onto the outline of the argument
    first = body.index("\n## ")
    key, body = body[:first].strip(), body[first:]
    key = re.sub(r'\n\s*---\s*$', '', key)
    body = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', body)
    body = re.sub(r'\[\[([^\]]+)\]\]', lambda m: m.group(1).split('/')[-1], body)
    body = body.replace("(see Sources)", "(see the research database's Sources note)")
    out, h2, h3 = [], False, False
    def close(level):
        nonlocal h2, h3
        if h3: out.append("\n</details>\n"); h3 = False
        if level == 2 and h2: out.append("\n</details>\n"); h2 = False
    for line in body.split("\n"):
        if line.strip() == "---":
            continue  # section rules are replaced by the details borders
        m = re.match(r'^(##|###) (.+)$', line)
        if m:
            level = len(m.group(1))
            close(level)
            cls = "sec" if level == 2 else "sub"
            out.append(f'<details class="{cls}" markdown="1">\n<summary>{m.group(2)}</summary>\n')
            if level == 2: h2 = True
            else: h3 = True
            continue
        out.append(line)
    close(2)
    out.append('<details class="sec" markdown="1">\n<summary>About the citations</summary>\n\n' + key + "\n\n</details>")
    return INTRO + "\n".join(out).rstrip() + "\n"

if __name__ == "__main__":
    src = open(sys.argv[1] if len(sys.argv) > 1 else DB).read()
    open(OUT, "w").write(build(src))
    print("wrote", os.path.normpath(OUT))
