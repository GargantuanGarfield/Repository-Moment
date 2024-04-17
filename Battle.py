import time  # Nicholas: for pauses
import random  # Nicholas: implement chance in moves
import Questions
import Player
Option_battle_list = ['Attack', 'Block']
Quiz_Types = ["MC", "JEOPARDY", "FITB", "TOF"]  # Nicholas: List of the quiz types for the if/else statements
ehp = 50
php = 50
edmg = 1
pdmg = 1
def battling(enemy, player):
    global ehp, php
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
                for i in range(len(Quiz_Types)):
                    if len(move) > 1:
                        if move == Quiz_Types[i][0:len(move)].upper():
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
                battle_choice = input(f'Choose what to do {Option_battle_list}: ').title()

        elif battle_choice == 'Block':
            print("UH OH YOU BLOCKED")
            battle_choice = input(f'Choose what to do {Option_battle_list}: ').title()

        elif battle_choice == 'Block':
            pass  # Need To Implement Block

battling("","")








