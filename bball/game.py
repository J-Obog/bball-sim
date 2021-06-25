from time import sleep 

class Game:
    def __init__(self, teams, site, save_dir, save_box, save_pbp):
        self.site = site
        self.teams = teams
        self.save_dir = save_dir
        self.save_box = save_box
        self.save_pbp = save_pbp
        self.period = 1
        self.clock = 12*60
        
    def run(self):
        pass