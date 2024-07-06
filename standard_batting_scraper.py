import requests
from bs4 import BeautifulSoup, Comment
from urllib.parse import urljoin
import pandas as pd
from player_scraper import *    #Imports the get_player_site(player_id, csv, excel) function

base_site = "https://www.baseball-reference.com/leagues/majors/2024-standard-batting.shtml"

response = requests.get(base_site)
print(response) #200 is good, 404 is bad

html = response.content

soup = BeautifulSoup(html, "html.parser")

with open('2024_player_standard_batting.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))

# Find all HTML comments
comments = soup.find_all(string=lambda text: isinstance(text, Comment))

# Initialize an empty list to store parsed content from comments
player_section = []

# Extract content from comments and parse it separately
for comment in comments:
    # Parse the comment content as HTML
    comment_soup = BeautifulSoup(comment, 'html.parser')
    # Add the parsed content to the list
    player_section.append(comment_soup)

# Initialize an empty list to store the desired elements
player_data = []

# Iterate over each parsed comment
for comment_soup in player_section:
    # Find all <td> elements with the specified "data-stat" value in the comment
    td_elements = comment_soup.find_all('tr', {"class": ["full_table", "full_table non_qual"]})
    # Append the found <td> elements to the list of desired elements
    player_data.extend(td_elements)


#Get all the player IDs
player_ids = []

# Iterate over each parsed comment
for player in player_data:
    # Find all <td> elements
    player_details = player.find('td')
    id = player_details.get('data-append-csv')

    player_ids.append(id)


data_stat_values = [td.get('data-stat') for td in player_data]






# Filter out None values
data_stat_values = [value for value in data_stat_values if value is not None]

print(data_stat_values)

player_info = pd.DataFrame()

player_info["Year"] = [year.text for year in soup.find_all('th', {"data-stat": "year_ID"})][1:]
length = len(player_info["Year"])


for data_stat_value in data_stat_values:
    player_info[data_stat_value] = [value.text for value in soup.find_all(lambda tag: tag.name in ['td', 'th'] and tag.get('data-stat') == data_stat_value)][1:length+1]