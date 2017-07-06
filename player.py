from sys import *

# a Player is Player(str, list)
# where the player's name is represented with a str,
# and a team of pokemon is represented with a list
class Player:
    def __init__(self, name, team):
        self.name = name
        self.team = team

def make_player(name, team):
    return Player(name, team)
