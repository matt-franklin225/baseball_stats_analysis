import copy
import pandas as pd
import numpy as nps

# This class stores data for a single baseball player

# Position: 1 = pitcher, 2 = catcher, 3 = first base, etc.
# https://en.wikipedia.org/wiki/Baseball_positions

# Id corresponds to webpage name for Baseball Reference profile
# Format: lastname[:5] + firstname[:2] + 01 (or 02, 03, etc. if others have the same ID)
# Ex: Clayton Kershaw -> kershcl01 -> https://www.baseball-reference.com/players/k/kershcl01.shtml

class Player:

    classification = 'baseball_player'
    career_stats = None
    yearly_stats = None
    career_panda = None

    def __init__(self, name = "Baseball Player", id = "playeba01", position = 1) -> None:
        self.name = name
        self.id = id
        self.position = position

    def load_info(self, name, id, position) -> None:
        self.name = name
        self.id = id
        self.position = position

    def load_yearly_data(self, new_data: pd.DataFrame) -> None:
        self.yearly_stats = new_data.to_numpy()

    def load_career_data(self, new_data: pd.DataFrame) -> None:
        self.career_panda = new_data
        self.career_stats = new_data.to_numpy()

    def print_yearly_data(self):
        print(self.yearly_stats)

    def print_career_data(self):
        print(self.career_stats)

    def determine_style(self):
        #Simplifying to two possibilities for now
        #categories = ['contact', 'speedster', 'defender', 'utility', 'slugger', 'disciplined', 'power-speed']
        #category_points = [0, 0, 0, 0, 0, 0, 0]
        categories = ['Contact', 'Slugger']
        category_points = [self.contact_points(), self.slugger_points()]
        if category_points[0] < category_points[1]: self.classification = 'Slugger'
        else: self.classification = 'Contact'
        print('Contact points: ' + str(category_points[0]))
        print('Slugger points: ' + str(category_points[1]))
        print('Player type: ' + self.classification)

    def contact_points(self):
        stats = self.career_panda
        points = 0
        points += float(stats["batting_avg"].iloc[0])
        points += (1-(int(stats["SO"].iloc[0]) / int(stats["AB"].iloc[0])))/4
        return points

    def slugger_points(self):
        stats = self.career_panda
        points = 0
        points += ((int(stats["HR"].iloc[0]) / int(stats["AB"].iloc[0])))*8
        points += ((int(stats["SO"].iloc[0]) / int(stats["AB"].iloc[0])))/2
        return points

    def disciplined_points(self):
        stats = self.career_panda
        points = 0
        points += ((int(stats["BB"].iloc[0]) / int(stats["PA"].iloc[0])))*4
        points += (1-(int(stats["SO"].iloc[0]) / int(stats["AB"].iloc[0])))/4
        return points

    def speedster_points(self):
        stats = self.career_panda
        points = 0
        points += ((int(stats["SB"].iloc[0]) / int(stats["PA"].iloc[0])))*8
        points += float(stats["batting_avg"].iloc[0])
        return points