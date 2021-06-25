from bball.stats import Stats
from random import randint

class Player:
    def __init__(self, name, pos, _3p, _2p, ft, ast, reb, tov, blk, stl, fl):
        self.name = name
        self.pos = pos
        self._3p = _3p
        self._2p = _2p
        self.ft = ft
        self.ast = ast
        self.reb = reb
        self.tov = tov
        self.blk = blk
        self.stl = stl
        self.fl = fl
        self.stats = Stats()
    
    def shoot3p(self):
        r = randint(0, 100)
        return r < self.ratings._3p

    def offensiveRating(self):
        return 0

    def defensiveRating(self):
        return 0
