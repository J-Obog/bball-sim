
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
