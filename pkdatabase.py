from pokemon import *
from movedatabase import *
from abilitydatabase import *

# Scratch that, let's do Gen 1 first.

# Pokemon Available (Gen 1):
# Venusaur, Charizard, Blastoise, Beedrill, Pidgeot, Pikachu, Raichu
# Sandslash, Nidoqueen, Nidoking, Clefable, Ninetales, Vileplume, Dugtrio
# Arcanine, Poliwrath, Alakazam, Machamp, Tentacruel, Golem, Slowbro
# Magneton, Muk, Cloyster, Gengar, Marowak, Chansey, Starmie
# Scyther, Jynx, Electabuzz, Pinsir, Gyarados, Lapras, Vaporeon
# Jolteon, Flareon, Omastar, Kabutops, Aerodactyl, Snorlax, Articuno,
# Zapdos, Moltres, Dragonite, Mewtwo, Mew

# Venusaur: Offensive Tank

# a Pokemon is Pokemon(str, ability, list, list, Status, str)
# where name is represented with a str,
# ability is an ability,
# stats are represented with a list,
# moves are represented with a list,
# status is represented with a Status,
# and an item is represented with a str

# Stats are stored in a list in the following order:
# [Level, HP, Attack, Defense, Special Attack, Special Defense, Speed, Bonuses]

# Bonuses are stored in a list in the following order:
# [Attack, Defense, Special Attack, Special Defense, Speed, Accuracy, Evasion]

# Moves are stored in a list in the following order:
# [Move, Current PP]

# a Status is one of
# 0 : no status,
# 1 : poisoned,
# 2 : badly poisoned,
# 3 : burned,
# 4 : paralyzed,
# 5 : asleep,
# 6 : frozen

# type list
# 0 - Normal
# 1 - Fighting
# 2 - Flying
# 3 - Poison
# 4 - Ground
# 5 - Rock
# 6 - Bug
# 7 - Ghost
# 8 - Steel
# 9 - Fire
# 10 - Water
# 11 - Grass
# 12 - Electric
# 13 - Psychic
# 14 - Ice
# 15 - Dragon
# 16 - Dark
# 17 - Fairy

bonuses = [1, 1, 1, 1, 1, 1, 1]

def Venusaur():
    venusaur_stats = [100, HP(359, 359), 153, 202, 284, 256, 222, bonuses, 11, 3]
    venusaur_moves = [[giga_drain, 16], [sludge_bomb, 16], [synthesis, 8], [hp_fire, 24]]
    venusaur = Pokemon("Venusaur", "Offensive Tank", chlorophyll, venusaur_stats, venusaur_moves, 0, "Venusaurite")
    return venusaur

def Charizard():
    charizard_stats = [100, HP(297, 297), 267, 193, 228, 206, 328, bonuses, 9, 2]
    charizard_moves = [[dragon_dance, 32], [dragon_claw, 24], [flare_blitz, 24], [roost, 16]]
    charizard = Pokemon("Charizard", "Dragon Dance X", blaze, charizard_stats, charizard_moves, 0, "Charizardite X")
    return charizard

pklist = [Venusaur, Charizard]
