import time  # Nicholas: for pauses
import random  # Nicholas: implement chance in moves
import Creature
import Player
Option_battle_list = ['Attack', 'Block', "Info", "Inspect"]
Quiz_Types = ["MCQ", "JEOPARDY", "FITB", "TFQ"]  # Nicholas: List of the quiz types for the if/else statements

creature_object = Creature.Creature("Craig", 'Nothin',random.randint(50,90),12, 60)
player_object = Player.Player("Pame",75,12, 101)

def assignment(p_obj, cr_obj):
    global enemy_hp, player_hp, enemy_atk, player_atk, enemy_deff, player_deff
    enemy_hp = cr_obj.hp
    player_hp = p_obj.hp
    enemy_atk = cr_obj.atk
    player_atk = p_obj.atk
    enemy_deff = cr_obj.deff * .01
    player_deff = p_obj.deff * .01


assignment(player_object, creature_object)



def battling(boss, Option_battle_list): # Nicholas: Boss should be boolean, nothing yet
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
                                success_option = player_object.attack("TFQ")  # Nicholas: Easy difficulty of questions
                                if success_option == 0:
                                    print("miss")
                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk) * enemy_deff
                                    print("normal")
                                elif success_option == 3:
                                    enemy_hp -= 1.5*((player_atk) * enemy_deff)
                                    print("Crit")
                                else:
                                    enemy_hp -= ((player_atk) * enemy_deff)/2
                                    print("half")



                            elif move == "MCQ":
                                success_option = player_object.attack("MCQ")  # Nicholas: Medium difficulty of questions
                                if success_option == 0:
                                    print("miss")
                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 5) * enemy_deff
                                    print("normal") # Nicholas: Player attack with damage boost of 5 multiplied by the enemy's defense(%), Normal
                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 5) * enemy_deff)
                                    print("Crit") # Nicholas: Player attack with damage boost of 5 multiplied by the enemy's defense(%), Crit
                                else:
                                    enemy_hp -= ((player_atk + 5) * enemy_deff) / 2
                                    print("half") # Nicholas: Player attack with damage boost of 5 multiplied by the enemy's defense(%), Halved

                            elif move == "FITB":
                                success_option = player_object.attack("FITB")  # Nicholas: Hard difficulty of questions
                                if success_option == 0:
                                    print("miss")
                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 10) * enemy_deff
                                    print("normal")  # Nicholas: Player attack with damage boost of 10 multiplied by the enemy's defense(%), Normal
                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 10) * enemy_deff)  # Nicholas: Player attack with damage boost of 10 multiplied by the enemy's defense(%), Crit by 1.5
                                    print("Crit")
                                else:
                                    enemy_hp -= ((player_atk + 10) * enemy_deff) / 2 # Nicholas: Player attack with damage boost of 10 multiplied by the enemy's defense(%), Halved
                                    print("half")

                            elif move == "JEOPARDY":
                                success_option = player_object.attack("JEOPARDY") # Nicholas: Hard difficulty of questions
                                if success_option == 0:
                                    print("miss")
                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 15) * enemy_deff # Nicholas: infer from past comments
                                    print("normal")
                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 15) * enemy_deff)  # Nicholas: infer from past comments
                                    print("Crit")
                                else:
                                    enemy_hp -= ((player_atk + 15) * enemy_deff) / 2  # Nicholas: infer from past comments
                                    print("half")


                            else:
                                print("How Did it not work")

                            good2go = True
                            break

                    elif len(move) == 1:
                        if move == Quiz_Types[i][0]:
                            move = Quiz_Types[i]
                            if move == "TFQ":
                                success_option = player_object.attack("TFQ")
                                if success_option == 0:
                                    print("miss")
                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk) * enemy_deff  # Nicholas: infer from past comments
                                    print("normal")
                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk) * enemy_deff)  # Nicholas: infer from past comments
                                    print("Crit")
                                else:
                                    enemy_hp -= ((player_atk) * enemy_deff) / 2  # Nicholas: infer from past comments
                                    print("half")


                            elif move == "MCQ":
                                success_option = player_object.attack("MCQ")
                                if success_option == 0:
                                    print("miss")
                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 5) * enemy_deff  # Nicholas: infer from past comments
                                    print("normal")
                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 5) * enemy_deff)  # Nicholas: infer from past comments
                                    print("Crit")
                                else:
                                    enemy_hp -= ((player_atk + 5) * enemy_deff) / 2  # Nicholas: infer from past comments
                                    print("half")


                            elif move == "FITB":
                                success_option = player_object.attack("FITB")
                                if success_option == 0:

                                    pass
                                elif success_option == 1:
                                    enemy_hp -= (player_atk + 10) * enemy_deff  # Nicholas: infer from past comments

                                elif success_option == 3:
                                    enemy_hp -= 1.5 * ((player_atk + 10) * enemy_deff)  # Nicholas: infer from past comments

                                else:
                                    enemy_hp -= ((player_atk + 10) * enemy_deff) / 2  # Nicholas: infer from past comments


                            elif move == "JEOPARDY":
                                success_option = player_object.attack("JEOPARDY")
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
                    print("Enemy Health:", int(enemy_hp))
                    print("Your Health:", int(player_hp))
                elif player_hp <= 0:
                    player_hp = 0
                    print("Enemy Health:", int(enemy_hp))
                    print("Your Health:", int(player_hp))

            else:
                player_hp -= enemy_atk * player_deff  # BUFF ENEMY - Implement the randomness
                if enemy_hp <= 0:
                    enemy_hp = 0
                elif player_hp <= 0:
                    player_hp = 0
                else:
                    pass
                print("Enemy Health:", int(enemy_hp))
                print("Your Health:", int(player_hp))
                print()
            battle_choice = input(f'Choose what to do {Option_battle_list[:4]}: ').title()


        elif battle_choice == 'Block':
            if player_object.block():
                player_hp -= (enemy_atk * player_deff) / 1.25
                print()
            else:
                player_hp -= (enemy_atk * player_deff)

            print("Enemy Health:", int(enemy_hp))
            print("Your Health:", int(player_hp))
            print()

            battle_choice = input(f'Choose what to do {Option_battle_list[:4]}: ').title()

        elif battle_choice == 'Info':
            player_object.help() # Info from player
            print()
            print()
            battle_choice = input(f'Choose what to do {Option_battle_list[:4]}: ').title()

        elif battle_choice == 'Inspect':
            creature_object.stats()  # Stats from creature
            print()
            battle_choice = input(f'Choose what to do {Option_battle_list[:4]}: ').title()




