# This class stores data for a single baseball player

# Position: 1 = pitcher, 2 = catcher, 3 = first base, etc.
# https://en.wikipedia.org/wiki/Baseball_positions

# Id corresponds to webpage name for Baseball Reference profile
# Format: lastname[:5] + firstname[:2] + 01 (or 02, 03, etc. if others have the same ID)
# Ex: Clayton Kershaw -> kershcl01 -> https://www.baseball-reference.com/players/k/kershcl01.shtml

class Player:

    def __init__(self) -> None:
        self.name = "Baseball Player"
        self.id = "playeba01"
        self.position = 1