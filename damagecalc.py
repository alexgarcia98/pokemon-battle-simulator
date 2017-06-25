import unittest
from pkdatabase import *
from stabcalc import *
import math


def damage_calc(pkmn1, pkmn2, move):
    # modifier = Weather * Critical * random * STAB * Type * Burn * other
    if((pkmn1.stats[8] == move.mtype) or (pkmn1.stats[9] == move.mtype)):
        stab = 1.5
    else:
        stab = 1
    if((pkmn1.status == 3) and (move.category == "physical")):
        burn = 0.5
    else:
        burn = 1
    modifier = 1 * 1 * 1 * stab * effc[move.mtype][pkmn2.stats[8]] * effc[move.mtype][pkmn2.stats[9]] * burn * 1
    if(move.category == "physical"):
        damage = int(round((((((2 * pkmn1.stats[0]) / 5) + 2) * move.power *
            (pkmn1.stats[2]/pkmn2.stats[3])) / 50) + 2) * modifier)
    elif(move.category == "special"):
        damage = int(round((((((2 * pkmn1.stats[0]) / 5) + 2) * move.power *
            (pkmn1.stats[4]/pkmn2.stats[5])) / 50) + 2) * modifier)
    else:
        damage = 0
    return damage

class Test_Cases(unittest.TestCase):

    def test1(self):
        self.assertEqual(damage_calc(Venusaur(), Charizard(), sludge_bomb), 159)
        self.assertEqual(damage_calc(Venusaur(), Charizard(), giga_drain), 33)
        self.assertEqual(damage_calc(Venusaur(), Charizard(), hp_fire), 35)
        self.assertEqual(damage_calc(Charizard(), Venusaur(), dragon_claw), 91)
        self.assertEqual(damage_calc(Charizard(), Venusaur(), flare_blitz), 405)
        self.assertEqual(damage_calc(Venusaur(), Charizard(), synthesis), 0)
        self.assertEqual(damage_calc(Charizard(), Venusaur(), dragon_dance), 0)
        self.assertEqual(damage_calc(Charizard(), Venusaur(), roost), 0)

if __name__ == '__main__':
    unittest.main()
