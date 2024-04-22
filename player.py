import copy
import pandas as pd

# This class stores data for a single baseball player

# Position: 1 = pitcher, 2 = catcher, 3 = first base, etc.
# https://en.wikipedia.org/wiki/Baseball_positions

# Id corresponds to webpage name for Baseball Reference profile
# Format: lastname[:5] + firstname[:2] + 01 (or 02, 03, etc. if others have the same ID)
# Ex: Clayton Kershaw -> kershcl01 -> https://www.baseball-reference.com/players/k/kershcl01.shtml

class Player:

    def __init__(self, name = "Baseball Player", id = "playeba01", position = 1) -> None:
        self.name = name
        self.id = id
        self.position = position

    def load_info(self, name, id, position):
        self.name = name
        self.id = id
        self.position = position

    def load_data(self, new_data: pd.DataFrame):
        self.data = new_data.values