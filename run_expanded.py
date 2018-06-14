# -*- coding: utf-8 -*-
"""
Created on Thu May 31 19:26:18 2018

@author: kmuss
"""
import random

from markov_python.cc_markov_expanded import MarkovChain
mc = MarkovChain()

f = open("marvel_character_lst.txt", "r")
raw_character_lst = f.read()
character_lst = raw_character_lst.split(",")

mc.add_file('marvel_storylines_from_urls.txt')

# chain_head = []
marvel_characters = ['thor', 'iron man', 'black panther']
idx = random.randint(0, len(character_lst)-1)
chain_head = character_lst[idx].split(' ')

      
story = mc.generate_text(chain_head, 25)
story = ' '.join(story)

print('Next from the Marvel Cinematic Universe: ')
print(story + '...')
   