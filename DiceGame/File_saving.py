import json
import os

#PASSWORDS IN A KEY VALUE PAIR (HASHMAP), FOR MORE INFO SEARCH PYTHON DICTIONARIES IF YOU'RE CLUELESS
valid_players = {"Subhan": "Umer", "Izaac": "Hanafin", "Seb": "Forster-Hulst", "Joseph": "Heaney", "Ben":"Oakley", "Wazza":"Wazza", "Sir":"Cool"}
leaderboard = {}

#DON'T WRITE OR CHANGE THE FILE MANUALLY IT IS NOT A .txt FILE, IT'S A .json FILE, IT WORKS DIFFERNETLY
def main(winner):
    filename = "leaderboard.json"
    
    if os.path.exists(filename) and os.path.getsize(filename) > 0:
        with open(filename, "r") as file:
            leaderboard = json.load(file)
    else:
        leaderboard = {}
        
    if winner.name not in leaderboard or winner.score > leaderboard[winner.name]:
        leaderboard[winner.name] = winner.score
        
    sorted_items = sorted(leaderboard.items(), key=lambda x: x[1], reverse=True)[:10]
    leaderboard = dict(sorted_items)

    with open(filename, "w") as file:
        json.dump(leaderboard, file, indent=4)
    
    print("-~Leaderboard~-")
    for rank, (name,score) in enumerate(leaderboard.items(), 1):

        print(f"{rank}. {name}:{score}")
