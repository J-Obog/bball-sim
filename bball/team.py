from bball.player import Player
import csv

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.on_court = self.players[:5]

    def sum_stats(self, stat):
        return sum([p.stats[stat] for p in self.players]) 

    @staticmethod
    def from_file(path):
        players = []
        with open(path) as csv_file:
            csv_data = csv.reader(csv_file)
            for r in csv_data:
                players.append(
                    Player(r[0], int(r[1]), list(map(int, r[2:])))
                )
        return Team(path[:-4], players)