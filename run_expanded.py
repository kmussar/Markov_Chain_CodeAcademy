# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:26:18 2018

@author: kmuss
"""
import random

from markov_python.cc_markov_expanded import MarkovChain
mc = MarkovChain()

mc.add_file('marvel_storylines_from_urls.txt')

chain_head = []
marvel_characters = ['thor', 'iron man', 'black panther']
idx = random.randint(0, len(marvel_characters)-1)
#print(marvel_characters[idx])
chain_head = marvel_characters[idx].split(' ')
#print("chain_head")
#print(chain_head)
      
story = mc.generate_text(chain_head, 25)
story = ' '.join(story)

print('Next from the Marvel Cinematic Universe: ')
print(story + '...')