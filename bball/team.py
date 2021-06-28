from bball.player import Player
from bball.stats import Stats
import json

class Team:
    def __init__(self, name, colors, players):
        self.name = name
        self.colors = colors
        self.players = players
        self.on_court = [player for player in self.players[:5]]
        self.stats = Stats()

    @staticmethod
    def loadFromFile(path):
        players = []
        file = open(path)
        data = json.load(file)

        for player in data['players']:
            players.append(
                Player(
                    name = player["name"], 
                    pos = player["pos"], 
                    _3p = player["3p"], 
                    _2p = player["2p"], 
                    ft = player["ft"], 
                    ast = player["ast"], 
                    reb = player["reb"], 
                    tov = player["tov"], 
                    blk = player["blk"], 
                    stl = player["stl"], 
                    fl = player["fl"]
                )
            )
            
        file.close()
        return Team(data['name'], data['colors'], players)
        