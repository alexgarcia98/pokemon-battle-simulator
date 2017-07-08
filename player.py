from sys import *
from random import randint
from pokemon import *

# a Player is Player(str, list)
# where the player's name is represented with a str,
# and a team of pokemon is represented with a list
class Player:
    def __init__(self, name, team, current):
        self.name = name
        self.team = team
        self.current = current

def make_player(name, team):
    return Player(name, team, None)

def get_faster(p1, p2):
    if((p1.current.stats[6] * p1.current.stats[7][4]) ==
        (p2.current.stats[6] * p2.current.stats[7][4])):
        r = randint(0, 1)
        if(r == 1):
            return p1
        else:
            return p2
    elif((p1.current.stats[6] * p1.current.stats[7][4]) >
        (p2.current.stats[6] * p2.current.stats[7][4])):
        return p1
    else:
        return p2

def is_loser(p1):
    l = 0
    for i in range(0, 6):
        if(is_fainted(p1.team[i]) == False):
            l += 1
    if(l == 0):
        return True
    else:
        return False
