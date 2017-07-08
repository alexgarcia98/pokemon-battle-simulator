# a Move is Move(str, Category, int, int, float, int, int)
# where name is represented with a str,
# category is represented with a Category,
# move type is represented with an int
# power is represented with an int,
# accuracy is represented with a float,
# pp is represented with an int,
# and priority is represented with an int

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

class Move:
    def __init__(self, name, category, mtype, power, accuracy, pp, priority):
        self.name = name
        self.category = category
        self.mtype = mtype
        self.power = power
        self.accuracy = accuracy
        self.pp = pp
        self.priority = priority

    def __eq__(self, other):
        return ((type(other) == Move)
          and self.name == other.name
          and self.category == other.category
          and self.mtype == other.mtype
          and self.power == other.power
          and self.accuracy == other.accuracy
          and self.pp == other.pp
          and self.priority == other.priority
        )

    def __repr__(self):
        return str(self.name)
