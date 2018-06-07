# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:26:18 2018

@author: kmuss
"""

from markov_python.cc_markov import MarkovChain
mc = MarkovChain()

mc.add_file('marvel_storylines_from_urls.txt')

story = mc.generate_text(20)
story = ' '.join(story)

print('Next from the Marvel Cinematic Universe: ')
print(story + '.')