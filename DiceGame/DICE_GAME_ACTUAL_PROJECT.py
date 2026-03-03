import random as r
from File_saving import valid_players, main
#print(valid_players)

# Asks for a string
def str_ask(str_input):
    while True:
        try:
            _t = input(str_input).lower().title().strip()
            if not _t.isalpha():
                raise ValueError("Input contains non-alphabetic characters.")
            return _t
        except ValueError:
            print("Enter only letters please (no numbers or symbols).")


#For the dice
class Dice:
    def __init__(self, sides=6) -> None:
        self.sides = sides
            

    def roll_dice(self) -> int:
        return r.randint(1, self.sides)


def add_n_roll(d1, d2) -> dict:
    res1 = d1.roll_dice()
    res2 = d2.roll_dice()
    _total = res2 + res1
    return {"dice": (res1, res2), "total" : res1 + res2, "is_double" : res1 == res2, "even" : _total % 2 == 0 , "odd" : _total % 2 != 0}

#For the Person
class Person:
    def __init__(self, name, score=0):
        self.name = name
        self.score = score
    
    def call(self) -> None:
        print(f"Name:{self.name}\nScore:{self.score}\n")

#Makes sure if it doenst go below zero
def zero_check(score) -> int:
    if score < 0:
        score = 0
    return score

#Manages the points when you roll
def rules(roll):
    if roll["is_double"]:
        score = 10
    elif roll["even"]:
        score = 10
    elif roll["odd"]:
        score = -5
    return score

def double_rules(roll):
    #check if even
    if roll%2 == 0:
        score = 10
    else:
        score = -5
    return score


def authenticate(player1):
    while player1 not in valid_players:
        player1 = str_ask(f"{player1} not found in database. Try again: ")
    
    while player1 in valid_players:
        _password = str_ask(f"{player1} enter your password\n~")
        if _password == valid_players[player1]:
            print("Valid password")
            p1 = Person(player1)
            p1.call()
            break
        else:
            print(f"Invalid password for {player1}")
            continue
            
    
    player2 = str_ask("Player 2, What's your name?\n~ ")
    while player2 not in valid_players or player1 == player2:
        if player1 == player2:
            player2 = str_ask(f"{player2} is already chosen try someone else\n~")
        else:
            player2 = str_ask(f"{player2} not found in database. Try again\n~")
    
    while player2 in valid_players:
        _password = str_ask(f"{player2} enter your password\n~")
        if _password == valid_players[player2]:
            print("Valid password")
            p2 = Person(player2)
            p2.call()
            break
        else:
            print(f"Invalid password for {player2}")
            continue
    
    return p1, p2

def run(person, roll):
    _ = input(f"{person.name} press enter to roll\n-")
    if type(roll) == dict:
        print(f"Rolled {roll['total']}")
        person.call()
    else:
        print(f"Rolled {roll}")
        person.call()


def rounds():
    p1, p2 = authenticate(str_ask("Player 1, What's your name?\n~ "))
    
    for _ in range(5):
        roll = add_n_roll(Dice(), Dice())
        p1.score += rules(roll)
        p1.score = zero_check(p1.score)
        run(p1, roll)
        if roll["is_double"]:
            print("DOUBLE TRIGGERED")
            _double_roll = r.randint(1, 6)
            p1.score += double_rules(_double_roll) + _double_roll
            run(p1, _double_roll)
        else:
            pass
        
        roll = add_n_roll(Dice(), Dice())
        p2.score += rules(roll)
        p2.score = zero_check(p2.score)
        run(p2, roll)
        if roll["is_double"]:
            print("DOUBLE TRIGGERED")
            _double_roll = r.randint(1, 6)
            p2.score += double_rules(_double_roll) + _double_roll
            run(p2, _double_roll)
        else:
            pass
    
    return p1, p2

def winner(p1, p2):
    if p1.score == p2.score:
        while p1.score == p2.score:
            p1.score = r.randint(1,6)
            p2.score = r.randint(1,6)
            if p1.score == p2.score:
                continue
            else:
                if p1.score > p2.score:
                    winner = p1
                elif p1.score < p2.score:
                    winner = p2
                    
    elif p1.score > p2.score:
        winner = p1
    elif p1.score < p2.score:
        winner = p2
    
    return winner
    


p1_final ,p2_final = rounds()
Master = winner(p1_final, p2_final)
print(f"{Master.score}:{Master.name}")
main(Master)