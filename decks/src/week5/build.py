# Chapter 5 is a map deck: this runs decks/src/week5map/build.py, which writes
# decks/chapter5.html (Chapter 5) and decks/chapter6.html (Chapter 6),
# each with its .json sidecar.
import os, runpy
runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'week5map', 'build.py'), run_name='__main__')
