 

class Ratings:
    def __init__(self):
        self._3p = 25
        self._2p = 25
        self.ft = 25
        self.ast = 25
        self.reb = 25
        self.tov = 25
        self.blk = 25
        self.stl = 25
        self.fl = 25

    def offensiveRating(self):
        return 0

    def defensiveRating(self):
        return 0

    def __str__(self):
        return (
            f"3P: {self._3p} | "
            f"2P: {self._2p} | "
            f"FT: {self.ft} | "
            f"AST: {self.ast} | "
            f"REB: {self.reb} | "
            f"TOV: {self.tov} | "
            f"BLK: {self.blk} | "
            f"STL: {self.stl} | "
            f"FL: {self.fl}"
        )