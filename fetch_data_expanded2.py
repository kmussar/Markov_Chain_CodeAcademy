# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 16:52:16 2018
@author: kmuss
"""
import requests
from bs4 import BeautifulSoup

marvel_movies = {     'iron_man': 'https://www.imdb.com/title/tt0371746/?ref_=nv_sr_1', 
                      'the_incredible_hulk': 'https://www.imdb.com/title/tt0800080/?ref_=nv_sr_1',
                      'iron_man2': 'https://www.imdb.com/title/tt1228705/?ref_=nv_sr_1', 
                      'thor':'https://www.imdb.com/title/tt0800369/?ref_=fn_al_tt_1', 
                      'captain_america_first_avenger':'https://www.imdb.com/title/tt0458339/?ref_=nv_sr_2', 
                      'the_avengers':'https://www.imdb.com/title/tt0848228/?ref_=fn_al_tt_1', 
                      'iron_man3':'https://www.imdb.com/title/tt1300854/?ref_=nv_sr_1',
                      'thor_dark_world':'https://www.imdb.com/title/tt1981115/?ref_=nv_sr_1',
                      'captain_america_winter_soldier':'https://www.imdb.com/title/tt1843866/?ref_=nv_sr_1',
                      'guardians_of_the_galaxy':'https://www.imdb.com/title/tt2015381/?ref_=tt_rec_tti', 
                      'avengers_age_of_ultron':'https://www.imdb.com/title/tt2395427/?ref_=nv_sr_1',
                      'ant_man':'https://www.imdb.com/title/tt0478970/?ref_=nv_sr_2',
                      'captain_america_civil_war':'https://www.imdb.com/title/tt3498820/?ref_=tt_rec_tti',
                      'doctor_strange':'https://www.imdb.com/title/tt1211837/?ref_=tt_rec_tti',
                      'guardians_of_the_galaxy2':'https://www.imdb.com/title/tt3896198/?ref_=tt_rec_tti',
                      'spider_man_homecoming':'https://www.imdb.com/title/tt2250912/?ref_=tt_rec_tti',
                      'thor_ragnarok':'https://www.imdb.com/title/tt3501632/?ref_=tt_rec_tti',
                      'black_panther':'https://www.imdb.com/title/tt1825683/',
                      'avengers_infinity_war':'https://www.imdb.com/title/tt4154756/'
                }

"""
# scrape storylines for all MCU movies and add them to a string. 
storylines_from_urls = ""

for x in marvel_movies: 
    page = requests.get(marvel_movies[x])
    soup = BeautifulSoup(page.content, 'html.parser')
    soup.find(class_="inline canwrap")
    soup.find(itemprop="description")
    x = soup.find(itemprop="description").get_text()
    storylines_from_urls += x 
    #print(storylines_from_urls)
    

# Open a file
f = open("marvel_storylines_from_urls.txt", "w")
f.write(storylines_from_urls)

# Close open file
f.close()
"""

# Set up a loop to gather characters from all of the movies. 
character_lst = []
for x in marvel_movies:  
    page = requests.get(marvel_movies[x])
    soup = BeautifulSoup(page.content, 'html.parser')
    all_characters = soup.find_all(class_="character")
    # load the first y number of characters from each movie
    for y in range(5): 
        char_name = all_characters[y].get_text()
        # Some characters have aliases, create separate items for each name in the list
        char_name = char_name.split('/')
        # remove whitespace from the text
        for c in char_name:
            c = c.strip()
            character_lst.append(c) 

f = open("marvel_character_lst.txt", "w")
f.write(",".join(character_lst))

# Close open file
f.close()   



