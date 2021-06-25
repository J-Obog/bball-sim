from argparse import ArgumentParser
#from bball.team import Team
#from bball.game import Game

def main():
    #args
    argp = ArgumentParser(description="Parse CL Args")
    argp.add_argument("-a", "--team-a", required=True, help="Path to json file that contains team a's data")
    argp.add_argument("-b", "--team-b", required=True, help="Path to json file that contains team b's data")
    argp.add_argument("-s", "--save-dir", required=False, help="Path to save game files")
    argp.add_argument("--save-box", required=False, help="Save game box score")
    argp.add_argument("--save-pbp", required=False, help="Save game play-by-play")
    args = argp.parse_args()
    
    #simulation
    """
    team_a = Team.loadFromFile(args.team_a)
    team_b = Team.loadFromFile(args.team_b)
    simulation = Game([team_a, team_b], site=args.site, save_dir=args.save_dir, save_box=args.save_box, save_pbp=args.save_pbp)
    simulation.run()
    """

if __name__ == '__main__':
  main()