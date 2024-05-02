import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import pandas as pd
from player import Player



def write_player_html_to_file(player_id, soup) -> None:
    with open(f'HTML\\{player_id}_info.html', 'wb') as file:
        file.write(soup.prettify('utf-8'))


def get_player(player_id, csv = False, excel = False, batter = True) -> Player:
    base_site = f"https://www.baseball-reference.com/players/{player_id[0]}/{player_id}.shtml"

    response = requests.get(base_site)
    print(response) #200 is good, 404 is bad

    html = response.content

    soup = BeautifulSoup(html, "html.parser")

    if batter: 
        main_content = soup.find('div', id = 'div_batting_standard')
        columns = 27
    else: 
        main_content = soup.find('div', id = 'div_pitching_standard')
        columns = 33

    #Get all of the column names
    td_elements = main_content.find_all('td', {'class': ['left', 'right']})[1:columns]

    #Get data stat values
    data_stat_values = [td.get('data-stat') for td in td_elements]

    # Filter out None values
    data_stat_values = [value for value in data_stat_values if value is not None]

    #with open(f'{player_id}_stats.html', 'wb') as file:
        #file.write(main_content.prettify('utf-8'))

    player_info = pd.DataFrame()

    player_info["Year"] = [year.text for year in main_content.find_all('th', {"data-stat": "year_ID"})][1:]
    length = len(player_info["Year"])


    try:
        for data_stat_value in data_stat_values:
            player_info[data_stat_value] = [value.text for value in main_content.find_all(lambda tag: tag.name in ['td', 'th'] and tag.get('data-stat') == data_stat_value)][1:length+1]

        # Removing minor leagues from rows
        for i in range(length-1, -1, -1):
            if '-min' in player_info["team_ID"][i]:
                player_info = player_info.drop(i, axis='index')


        # Removing partial seasons (may or may not do this) 
        #for i in range(length-1, -1, -1):
            #print(player_info["Year"][i-1])
            #if i>0 and player_info["Year"][i] == player_info["Year"][i-1]:
                    #player_info = player_info.drop(i, axis='index')
                #continue
            #continue

    finally:

        write_player_html_to_file(player_id, soup)

        player = Player()
        player.load_data(player_info)
        return player




#Including this option here for more convenient testing
if __name__ == '__main__':
    name = []
    while len(name) < 2:
        name = input('Enter the player\'s name: ').split(' ')

    last = name[1].lower() if len(name[1]) <= 5 else name[1][:5].lower()
    first = name[0][:2].lower()
    id = last + first + '01'

    csv = (input('Do you want a CSV file? (1 for yes) ') == '1')
    excel = (input('Do you want an Excel file? (1 for yes) ') == '1')

    batter = (input('Is your player a batter? (1 for yes) ') == '1')

    if batter:
        get_player(id, csv, excel, batter = True)
    else:
        get_player(id, csv, excel, batter = False)