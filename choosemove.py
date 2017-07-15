from move import *
from pokemon import *
from sys import *
from pkdatabase import *

# arena ->
def choose_move(arena1, p):
    print("\n" + str(p.name) + ", choose your move.\n" +
        "    1) Fight\n" +
        "    2) Switch\n" +
        "    3) View Field\n" +
        "    4) Forfeit\n" +
        "Enter Selection: ", end="")
    answer = stdin.readline()
    if(answer == "1\n"):
        return fight(arena1, p)
    elif(answer == "2\n"):
        return switch(arena1, p)
    elif(answer == "3\n"):
        return view_field(arena1, p)
    elif(answer == "4\n"):
        return forfeit(arena1, p)
    else:
        print("\nInvalid option")
        return choose_move(arena1, p)

def fight(arena1, p):
    print("\nChoose your attack." + my_moves(p.current) +
        "\nEnter the corresponding number: ", end="")
    answer = stdin.readline()
    while True:
        try:
            x = int(answer[:-1])
            break
        except ValueError:
            print("\nThat was not a valid number.  Try again...")
    if((x >= 0) and (x <= 4)):
        if(x == 0):
            return choose_move(arena1, p)
        else:
            if(p.current.moves[x - 1][1] == 0):
                print("\nThere is no more PP left for that move! Choose another one.")
                return fight(arena1, p)
            p.current.moves[x - 1][1] -= 1
            return p.current.moves[x - 1][0]
    else:
        print("Out of range. Please try again...")
        return fight(arena1, p)

def switch(arena1, p):
    print("\nWho would you like to switch in?" + print_alive(p) +
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
            return choose_move(arena1, p)
        elif(p.team[x - 1] == "No Pokemon"):
            print("\nThere is no pokemon there. Please try again...")
            return switch(arena1, p)
        elif(is_fainted(p.team[x - 1]) == True):
            print("\n" + str(p.team[x - 1]) + " is fainted! Choose someone else.")
            return switch(arena1, p)
        elif(p.team[x - 1] == p.current):
            print("\n" + str(p.team[x - 1]) + " is already out! Choose someone else.")
            return switch(arena1, p)
        else:
            return p.team[x - 1]
    else:
        print("\nOut of range. Please try again...")
        return switch(arena1, p)

def view_field(arena1, p):
    print("")
    if(p == arena1.player2):
        print(str(arena1.player1.name) + "'s side:\n" +
            "    " + str(arena1.player1.current) + " (Level " +
            str(arena1.player1.current.stats[0]) + ")" + "\n    HP: " +
            str(arena1.player1.current.stats[1].current) + "/" +
            str(arena1.player1.current.stats[1].base))
    else:
        print(str(arena1.player2.name) + "'s side:\n" +
            "    " + str(arena1.player2.current) + " (Level " +
            str(arena1.player2.current.stats[0]) + ")" + "\n    HP: " +
            str(arena1.player2.current.stats[1].current) + "/" +
            str(arena1.player2.current.stats[1].base))
    print("\nYour side:\n" +
        "    " + str(p.current) + " (Level " +
        str(p.current.stats[0]) + ")" + "\n    HP: " +
        str(p.current.stats[1].current) + "/" +
        str(p.current.stats[1].base))
    return choose_move(arena1, p)

def print_alive(p):
    s = "\n    0: Go Back"
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

def forfeit(arena1, p):
    print("\nAre you sure you want to forfeit?\n" +
        'Type "Yes, I am a pussy." if you would like to forfeit. ', end="")
    answer = stdin.readline()
    if(answer == "Yes, I am a pussy.\n"):
        return "loser"
    else:
        print("\nThen get out there and fight you pussy.")
        return choose_move(arena1, p)
