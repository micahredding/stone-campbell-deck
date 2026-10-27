#!/usr/bin/env python3
"""Build research/wright-working-model.md ("N. T. Wright as Restorationist") from the
research database note 'Wright as Restorationist.md'. Each ## and ### section becomes a
collapsed <details> block, so the page opens on the outline of the argument.
Usage: python3 research/tools/build_wright_page.py [path-to-database-note]"""
import os, re, sys

DB = os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/Documents/3/research/"
    "stone-campbell-research/10 Research Projects/The Church as Working Model (Wright)/"
    "Wright as Restorationist.md")
OUT = os.path.join(os.path.dirname(__file__), "..", "wright-working-model.md")

CONTROLS = '''<style>
details.sec { border-top: 1px solid #d0d7de; padding: .4em 0; }
details.sec > summary { cursor: pointer; font-size: 1.35em; font-weight: 600; }
details.sub { margin: .3em 0 .3em 1em; }
details.sub > summary { cursor: pointer; font-size: 1.1em; font-weight: 600; }
</style>
<p><button onclick="var o=this.dataset.open!=='1';document.querySelectorAll('details').forEach(function(d){d.open=o});this.dataset.open=o?'1':'0';this.textContent=o?'Collapse all':'Expand all';">Expand all</button></p>
'''

def build(src):
    src = re.sub(r'(?s)^---\n.*?\n---\n', '', src)                       # Obsidian front matter
    src = re.sub(r'\[\[([^\]|]+)\|([^\]]+)\]\]', r'\2', src)             # [[target|label]]
    src = re.sub(r'\[\[([^\]]+)\]\]', lambda m: m.group(1).split('/')[-1], src)
    first = src.index("\n## ")
    intro, body = src[:first].strip(), src[first:]
    out, h2, h3 = [], False, False
    def close(level):
        nonlocal h2, h3
        if h3: out.append("\n</details>\n"); h3 = False
        if level == 2 and h2: out.append("\n</details>\n"); h2 = False
    for line in body.split("\n"):
        if line.strip() == "---":
            continue
        m = re.match(r'^(##|###) (.+)$', line)
        if m:
            level = len(m.group(1)); close(level)
            cls = "sec" if level == 2 else "sub"
            out.append(f'<details class="{cls}" markdown="1">\n<summary>{m.group(2)}</summary>\n')
            if level == 2: h2 = True
            else: h3 = True
            continue
        out.append(line)
    close(2)
    return intro + "\n\n" + CONTROLS + "\n".join(out).rstrip() + "\n"

if __name__ == "__main__":
    src = open(sys.argv[1] if len(sys.argv) > 1 else DB).read()
    open(OUT, "w").write(build(src))
    print("wrote", os.path.normpath(OUT))
