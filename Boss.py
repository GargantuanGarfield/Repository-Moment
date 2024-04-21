#
# Gavin McKenzie
# 4/16/24
# Boss Subclass
import random
from time import sleep
import Creature

class Boss(Creature.Creature):

    def __init__(self, name, atk, deff, hp, status='', love=''):
        super().__init__(self, name, atk, deff, hp, status)
        self.love = love

    def stats(self):
        print(f"The PYTHON - Syed\n{'-' * 17}\n\tAtk - UNMEASURABLE\n\tdef - WAY TOO MUCH\n\tHP - HES LITERALLY IMMORTAL\n\tStatus - ROYALLY PISSED OFF\n\n\tLove - NOT Lookin great gonna be honest,\n\t\t"
              f"  it might just hurt less to give up now.\n\t\t  Im sorry fella and/or fillet")

    def attack(self):
        print(f"{self.name} pulls back for a great swing..")
        sleep(1.2)

        # Hit success calculation
        rannum = random.randrange(0, 21)
        if rannum >= 18:
            print("CRITICAL HIT")
            sleep(2)
            return 3
        elif rannum >= 2:
            print("The attack connects")
            sleep(2)
            return 1
        else:
            print("The attack misses")
            sleep(2)
            return 0

    def spec_atk(self):
        print(f"{self.name} begins to charge up for a SPECIAL ATTACK!")
        sleep(1.2)
        print("You see sparkling tendrils of light and electricity pulsating \nthroughout the various cables around you")
        sleep(1.2)

        # Hit success calculation
        rannum = random.randrange(0, 21)
        if rannum == 20:
            print("CRITICAL HIT")
            sleep(2)
            print("Every bone in your body screams out in pain, you hear a few of them snap under the pressure")
            return 3
        elif rannum >= 9:
            print("You are blown back by the sheer force of the biden blast")
            sleep(2)
            print("owie")
            sleep(.9)
            return 1
        else:
            print("The attack misses")
            sleep(2)
            print("Several portalinian onlookers are deconstructed by the force of the attack")
            sleep(.9)
            return 0

    def block(self):
        print(f"{self.name} braces itself for an attack")
        sleep(1.2)
        rannum = random.randrange(0, 21)
        if rannum <= 17:
            print("It blocks")
            return True
        else:
            print("The block fails...")
            return False


