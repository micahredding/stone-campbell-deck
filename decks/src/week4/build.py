# Chapter 4 builds with the Chapter 3 engine: PART=4 python3 decks/src/week3/build.py
import os, runpy
os.environ['PART'] = '4'
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'week3', 'build.py'), run_name='__main__')
