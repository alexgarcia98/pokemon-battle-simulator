# a Pokemon is Pokemon(str, str, ability, list, list, Status, str)
# where name is represented with a str,
# build is represented with a str,
# ability is an ability,
# stats are represented with a list,
# moves are represented with a list,
# status is represented with a Status,
# and an item is represented with a str

# Stats are stored in a list in the following order:
# [Level, HP, Attack, Defense, Special Attack, Special Defense, Speed, Bonuses, Type1, Type2]

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

class Pokemon:
    def __init__(self, name, build, ability, stats, moves, status, item):
        self.name = name
        self.build = build
        self.ability = ability
        self.stats = stats
        self.moves = moves
        self.status = status
        self.item = item

    def __eq__(self, other):
        return ((type(other) == Pokemon)
          and self.name == other.name
          and self.build == other.build
          and self.ability == other.ability
          and self.stats == other.stats
          and self.moves == other.moves
          and self.status == other.status
          and self.item == other.item
        )

    def __repr__(self):
        return str(self.name)

# an HP is HP(int, int)
# where both the base HP and current HP are represented with ints
class HP:
    def __init__(self, base, current):
        self.base = base
        self.current = current

    def __eq__(self, other):
        return ((type(other) == HP)
          and self.base == other.base
          and self.current == other.current
        )

    def __repr__(self):
        return ("HP({!r}, {!r})".format(self.base, self.current))

# Pokemon -> bool
# checks whether a Pokemon's current HP is <= 0
def is_fainted(pkmn):
    if(pkmn.stats[1].current <= 0):
        return True
    else:
        return False
