from move import *
from pokemon import *
from sys import *
from pkdatabase import *
from teambuilder import *
from choosemove import *
from player import *
from damagecalc import *

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
# Zapdos, Moltres, Dragonite, Mew


# an Arena is Arena()
class Arena:
    def __init__(self, player1, player2, environment):
        self.player1 = player1
        self.player2 = player2
        self.environment = environment

    def __eq__(self, other):
        return ((type(other) == Arena)
          and self.player1 == other.player1
          and self.player2 == other.player2
          and self.environment == other.environment
        )

    def __repr__(self):
        return ("Arena({!r}, {!r}, {!r})".format(self.player1, self.player2, self.environment))

class Environment:
    def __init__(self, name, turns):
        self.name = name
        self.turns = turns

def empty_arena():
    return Arena(None, None, [])

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
    plyr1 = Player(p1_1, list1, None)
    plyr2 = Player(p2_1, list2, None)
    arena2 = Arena(plyr1, plyr2, None)
    print("\nLet the battle begin!\n")
    return battle(arena2)

def battle(arena1):
    print(arena1.player1.name + " sent out " + repr(arena1.player1.team[0]) + "!\n" +
        arena1.player2.name + " sent out " + repr(arena1.player2.team[0]) + "!")
    arena1.player1.current = arena1.player1.team[0]
    arena1.player2.current = arena1.player2.team[0]
    action1 = choose_move(arena1, arena1.player1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    action2 = choose_move(arena1, arena1.player2)
    turn(arena1, action1, action2)

    # turn()

def start_turn(arena1):
    action1 = choose_move(arena1, arena1.player1)
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    action2 = choose_move(arena1, arena1.player2)
    turn(arena1, action1, action2)

def turn(arena1, action1, action2):
    if((action1 == "loser") and (action2 == "loser")):
        print("\nYou fucking pussies, I can't believe you both forfeited. " +
            "\nGo sit in a corner and wallow in your shame.")
        return None
    elif((action1 == "loser") and (action2 != "loser")):
        print("\n" + str(arena1.player1.name) + " is too pussy to fight, so " +
            str(arena1.player2.name) + " wins the game!")
        return None
    elif((action1 != "loser") and (action2 == "loser")):
        print("\n" + str(arena1.player2.name) + " is too pussy to fight, so " +
            str(arena1.player1.name) + " wins the game!")
        return None
    else:
        arena1 = execute_action(arena1, action1, action2)
        return start_turn(arena1)
    # Player 1 chooses action

def execute_action(arena1, action1, action2):
    if(type(action1) == Pokemon):
        print("\n" + str(arena1.player1.name) + " recalled " + str(arena1.player1.current) +
            " and sent out " + str(action1) + "!")
        arena1.player1.current = action1
    if(type(action2) == Pokemon):
        print("\n" + str(arena1.player2.name) + " recalled " + str(arena1.player2.current) +
            " and sent out " + str(action2) + "!")
        arena1.player2.current = action2
    c1 = arena1.player1.current
    c2 = arena1.player2.current
    faster = get_faster(arena1.player1, arena1.player2)
    print("Action1: " + str(action1))
    print("Action1 Type: " + str(type(action1)))
    print("Action2: " + str(action2))
    print("Action2 Type: " + str(type(action2)))
    if((arena1.player1 == faster) and (type(action1) == Move)):
        arena2 = attack_mon(arena1, action1, action2, arena1.player1, arena1.player2)
    elif((arena1.player2 == faster) and (type(action2) == Move)):
        arena2 = attack_mon(arena1, action2, action1, arena1.player2, arena1.player1)
    else:
        arena2 = arena1
    return arena2

def attack_mon(arena1, action1, action2, p1, p2):
    arena2 = domage(arena1, action1, action2, p1, p2)
    if(type(action2) == Move):
        arena3 = domage(arena2, action2, action1, p2, p1)
    return arena3

def domage(arena1, action1, action2, p1, p2):
    c1 = p1.current
    c2 = p2.current
    damage = damage_calc(c1, c2, action1)
    hprem = c2.stats[1].current - damage
    if(hprem < 0):
        hprem = 0
    c2.stats[1].current = hprem
    print(display_txt(arena1, action1, action2, p1, p2))
    if(hprem == 0):
        print("\n" + str(c2) + " fainted!")
        if(is_loser(p2) == True):
            print("\n" + str(p2.name) + " lost all of their pokemon, so " +
                str(p1.name) + " wins the game!")
            return None
        else:
            p2.current = replace_pkmn(arena1, p2, p1)
            if(arena1.player1.name == p1.name):
                arena1.player1 = p1
                arena1.player2 = p2
            else:
                arena1.player1 = p2
                arena1.player2 = p1
    return arena1

def display_txt(arena1, action1, action2, p1, p2):
    c1 = p1.current
    c2 = p2.current
    hprem = c2.stats[1].current
    s = ""
    if((effc[action1.mtype][c2.stats[8]] * effc[action1.mtype][c2.stats[9]]) > 1):
        s = ("\n" + str(c1) + " used " + str(action1.name) + "!" +
            "\nIt's super effective! " + str(c2) + " is left with " +
            str(hprem) + " HP.")
    elif((effc[action1.mtype][c2.stats[8]] *
        effc[action1.mtype][c2.stats[9]]) == 0):
        s = ("\n" + str(c1) + " used " + str(action1.name) + "!" +
            "\nIt doesnt affect " + str(c2) + "... ")
    elif((effc[action1.mtype][c2.stats[8]] *
        effc[action1.mtype][c2.stats[9]]) > 1):
        s = ("\n" + str(c1) + " used " + str(action1.name) + "!" +
            "\nIt's not very effective... " + str(c2) + " is left with " +
            str(hprem) + " HP.")
    else:
        s = ("\n" + str(c1) + " used " + str(action1.name) + "!" +
            "\n" + str(c2) + " is left with " + str(hprem) + " HP.")
    return s

def replace_pkmn(arena1, p1, p2):
    print("\nSelect your next pokemon." + print_living(p1) +
        "\nEnter the corresponding number: ", end="")
    answer = stdin.readline()
    while True:
        try:
            x = int(answer[:-1])
            break
        except ValueError:
            print("\nThat was not a valid number.  Try again...")
    if((x >= 0) and (x <= 6)):
        if(x == 0):
            print("\n" + str(p1.name) + " is too pussy to fight, so " +
                str(p2.name) + " wins the game!")
            return None
        elif(p1.team[x - 1] == "No Pokemon"):
            print("\nThere is no pokemon there. Please try again...")
            return replace_pkmn(arena1, p1, p2)
        elif(p1.team[x - 1] == p1.current):
            print("\n" + str(p1.team[x - 1]) + " is already out! Choose someone else.")
            return replace_pkmn(arena1, p1, p2)
        elif(is_fainted(p1.team[x - 1]) == True):
            print("\n" + str(p1.team[x - 1]) + " is fainted! Choose someone else.")
            return replace_pkmn(arena1, p1, p2)
        else:
            return p1.team[x - 1]
    else:
        print("\nOut of range. Please try again...")
        return replace_pkmn(arena1, p1, p2)

def print_living(p):
    s = "\n    0: Forfeit"
    i = 1
    for j in range(0, 6):
        if(p.team[j] == "No Pokemon"):
            pass
        elif(is_fainted(p.team[j]) == False):
            s = s + "\n    " + str(i) + ": " + (str(p.team[j].name))
        elif(is_fainted(p.team[j]) == True):
            s = s + "\n    " + str(i) + ": " + (str(p.team[j].name) + " (Fainted)")
        i += 1
    return s

start_menu(empty_arena())
