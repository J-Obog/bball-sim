from random import randint
import bball.constants as C 

class Player:
    def __init__(self, name, pos, ratings):
        self.name = name
        self.pos = pos
        self.ratings = ratings
        self.stats = [0 for s in range(len(C.PLAYER_STATS))]