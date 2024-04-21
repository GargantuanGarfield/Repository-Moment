#
# Gavin McKenzie
# 4/16/24
# Player Subclass
import random
from Questions import TFQ, MCQ, FITB, JEOPARDY, choices
import Creature
from time import sleep
import os


class Player(Creature.Creature):

    def __init__(self, name='', atk=0, deff=0, hp=0,  weapon={'name': '', 'atk': 0, 'effect': 'DAMAGE'}, armor={'name': '', 'armor': 0, 'effect': 'ARMOR'}, score=0):
        super().__init__(self, name, atk, deff, hp)
        self.weapon = weapon
        self.armor = armor
        self.score = score


    # Will V: This function will display instruct.txt, which tells the user how to play
    def HELP(self):
        instruct = open("Instruct.txt", "r")
        os.system('cls')
        for line in instruct:
            print(line.strip())
            sleep(.025)


    # prints player info
    def stats(self):
        super().stats(self)
        print(f"Equipped Weapon - {self.weapon}\n\tEquipped armor - {self.armor}")

    #ATTACK METHOD
    def attack(self, diff):
        diff_names = {'TFQ': TFQ, 'MCQ': MCQ, 'JEOPARDY': JEOPARDY, 'FITB': FITB}
        for name in diff_names.items():
            if diff == name[0]:
                diff = name[1]
            else:
                pass


        # If the difficulty is valid, executes the attack method
        if type(diff) != 'dict':

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
                print("\t\t-- True or false? -- ATTACK\n")
                print(f"(T/F) {question}")
                user_ans = input('\t - ').lower().strip()

                # Correct/Incorrect answer hit calculations
                if user_ans == answer[0].lower() or user_ans == answer[0:len(user_ans)]:
                    self.score += 10
                    print(f"{user_ans}?.. \n\t== Correct!==")
                    sleep(.3)
                    success = hit_rolling(True)  # checks if the move hits, and return 0 for miss, 1 for hit, and 3 for crit
                    self.score = rolling_check(success, self.score)
                    return success

                else:
                    self.score -= 10
                    print(f"{user_ans}?..\n\tIncorrect..")
                    sleep(1.4)
                    print(f"The correct answer was {answer}..")
                    sleep(.98)
                    print("You feel your body weaken and your focus falters...")
                    sleep(1.5)
                    success = hit_rolling(False) # checks if the move hits, and return 0 for miss, 1 for hit, and 2 for graze
                    self.score = rolling_check(success, self.score)
                    return success

            # Medium difficulty question setup, prompt and checking
            # MC questions
            elif diff == MCQ:
                #Assigning stuff
                question_choices = choices
                question_choices.remove(answer)
                bad_choices = []
                for i in range(4):
                    choice = random.choice(question_choices)
                    while choice in bad_choices:
                        choice = random.choice(question_choices)
                    bad_choices.append(choice)

                #Question Formatting and input


                print("\t\t-- Multiple Choice -- ATTACK\n")
                print(question)
                rannum = random.randint(1, 4)
                for num in range(4):
                    if (num + 1) == rannum:
                        print(f"{num + 1}.) {answer}")
                    else:
                        print(f"{num + 1}.) {bad_choices[num]}")
                        question_choices.remove(bad_choices[num])
                user_ans = input('\t - ').lower().strip()

                # Correct/Incorrect answer hit calculations
                if user_ans == answer[0:len(user_ans)]:
                    self.score += 15
                    print(f"{answer}?.. \n\t== Correct! ==")
                    sleep(1.5)
                    success = hit_rolling(True)  # checks if the move hits, and return 0 for miss, 1 for hit, and 3 for crit
                    self.score = rolling_check(success, self.score)
                    return success

                else:
                    self.score -= 15
                    print(f"{user_ans}?..\n\tIncorrect..")
                    sleep(1.4)
                    print(f"The correct answer was {answer}..")
                    sleep(.98)
                    print("You feel your body weaken and your focus falters...")
                    sleep(1.5)
                    success = hit_rolling(False) # checks if the move hits, and return 0 for miss, 1 for hit, and 2 for graze
                    self.score = rolling_check(success, self.score)
                    return success

            # HARD difficulty question setup, prompt and checking
            # Fill in the black Questions
            elif diff == FITB:

                # Question formatting and stuff
                print("\t\t -- Fill in the blank -- ATTACK")
                print("Word Bank:")
                for q in range(1,6):
                    for answers in FITB[q].values():
                        if q < 5:
                            print(answers, end=", ")
                        else:
                            print(answers + '\n')

                print(question)
                user_ans = input("\t - ").lower().strip()

                # Correct/Incorrect answer hit calculations
                if user_ans == answer[0:len(user_ans)]:
                    self.score += 20
                    print(f"{answer}?.. \n\t== Correct! ==")
                    sleep(1.5)
                    success = hit_rolling(True)  # checks if the move hits, and return 0 for miss, 1 for hit, and 3 for crit
                    self.score = rolling_check(success, self.score)
                    return success

                else:
                    self.score -= 20
                    print(f"{user_ans}?..\n\tIncorrect..")
                    sleep(1.4)
                    print(f"The correct answer was {answer}..")
                    sleep(.98)
                    print("You feel your body weaken and your focus falters...")
                    sleep(1.5)
                    success = hit_rolling(False) # checks if the move hits, and return 0 for miss, 1 for hit, and 2 for graze
                    self.score = rolling_check(success, self.score)
                    return success


            # NIGHTMARE difficulty question setup, prompt and checking
            # Jeopardy Questions
            else:

                #Question formatting : this ones easy... I hope
                print("A dilapidated and rotting Alex Trebeck appears in front of you and you feel locked in place..")
                sleep(1.12)
                print("A podium with your name on it appears in front of you and the zombie Trebeck stares at you as if to say..\n")
                sleep(2)
                print("Python for 300..", end=" ")
                sleep(1.5)
                print(f"\nQuestion: ")
                print(question)
                user_ans = input("\tWhat is? - ").lower().strip()

                # Correct/Incorrect answer hit calculations
                if user_ans == answer[0:len(user_ans)]:
                    self.score += 30
                    print(f"{answer}?.. \n\t== Correct! ==")
                    sleep(1.5)
                    success = hit_rolling(True) # checks if the move hits, and return 0 for miss, 1 for hit, and 3 for crit
                    self.score = rolling_check(success, self.score)
                    return success

                else:
                    self.score -= 30
                    print(f"{user_ans}?..\n\tIncorrect..")
                    sleep(1.4)
                    print(f"The correct answer was {answer}..")
                    sleep(.98)
                    print("You feel your body weaken and your focus falters...")
                    sleep(1.5)
                    success = hit_rolling(False) # checks if the move hits, and return 0 for miss, 1 for hit, and 2 for graze
                    self.score = rolling_check(success, self.score)
                    return success

        # If Difficulty is invalid
        else:
            print("Difficulty Invalid")

    # FINALLY MOVING ON MY LORD
    # Blocking method, alternative to attacking
    def block(self):
        print("You brace yourself to block the attack...")
        sleep(1.2)
        rannum = random.randrange(0, 21)
        if rannum <= 17:
            print("You blocked the attack")
            print("   Damage reduced")
            return True
        else:
            print("The attack breaks through! OW")
            return False




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
            print("The attack grazes the enemy\n\tHalf Damage")
            sleep(2)
            return 2
        else:
            print("The attack misses")
            sleep(2)
            return 0


def rolling_check(output, score):
    if output == 0:
        score -= 10
    elif output == 1:
        score += 10
    elif output == 3:
        score += 20
    return score
