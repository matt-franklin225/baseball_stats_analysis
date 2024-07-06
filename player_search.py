# From player_scraper we get the get_player method
from player_scraper import *

def introduction() -> None:
    print("Hello, and welcome to my baseball statistics analysis project. ")
    print("I hope you enjoy it and find it useful! --Matt \n")


def get_player_info_from_id(id) -> tuple[str, str, str]:
    response = requests.get(f"https://www.baseball-reference.com/players/{id[0]}/{id}.shtml")
    soup = BeautifulSoup(response.content, "html.parser")
    profile = soup.find('div', id = 'meta')
    name = profile.find('h1').text.strip('\n')
    positions = profile.find('p').text[11:].strip()

    (debut, last_game) = (None, None)
    info = profile.find_all('p')
    for item in info:
        if item.text.startswith("Debut:"):
            debut = item.text.split()[3]
        if item.text.startswith("Last Game:"):
            last_game = item.text.split()[4]
            break

    if debut == None:
        years = ''
    elif last_game == None:
        years = f'{debut}-'
    else:
        years = f'{debut}-{last_game}'

    return (name, positions, years)


def print_player(id, name, positions, years):
    print(f'{id[-1]}. {name} ({positions}) {years}')


def find_player_id_and_position() -> str:
    player_id = ''
    position = ''
    while player_id == '':
        input_name = []
        while len(input_name) < 2:
            input_name = input('Enter the player\'s name: ').split(' ')

        last = input_name[1].lower() if len(input_name[1]) <= 5 else input_name[1][:5].lower()
        first = input_name[0][:2].lower()
        id_start = last + first + '0'
        num = 1
        response = 200
        player_options = []
        temp_id = id_start + '1'
        while response == 200:
            print(temp_id)
            base_site = f"https://www.baseball-reference.com/players/{temp_id[0]}/{temp_id}.shtml"
            response = requests.get(base_site).status_code
            print(response)
            if response == 200:
                (name, positions, years) = get_player_info_from_id(temp_id)
                player_options.append([temp_id, name, positions, years])
                print(player_options)
                num += 1
                temp_id = id_start + str(num)

        if len(player_options) == 0:
            print("Sorry, couldn't find that player")
            continue
        elif len(player_options) == 1:
            print_player(id_start + '1', name, positions, years)
            ans = input('Is this your player? (Enter 1 if yes) ')
            if ans == '1':
                player_id = id_start + '1'
                break
        else:
            for i in range(len(player_options)):
                print_player(player_options[i][0], player_options[i][1], player_options[i][2], player_options[i][3])
            ans = input("Enter your player's number (Or 0 if player not present) ")
            if int(ans) >= 1 and int(ans) <= len(player_options) + 1:
                player_id = id_start + ans
                position = player_options[int(ans)-1][2]
                break
        
    return player_id, position


def search_player(id):
    player = get_player(id)
    return player.career_stats
    #return {"player_id": id, "stats": {"hits": 100, "home_runs": 25, "avg": 0.320}}



if __name__ == '__main__':
    introduction()

    (id, position) = find_player_id_and_position()

    print(f'ID: {id}, Position: {position}')

    batter = False
    if batter:
        player = get_player(id, 0, 0, batter = True)
    else:
        player = get_player(id, 0, 0, batter = False)