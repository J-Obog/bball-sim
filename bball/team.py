from bball.player import Player
from bball.stats import Stats
import json

class Team:
    def __init__(self, name, colors, players):
        self.name = name
        self.colors = colors
        self.players = []
        self.stats = Stats()

    @classmethod
    def loadFromFile(path):
        pass
        #return Team()