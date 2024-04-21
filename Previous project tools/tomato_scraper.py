'''
Program to retrieve movie information from an article on action movies on Rotten Tomatoes
'''

import requests
from bs4 import BeautifulSoup
import pandas as pd

#Get data
base_site = "https://editorial.rottentomatoes.com/guide/140-essential-action-movies-to-watch-now/"
response = requests.get(base_site)

#Make HTML file
html = response.content
soup = BeautifulSoup(html, 'lxml')
#Cutting this part out cuz lag
#with open('Rotten_tomatoes_page-2_LXML_Parser.html', 'wb') as file:
    #file.write(soup.prettify('utf_8'))

#Retrieve relevant divs
divs = soup.find_all('div', {'class': 'col-sm-18 col-full-xs countdown-item-content'}) #

#Get headings
headings = [div.find("h2") for div in divs]

#Get names
movie_names = [heading.find('a').string for heading in headings]

#Get years
years = [heading.find('span', class_ = 'start-year').string for heading in headings]
years = [year.strip('()') for year in years]
years = [int(year) for year in years]

#Get scores
scores = [heading.find('span', class_ = 'tMeterScore').string for heading in headings]

#Get consensus
consensus = [div.find("div", {"class": "info critics-consensus"}) for div in divs]
common_phrase = "Critics Consensus: "
common_len = len(common_phrase)
consensus_text = [con.text[common_len:] if con.text.startswith(common_phrase) else con.text for con in consensus]

#Get directors
directors = [div.find("div", {"class": "info director"}) for div in divs]
final_directors = [None if director.find("a") is None else director.find("a").string for director in directors]

#Get casts
casts = [div.find("div", {"class": "info cast"}) for div in divs]
better_casts = [[group.string for group in cast.find_all("a")] for cast in casts]
final_casts = [", ".join(cast) for cast in better_casts]

#Get adjusted scores
a_scores = [div.find("div", {"class": "info countdown-adjusted-score"}) for div in divs]
a_phrase = "Adjusted Score: "
a_len = len(a_phrase)
adjusted_scores = [a.text[a_len:] if a.text.startswith(a_phrase) else a.text for a in a_scores]

#Get synopses
synopses = [div.find("div", {"class": "info synopsis"}) for div in divs]
s_phrase = "Synopsis: "
s_len = len(s_phrase)
final_synopses = [s.text[s_len:] if s.text.startswith(s_phrase) else s.text for s in synopses]


#Create and populate data frame
pd.set_option('display.max_colwidth', None) #Allows columns to fit longer strings
movies_info = pd.DataFrame()
movies_info["Movie Title"] = movie_names
movies_info["Year"] = years
movies_info["Score"] = scores
movies_info["Adjusted Score"] = adjusted_scores
movies_info["Director"] = final_directors
movies_info["Synopsis"] = final_synopses
movies_info["Cast"] = final_casts
movies_info["Consensus"] = consensus_text

#Export data
movies_info.to_csv("movies_info.csv", index = False, header = True)
movies_info.to_excel("movies_info.xlsx", index = False, header = True)