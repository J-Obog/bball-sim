
class Stats:
    def __init__(self):
        self.mins = 0
        self.fg = 0 
        self.fga = 0 
        self._3p = 0 
        self._3pa = 0 
        self.ft = 0 
        self.fta = 0 
        self.reb = 0 
        self.ast = 0 
        self.stl = 0
        self.blk = 0 
        self.tov = 0
        self.fl = 0 
        self.pts = 0 
    
    def fieldGoalPct(self):
        return self.fg/float(self.fga)
    
    def threePointPct(self):
        return self._3p/float(self._3pa)

    def freeThrowPct(self):
        return self.ft/float(self.fta)

    def __str__(self):
        return (
            f"MP: {self.mins} | "
            f"FG: {self.fg} | "
            f"FGA: {self.fga} | " 
            f"3P: {self._3p} | " 
            f"3PA: {self._3pa} | " 
            f"FT: {self.ft} | " 
            f"FTA: {self.fta} | " 
            f"REB: {self.reb} | " 
            f"AST: {self.ast} | " 
            f"STL: {self.stl} | "
            f"BLK: {self.blk} | " 
            f"TOV: {self.tov} | "
            f"PF: {self.fl} | " 
            f"PTS: {self.pts}"
        )