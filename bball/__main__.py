from argparse import ArgumentParser
from bball.team import Team
from bball.game import Game

def main():
    """Command Line options for running simulation"""
    argp = ArgumentParser(description="Parse CL Args")
    argp.add_argument("-a", "--team-a", type=str, required=True, help="Path to json file that contains team a's data")
    argp.add_argument("-b", "--team-b", type=str, required=True, help="Path to json file that contains team b's data")
    argp.add_argument("-s", "--save-game", default=False, action="store_true", help="Save game box score and play by play")
    argp.add_argument("-d", "--save-dir", type=str, help="Path to save game files")
    argp.add_argument('-l', "--location", type=int, choices=[-1,0,1], default=0, help='Location where game should be played')
    args = argp.parse_args()

    """Configuring sim classes"""
    team_a = Team.load_from_file(args.team_a)
    team_b = Team.load_from_file(args.team_b)
    simulation = Game([team_a, team_b], args.location)
    simulation.run()

    if args.save_game:
      simulation.save(args.save_dir)


if __name__ == '__main__':
  main()