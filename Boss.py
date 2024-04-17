#
# Gavin McKenzie
# 4/16/24
# Boss Subclass
import random
from time import sleep
import Creature

class Boss(Creature.Creature):

    def __init__(self, name, atk, deff, hp, status, love):
        super().__init__(name, atk, deff, hp, status)
        self.love = love

    def __str__(self):
        print("You stare at the boss...")
        sleep(3)
        return "It doesn't seem very friendly"

    def stats(self):
        print(f"{self.name}\n{'-' * len(self.name)}\n\tAtk - UNMEASURABLE\n\tdef - WAY TOO MUCH\n\tHP - HES LITERALLY IMMORTAL\n\tStatus - ROYALLY PISSED OFF\n\n\tLove - NOT Lookin great gonna be honest,\n\t\t"
              f"  it might just hurt less to give up now.\n\t\t  Im sorry fella and/or fillet")

    def attack(self):
        pass

    def spec_atk(self):
        pass

    def block(self):
        pass

benis = Boss("GREAT EXPLOSION MURDER GOD PYTHON",0,0,0,0,0)
benis.stats()