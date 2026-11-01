# Chapter 5 is a map deck: this runs decks/src/week5map/build.py, which writes
# decks/week5-brush-run-map.html (session one) and decks/week5b-brush-run-map.html (session two),
# each with its .json sidecar.
import os, runpy
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'week5map', 'build.py'), run_name='__main__')
