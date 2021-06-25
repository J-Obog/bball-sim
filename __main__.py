import colorama
from ratings import Ratings
from player import Player
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

p = Player("John Doe", 0, Ratings())
