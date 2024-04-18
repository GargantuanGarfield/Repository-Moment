#
# Gavin McKenzie
# 4/16/24
# Creature Superclass
import random

class Creature:
    def __init__(self, name='', type='', atk=0, deff=0, hp=0, status=''):
        self.name = name
        self.type = type
        self.atk = atk
        self.deff = deff
        self.hp = hp
        self.status = status

    def __str__(self):
        return f'This is a townsperson taken over by a {self.name} parasite, its a {self.type} type parasite'

    def stats(self):
        print(f"{self.name}:\n" + '-' * len(self.name) + f"\n\tatk - {self.atk}\n\tdef - {self.deff}\n\thp - {self.hp}")

    def block(self):
        print("The enemy readies itself..")
        sleep(.9)
        rannum = random.randrange(0,21)
        if rannum <= 18:
            print("It blocks the attack")
            return True
        else:
            print("The attack breaks through!")
            return False

    def attack(self):
        print("The enemy prepares to attack..")
        sleep(.9)
        rannum = random.randrange(0,21)
        if rannum == 20:
            print("CRITICAL HIT")
            return 2
        elif rannum >= 2:
            print("The attack connects")
            return 1
        else:
            print("The attack misses")
            return 0