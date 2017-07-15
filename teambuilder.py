from move import *
from pokemon import *
from sys import *
from pkdatabase import *

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
    elif(answer == "2\n"):
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
        print("\nInvalid option")
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
            pkmn = pklist[x - 1]()
            # Name of Pokemon
            # Set Name
            # Moves
            # Item
            # Ability
            # Stats
            print(
                "\nName: " + pkmn.name + "\n" +   # Name of Pokemon
                "Build: " + pkmn.build + "\n" + # type of set being run
                "Moves: " + pkmn.moves[0][0].name + ", " +
                pkmn.moves[1][0].name + ", " +
                pkmn.moves[2][0].name + ", " +
                pkmn.moves[3][0].name + "\n" +
                "Item: " + pkmn.item + "\n" +
                "Ability: " + pkmn.ability.name + "\n"
                "HP: " + str(pkmn.stats[1].base) + ", " +
                "Atk: " + str(pkmn.stats[2]) + ", " +
                "Def: " + str(pkmn.stats[3]) + ", " +
                "SpAtk: " + str(pkmn.stats[4]) + ", " +
                "SpDef: " + str(pkmn.stats[5]) + ", "
                "Spd: " + str(pkmn.stats[6])
            )
            return team_builder(list1, size)
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
            return team_add(list1, size)
    if((x >= 0) and (x <= len(pklist))):
        if(x == 0):
            return team_builder(list1, size)
        else:
            a = pklist[x - 1]()
            for i in range(0, size):
                if(a == list1[i]):
                    print("\n" + str(pklist[x - 1].__name__) + " is already on your team!")
                    return team_add(list1, size)
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
            return team_remove(list1, size)
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
