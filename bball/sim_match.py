from argparse import ArgumentParser

def main():
    argp = ArgumentParser(description="Parse CL Args")
    argp.add_argument("--t1", required=True, help="Path to team one's json file")
    argp.add_argument("--t2", required=True, help="Path to team two's json file")
    argp.add_argument("--save-box", required=False, help="Save game box score")
    argp.add_argument("--save-play", required=False, help="Save game play-by-play")
    argp.add_argument("-s", "--save-dir", required=False, help="Path to save game files")
    args = argp.parse_args()
    print(args)
    #argp.add_argument("-l", "--load-dir", required=False, help="Path to load game files")
    #print("Hello World")

if __name__ == '__main__':
  main()