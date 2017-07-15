from move import *

# a Move is Move(str, Category, int, float, int)
# where name is represented with a str,
# category is represented with a Category,
# power is represented with an int,
# accuracy is represented with a float,
# and pp is represented with an int

# a Category is one of
# - "physical",
# - "special", or
# - "status"

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

giga_drain = Move("Giga Drain", "special", 11, 75, 1, 16, 0)
sludge_bomb = Move("Sludge Bomb", "special", 3, 90, 1, 16, 0)
synthesis = Move("Synthesis", "status", 11, 0, 1, 8, 0)
hp_fire = Move("Hidden Power", "special", 9, 60, 1, 24, 0)

dragon_dance = Move("Dragon Dance", "status", 15, 0, 1, 32, 0)
dragon_claw = Move("Dragon Claw", "physical", 15, 80, 1, 24, 0)
flare_blitz = Move("Flare Blitz", "physical", 9, 120, 1, 24, 0)
roost = Move("Roost", "status", 2, 0, 1, 16, 0)

scald = Move("Scald", "special", 10, 80, 1, 24, 0)
dark_pulse = Move("Dark Pulse", "special", 16, 80, 1, 24, 0)
aura_sphere = Move("Aura Sphere", "special", 1, 80, 1, 32, 0)
ice_beam = Move("Ice Beam", "special", 14, 90, 1, 16, 0)

'''

Blastoise @ Blastoisinite
Ability: Rain Dish
EVs: 56 HP / 252 SpA / 200 Spe
Modest Nature
- Scald
- Dark Pulse
- Aura Sphere
- Ice Beam

'''
