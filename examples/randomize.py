from censusname import Censusname
from random import randint
import json

for i in range(2):
    f = open(f"examples/team{i+1}.json", "w+") 
    d = { "name": f"Team{i+1}", "colors": [0,0], "players": [] }
    for j in range(10):
        pn = last_first = Censusname(given="male").generate()
        d["players"].append({
             'name': pn,
             "pos": j % 5,
             "3p": randint(25, 99),
             "2p": randint(25, 99),
             "ft": randint(25, 99),
             "ast": randint(25, 99),
             "reb": randint(25, 99),
             "tov": randint(25, 99),
             "blk": randint(25, 99),
             "stl": randint(25, 99),
             "fl": randint(25, 99)
        })
    json.dump(d, f)
    f.close()