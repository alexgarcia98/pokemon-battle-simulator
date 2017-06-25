from move import *
from pokemon import *
from sys import *
from pkdatabase import *

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
    print("\nLet the battle begin!\n")


def team_builder(list1, size):
    print("\nTeam Builder\n" +
        "    1) View Pokemon List\n" +
        "    2) View Pokemon Information\n" +
        "    3) Add to Team\n" +
        "    4) Remove from Team\n" +
        "    5) View Team\n" +
        "    6) Finish\n" +
        "Enter selection: ", end="")
    answer = stdin.readline()
    if(answer == "1\n"):
        return view_list(list1, size)
    elif(answer -- "2\n"):
        return pokemon_info(list1, size)
    elif(answer == "3\n"):
        if(size == 6):
            print("\nYour team is full! Remove a Pokemon first before adding a new one.")
            return team_builder(list1, size)
        else:
            return team_add(list1, size)
    elif(answer == "4\n"):
        return team_remove(list1, size)
    elif(answer == "5\n"):
        return team_view(list1, size)
    elif(answer == "6\n"):
        if(size != 0):
            return list1
        else:
            print("\nYour team can't be empty! Add at least one Pokemon.")
            return team_builder(list1, size)
    else:
        print("\nInvalid option\n")
        return team_builder(list1, size)

def view_list(list1, size):
    str1 = "\n0 - Return to Team Builder\n"
    for i in range(len(pklist)):
        str1 = str1 + str(i + 1) + " - " + pklist[i].__name__ + "\n"
    print(str1[:-1])
    return team_builder(list1, size)

def pokemon_info(list1, size):
    print("\nWhich Pokemon would you like further information about?\n" +
        "Please enter the corresponding number: ", end="")
    answer = stdin.readline()
    while True:
        try:
            x = int(answer[:-1])
            break
        except ValueError:
            print("\nThat was not a valid number.  Try again...")
    if((x >= 0) and (x <= len(pklist))):
        if(x == 0):
            return team_builder(list1, size)
        else:
            # Name of Pokemon
            # 
            pass
    else:
        print("Out of range. Please try again...")
        return pokemon_info(list1, size)

def team_add(list1, size):
    print("\nWho would you like to add?\n" +
        "Please enter the corresponding number: ", end="")
    answer = stdin.readline()
    while True:
        try:
            x = int(answer[:-1])
            break
        except ValueError:
            print("\nThat was not a valid number.  Try again...")
    if((x >= 0) and (x <= len(pklist))):
        if(x == 0):
            return team_builder(list1, size)
        else:
            list1[size] = pklist[x - 1]()
            size1 = size + 1
            print("\n" + str(pklist[x - 1].__name__) + " successfully added.")
            if(size1 == 6):
                return team_builder(list1, size1)
            else:
                return team_add(list1, size1)
    else:
        print("Out of range. Please try again...")
        return team_add(list1, size)

def team_remove(list1, size):
    print("\nWho would you like to remove?\n" +
        "Please enter the corresponding number: ", end="")
    answer = stdin.readline()
    while True:
        try:
            x = int(answer[:-1])
            break
        except ValueError:
            print("\nThat was not a valid number.  Try again...")
    if((x >= 0) and (x <= len(pklist))):
        if(x == 0):
            return team_builder(list1, size)
        else:
            a = pklist[x - 1]()
            for i in range(0, size):
                if(a == list1[i]):
                    list1[i] = list1[size - 1]
                    list1[size - 1] = "No Pokemon"
                    size1 = size - 1
                    print("\n" + str(pklist[x - 1].__name__) + " successfully removed.")
                    return team_remove(list1, size1)
            print("\n" + str(pklist[x - 1].__name__) + " is not currently on your team.")
            return team_remove(list1, size)
    else:
        print("\nOut of range. Please try again...")
        return team_remove(list1, size)

def team_view(list1, size):
    print("\n" + str(list1))
    return team_builder(list1, size)

start_menu(empty_arena())
