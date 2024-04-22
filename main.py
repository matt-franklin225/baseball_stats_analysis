# From player_scraper we get the get_player method
from player_scraper import *


if __name__ == '__main__':
    name = []
    while len(name) < 2:
        name = input('Enter the player\'s name: ').split(' ')

    last = name[1].lower() if len(name[1]) <= 5 else name[1][:5].lower()
    first = name[0][:2].lower()
    id = last + first + '01'

    #id = input("Enter MLB player ID: ")
    csv = (input('Do you want a CSV file? (1 for yes) ') == '1')
    excel = (input('Do you want an Excel file? (1 for yes) ') == '1')

    batter = (input('Is your player a batter? (1 for yes) ') == '1')

    if batter:
        get_player(id, csv, excel, batter = True)
    else:
        get_player(id, csv, excel, batter = False)