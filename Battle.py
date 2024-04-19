import time  # Nicholas: for pauses
import random  # Nicholas: implement chance in moves
import Questions
import Player
Option_battle_list = ['Attack', 'Block']
Quiz_Types = ["MC", "JEOPARDY", "FITB", "TOF"]  # Nicholas: List of the quiz types for the if/else statements
ehp = 50 # Nicholas: REPLACE WITH THE CLASS ENEMY HP
php = 50 # Nicholas: REPLACE WITH THE CLASS PLAYER HP
edmg = 1
pdmg = 1

rannum = random.randint(0,20) # Replace in the actual code with Player.hit_rolling
if rannum == 20:
    print("CRITICAL HIT")
    time.sleep(2)
    num = 3
elif rannum >= 2:
    print("The attack connects")
    time.sleep(2)
    num = 1
else:
    print("The attack misses")
    time.sleep(2)
    num = 2

def battling(enemy, player):
    global ehp, php # Nicholas: REPLACE WITH THE CLASS ENEMY HP AND PLAYER HP
    battle_choice = input(f'Choose what to do {Option_battle_list}: ').title()
    while ehp > 0 and php > 0:  # Nicholas: code runs until player or enemy dies

        while battle_choice not in Option_battle_list:  # runs until battle_choice is valid
            battle_choice = input(f'Choose what to do {Option_battle_list}: ').title()

        if battle_choice == 'Attack':

            good2go = False
            while not good2go:
                for room in Quiz_Types:
                    print('[' + room[0] + ']' + room[1:] + ": ", end="")
                move = input("\n\tInput What you would like to do (M/J/F/T): ").upper()

                for i in range(len(Quiz_Types)):  # Nicholas: Repurposed code form Gavin
                    if len(move) > 1:
                        if move == Quiz_Types[i][0:len(move)].upper():  # Checks if the Input is part of the answer
                            move = Quiz_Types[i]
                            if move == "TOF":
                                print("easy")
                                ehp -= pdmg



                            elif move == "MC":
                                print("med")
                                ehp -= pdmg + 1


                            elif move == "FITB":
                                print("hard")
                                # Player.atk("hard")
                                ehp -= pdmg + 2

                            elif move == "JEOPARDY":
                                print("ntmare")
                                # Player.atk("ntmare")
                                ehp -= pdmg + 3


                            else:
                                print("How Did it not work")

                            good2go = True
                            break

                    elif len(move) == 1:
                        if move == Quiz_Types[i][0]:
                            move = Quiz_Types[i]
                            if move == "TOF":
                                print("easy")
                                # Player.atk("easy")
                                ehp -= pdmg


                            elif move == "MC":
                                print("med")
                                # Player.atk("med")
                                ehp -= pdmg + 1


                            elif move == "FITB":
                                print("hard")
                                # Player.atk("hard")
                                ehp -= pdmg + 2


                            elif move == "JEOPARDY":
                                print("ntmare")
                                # Player.atk("ntmare")
                                ehp -= pdmg + 3



                            else:
                                print("How Did it not work")
                            good2go = True
            while not good2go:
                if ehp <= 0:
                    ehp = 0
                    print(ehp)
                    print(php)
                elif php <= 0:
                    php = 0
                    print(ehp)
                    print(php)
            else:
                php -= edmg
                print(ehp)
                print(php)
                print()
                battle_choice = input(f'Choose what to do {Option_battle_list}: ').title()

        elif battle_choice == 'Block':
            print("UH OH YOU BLOCKED")
            battle_choice = input(f'Choose what to do {Option_battle_list}: ').title()

        elif battle_choice == 'Block':
            pass  # Need To Implement Block










