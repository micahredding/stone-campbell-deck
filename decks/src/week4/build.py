# Chapter 4 has one deck, the map deck: this runs decks/src/week4map/build.py, which writes
# decks/week4-last-will-map.html (and its .json sidecar). No linear Chapter 4 deck is built.
import os, runpy
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'week4map', 'build.py'), run_name='__main__')
