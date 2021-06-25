from ratings import Ratings
from stats import Stats

class Player:
    def __init__(self, name, position, ratings):
        self.name = name
        self.position = position
        self.ratings = ratings
        self.stats = Stats()
        
    def __str__(self):
        POSITIONS = ["PG","SG","SF","PF","C"]
        return (
            f"Name: {self.name}\n"
            f"Position: {POSITIONS[self.position]}\n"
            f"Ratings: {str(self.ratings)}\n"
            f"Stats: {str(self.stats)}"
        )
