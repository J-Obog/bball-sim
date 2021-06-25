from stats import Stats

class Team:
    def __init__(self, name, players):
        self.name = name
        self.players = players
        self.stats = Stats()
        #ratings
        lineScore = []