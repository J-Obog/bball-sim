from bball.player import Player
from bball.stats import Stats
import json

class Team:
    def __init__(self, name, colors, players):
        self.name = name
        self.colors = colors
        self.players = players
        self.stats = Stats()

    @staticmethod
    def loadFromFile(path):
        players = []
        file = open(path)
        data = json.load(file)

        for player in data['players']:
            players.append(
                Player(
                    player['name'],
                    player["pos"],
                    player["3p"],
                    player["2p"],
                    player["ft"],
                    player["ast"],
                    player["reb"],
                    player["tov"],
                    player["blk"],
                    player["stl"],
                    player["fl"]
                )
            )
            
        file.close()
        return Team(data['name'], data['colors'], players)