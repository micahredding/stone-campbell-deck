# Build Chapter 3, part two with the Week 3 engine:  python3 decks/src/week3b/build.py  (run from the repo root)
import os, runpy
os.environ['PART'] = '2'
runpy.run_path('decks/src/week3/build.py', run_name='__main__')
