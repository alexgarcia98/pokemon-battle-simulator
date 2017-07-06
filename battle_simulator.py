from move import *
from pokemon import *
from sys import *
from pkdatabase import *
from teambuilder import *

# Pokemon Available:
# Dragonite, Tyranitar, Metagross, Garchomp, Volcarona, Greninja, Tapu Koko
# Pinsir, Heracross, Mawile, Heatran, Landorus-T, Zygarde, Magearna
# Mew, Scizor, Latios, Tangrowth, Ferrothorn, Aegislash, Celesteela

# Scratch that, let's do Gen 1 first.

# Pokemon Available (Gen 1):
# Venusaur, Charizard, Blastoise, Beedrill, Pidgeot, Pikachu, Raichu
# Sandslash, Nidoqueen, Nidoking, Clefable, Ninetales, Vileplume, Dugtrio
# Arcanine, Poliwrath, Alakazam, Machamp, Tentacruel, Golem, Slowbro
# Magneton, Muk, Cloyster, Gengar, Marowak, Chansey, Starmie
# Scyther, Jynx, Electabuzz, Pinsir, Gyarados, Lapras, Vaporeon
# Jolteon, Flareon, Omastar, Kabutops, Aerodactyl, Snorlax, Articuno,
# Zapdos, Moltres, Dragonite, Mewtwo, Mew


# an Arena is Arena()
class Arena:
    def __init__(self, player1, player2, weather, terrain, hazards):
        self.player1 = player1
        self.player2 = player2
        self.weather = weather

class Weather:
    def __init__(self, name, turns):
        self.name = name
        self.turns = turns

def empty_arena():
    return Arena(None, None, None, None, None)

def start_menu(arena1):
    print("Pokemon Battle Simulator\n" + "Player 1, what is your name? ", end="")
    p1 = stdin.readline()
    p1_1 = p1[:-1]
    print("\nWelcome, " + p1_1 + ". Please build your team.")
    empty = "No Pokemon"
    list1 = team_builder([empty, empty, empty, empty, empty, empty], 0)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n" +
        "Player 2, what is your name? ", end="")
    p2 = stdin.readline()
    p2_1 = p2[:-1]
    print("\nWelcome, " + p2_1 + ". Please build your team.")
    list2 = team_builder([empty, empty, empty, empty, empty, empty], 0)
    plyr1 = Player(p1_1, list1)
    plyr2 = Player(p2_1, list2)
    arena2 = Arena(plyr1, plyr2, "None", "None", "None")
    print("\nLet the battle begin!\n")
    return battle(arena2)

def battle(arena1):
    pass

def turn(arena1):
    pass
    # Player 1 chooses action

start_menu(empty_arena())
