#
# Gavin McKenzie
# 4/16/24
# Player Subclass
import random
import Questions

class Player(Creature):

    def __init__(self, name, atk, deff, hp, weapon, armor):
        super().__init__(name, atk, deff, hp)
        self.weapon = weapon
        self.armor = armor

    def __str__(self):
        return f"You WHIP out your left hand with the body mirror implant and gaze at yourself... weird fella.. and/or fillet"

    #prints player info
    def stats(self):
        words = super().stats(self)
        return (words + f"Equipped Weapon - {self.weapon}\n\tEquipped armor - {self.armor}")

    #
    def atk(self, diff):
        #Assigning question and answer vars
        q_num = random.randint(1,5)
        question = Questions.diff[q_num].value()
        answer = Questions.diff[q_num].key()

        #HUGE if-else statement for difficulties and question printing and input checking
        if diff == 'easy':
            pass

        elif diff == 'med':
            pass

        elif diff ==  'hard':
            pass

        else:
            pass


        #Return statements and finally hit/miss calculations