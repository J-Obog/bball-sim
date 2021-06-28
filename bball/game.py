from time import sleep 
from random import randint

class Game:
    def __init__(self, teams, site):
        self.site = site
        self.teams = teams
        self.off_team = randint(0,1)
        self.period = 1
        self.game_clock = 12*60
        self.shot_clock = 24
        self.events = []

    def run(self):
        pass

    def sim_possession(self):
        pass

    def save(self, path):
        pass