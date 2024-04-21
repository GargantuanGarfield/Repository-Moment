import time  # Nicholas: for pauses
import random  # Nicholas: implement chance in moves


Option_battle_list = ['Attack', 'Block', "Info", "Inspect"]
Boss_battle_List = ['Attack', 'Block', "Special Attack", 'Attack', 'Attack', 'Attack', 'Block', 'Block', 'Block', 'Block', 'Special Attack', 'Special Attack']
Quiz_Types = ["MCQ", "JEOPARDY", "FITB", "TFQ"]  # Nicholas: List of the quiz types for the if/else statements

def assignment(p_obj, cr_obj):
    global enemy_hp, player_hp, enemy_atk, player_atk, enemy_deff, player_deff
    enemy_hp = cr_obj.hp
    player_hp = p_obj.hp
    enemy_atk = cr_obj.atk
    player_atk = p_obj.atk
    enemy_deff = cr_obj.deff * .01
    player_deff = p_obj.deff * .01



# PLayer can choose to attack, block, see the enemy stats, or see the help screen
# Enemy always attacks

def battling(Option_battle_list, p_obj, cr_obj):
    assignment(p_obj, cr_obj)
    global enemy_hp, player_hp, enemy_atk, player_atk, enemy_deff, player_deff # all the global

    battle_choice = input(f'Choose what to do {Option_battle_list[:4]}: ').title()
    while enemy_hp > 0 and player_hp > 0:  # Nicholas: code runs until player or enemy dies

        while battle_choice not in Option_battle_list[:4]:  # runs until battle_choice is valid
            battle_choice = input(f'Choose what to do {Option_battle_list[:4]}: ').title()

        if battle_choice == 'Attack':  # Nicholas: Runs attack

            good2go = False  # Nicholas: Runs until either the player or enemy dies.
            while not good2go:
                for room in Quiz_Types:
                    print('[' + room[0] + ']' + room[1:] + ": ", end="")  # Nicholas: Displays word with brackets around the first letter.
                move = input("\n\tInput What you would like to do (M/J/F/T): ").upper()
                print()

                for i in range(len(Quiz_Types)):  # Nicholas: Repurposed code form Gavin
                    if len(move) > 1:
                        if move == Quiz_Types[i][0:len(move)].upper():  # Nicholas: Checks if the Input is part of the answer
                            move = Quiz_Types[i]
                            if move == "TFQ":
                                success_option = p_obj.attack("TFQ")  # Nicholas: Easy difficulty of questions
                                if success_option == 0:

                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk) * enemy_deff

                                elif success_option == 3:
                                    enemy_hp -= 1.5*((player_atk) * enemy_deff)

                                else:
                                    enemy_hp -= ((player_atk) * enemy_deff)/2




                            elif move == "MCQ":
                                success_option = p_obj.attack("MCQ")  # Nicholas: Medium difficulty of questions
                                if success_option == 0:

                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 5) * enemy_deff
                                     # Nicholas: Player attack with damage boost of 5 multiplied by the enemy's defense(%), Normal
                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 5) * enemy_deff)
                                    # Nicholas: Player attack with damage boost of 5 multiplied by the enemy's defense(%), Crit
                                else:
                                    enemy_hp -= ((player_atk + 5) * enemy_deff) / 2
                                 # Nicholas: Player attack with damage boost of 5 multiplied by the enemy's defense(%), Halved

                            elif move == "FITB":
                                success_option = p_obj.attack("FITB")  # Nicholas: Hard difficulty of questions
                                if success_option == 0:

                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 10) * enemy_deff
                                  # Nicholas: Player attack with damage boost of 10 multiplied by the enemy's defense(%), Normal
                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 10) * enemy_deff)  # Nicholas: Player attack with damage boost of 10 multiplied by the enemy's defense(%), Crit by 1.5

                                else:
                                    enemy_hp -= ((player_atk + 10) * enemy_deff) / 2 # Nicholas: Player attack with damage boost of 10 multiplied by the enemy's defense(%), Halved


                            elif move == "JEOPARDY":
                                success_option = p_obj.attack("JEOPARDY") # Nicholas: Hard difficulty of questions
                                if success_option == 0:

                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 15) * enemy_deff # Nicholas: infer from past comments

                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 15) * enemy_deff)  # Nicholas: infer from past comments

                                else:
                                    enemy_hp -= ((player_atk + 15) * enemy_deff) / 2  # Nicholas: infer from past comments



                            else:
                                print("How Did it not work")

                            good2go = True
                            break

                    elif len(move) == 1:
                        if move == Quiz_Types[i][0]:
                            move = Quiz_Types[i]
                            if move == "TFQ":
                                success_option = p_obj.attack("TFQ")
                                if success_option == 0:

                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk) * enemy_deff  # Nicholas: infer from past comments

                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk) * enemy_deff)  # Nicholas: infer from past comments

                                else:
                                    enemy_hp -= ((player_atk) * enemy_deff) / 2  # Nicholas: infer from past comments


                            elif move == "MCQ":
                                success_option = p_obj.attack("MCQ")
                                if success_option == 0:

                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 5) * enemy_deff  # Nicholas: infer from past comments

                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 5) * enemy_deff)  # Nicholas: infer from past comments

                                else:
                                    enemy_hp -= ((player_atk + 5) * enemy_deff) / 2  # Nicholas: infer from past comments



                            elif move == "FITB":
                                success_option = p_obj.attack("FITB")
                                if success_option == 0:

                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 10) * enemy_deff  # Nicholas: infer from past comments

                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 10) * enemy_deff)  # Nicholas: infer from past comments

                                else:
                                    enemy_hp -= ((player_atk + 10) * enemy_deff) / 2  # Nicholas: infer from past comments


                            elif move == "JEOPARDY":
                                success_option = p_obj.attack("JEOPARDY")
                                if success_option == 0:

                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 15) * enemy_deff  # Nicholas: infer from past comments

                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 15) * enemy_deff)  # Nicholas: infer from past comments

                                else:
                                    enemy_hp -= ((player_atk + 15) * enemy_deff) / 2  # Nicholas: infer from past comments


                            else:
                                print("How Did it not work")

                            good2go = True

            while not good2go:
                if enemy_hp <= 0:
                    enemy_hp = 0
                    print("\nEnemy Health:", int(enemy_hp))
                    print("Your Health:", int(player_hp))
                elif player_hp <= 0:
                    player_hp = 0
                    print("\nEnemy Health:", int(enemy_hp))
                    print("Your Health:", int(player_hp))

            else:
                #Boss will randomly choose what to do and, and do it
                Boss_options = Boss_battle_List
                move = random.choice(Boss_options)
                Boss_options.pop(move)
                if move == 'Attack':
                    cr_obj.attack()
                elif move == 'Block':
                    cr_obj.block()
                else:
                    cr_obj.spec_atk

                if enemy_hp <= 0:
                    enemy_hp = 0
                elif player_hp <= 0:
                    player_hp = 0
                else:
                    pass
                print("\nEnemy Health:", int(enemy_hp))
                print("Your Health:", int(player_hp))
                print()



        elif battle_choice == 'Block':
            if p_obj.block():
                player_hp -= (enemy_atk * player_deff) * .2
                print()
            else:
                player_hp -= (enemy_atk * player_deff)

            print("\nEnemy Health:", int(enemy_hp))
            print("Your Health:", int(player_hp))
            print()



        elif battle_choice == 'Info':
            p_obj.HELP() # Info from player
            print()
            print()


        elif battle_choice == 'Inspect':
            cr_obj.stats()  # Stats from creature
            print()












