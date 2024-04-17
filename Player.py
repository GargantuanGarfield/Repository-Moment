#
# Gavin McKenzie
# 4/16/24
# Player Subclass
import random
from Questions import TFQ, MCQ, FITB, JEOPARDY
import Creature
from time import sleep

class Player(Creature.Creature):

    def __init__(self, name='', atk=0, deff=0, hp=0, status='chilling', weapon='', armor=''):
        super().__init__(name, atk, deff, hp, status)
        self.weapon = weapon
        self.armor = armor

    def __str__(self):
        return f"You WHIP out your left hand with the body mirror implant and gaze at yourself... weird fella.. and/or fillet"

    # prints player info
    def stats(self):
        words = super().stats(self)
        return (words + f"Equipped Weapon - {self.weapon}\n\tEquipped armor - {self.armor}")

    #
    def attack(self, diff):
        diff_names = {'TFQ': TFQ, 'MCQ': MCQ, 'JEOPARDY': JEOPARDY, 'FITB': FITB}
        for name in diff_names.items():
            if diff == name[0]:
                diff = name[1]
            else:
                pass

        # If the difficulty is valid, executes the attack method
        if diff == TFQ:

            # Assigning question and answer vars
            q_num = random.randint(1, 5)
            for item in diff[q_num].items():
                question = item[0]
                answer = item[1]


            # HUGE if-else statement for difficulties and question printing and input checking

            # Easy difficulty question setup, prompt and checking
            # True/False Questions
            if diff == TFQ:

                # Input
                print("\t\t-- True or false? -- \n")
                print(f"(T/F) {question}")
                user_ans = input('\t').lower()

                # Correct/Incorrect answer hit calculations
                if user_ans == 't' or user_ans == answer[0:len(user_ans)]:
                    print("Correct!")
                    sleep(.3)
                    success = hit_rolling(True)
                    return success

                else:
                    print("Incorrect..")
                    success = hit_rolling(False)
                    return success

            # Medium difficulty question setup, prompt and checking
            # MC questions
            elif diff == MCQ:

                print("\tMultiple choice:\n")
                print(question)

                # Correct/Incorrect answer hit calculations
                if user_ans == answer:
                    print("Correct!")
                    success = hit_rolling(True)
                    return success

                else:
                    print("Incorrect..")
                    success = hit_rolling(False)
                    return success


            # HARD difficulty question setup, prompt and checking
            # Fill in the black Questions
            elif diff == FITB:

                # Correct/Incorrect answer hit calculations
                if user_ans == answer:
                    print("Correct!")
                    success = hit_rolling(True)
                    return success

                else:
                    print("Incorrect..")
                    success = hit_rolling(False)
                    return success


            # NIGHTMARE difficulty question setup, prompt and checking
            # Jeopardy Questions
            else:
                # TODO: KILL YOURSELF

                # Correct/Incorrect answer hit calculations
                if user_ans == answer:
                    print("Correct!")
                    success = hit_rolling(True)
                    return success

                else:
                    print("Incorrect..")
                    success = hit_rolling(False)
                    return success


            # Return statements and finally hit/miss calculations


        # If Difficulty is invalid
        else:
            print("Difficulty Invalid")

#Function that decides hit chance
def hit_rolling(status):
    rannum = random.randrange(0, 21)
    if status:
        if rannum == 20:
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
    else:
        if rannum >= 18:
            print("The attack connects")
            sleep(2)
            return 2
        elif rannum >= 8:
            print("The attack grazes the enemy")
            sleep(2)
            return 2
        else:
            print("The attack misses")
            sleep(2)
            return 0
