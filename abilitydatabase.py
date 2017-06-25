from ability import *

# Types of abilities:
# 0 - transcendent: ability effects last entire turn (ex: Arena Trap)
# 1 - beginning of turn: activated at the start of turn (ex: Speed Boost)
# 2 - during attack (offense): activated when initiating attack (ex: Aerilate)
# 3 - after attack (offense): activated after initiating attack (ex: Magician)
# 4 - during attack (defense): activated upon taking damage (ex: Lightningrod)
# 5 - after attack (defense): activated after taking damage (ex: Rough Skin)

# an AType is one of the numbers
# 0 through 5
# where each number corresponds to the effects listed above

# an ability is Ability(AType, str)
# where the kind of ability is represented with an AType
# and the name of the ability is represented with a str

chlorophyll = Ability(0, "Chlorophyll")
blaze = Ability(2, "Blaze")
