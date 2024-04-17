import time  # Nicholas: for pauses
import random  # Nicholas: implement chance in moves
import Questions
Option_battle_list = ['Attack', 'Block']
Quiz_Types = ["MC", "JEOPARDY", "FITB", "TOF"]  # Nicholas: List of the quiz types for the if/else statements
def battling(enemy, player):
    while enemy.hp > 0 and player.hp:  # Nicholas: code runs until player or enemy dies

        battle_choice = input(f'Choose what to do {Option_battle_list}: ').title()
        while battle_choice not in Option_battle_list:  # runs until battle_choice is valid
            battle_choice = input(f'Choose what to do {Option_battle_list}: ').title()

        if battle_choice == 'Attack':

            quiz_choice = input(f'you can choose: {Quiz_Types}: ').capitalize()
            if quiz_choice in Quiz_Types:
                if quiz_choice == 'MC':
                    pass
                        # TODO enemy.hp -= player.atk
                        # TODO print(f'{enemy.name} has {enemy.hp} health!')

                elif quiz_choice == 'JEOPARDY':
                    pass
                        # TODO ratHealth -= player.atk
                        # TODO print(f'{enemy.name} has {enemy.hp} health!')

                elif quiz_choice == 'FITB':
                    pass
                        # TODO enemy.hp -= player.atk
                        # TODO print(f'{enemy.name} has {enemy.hp} health!')

                elif quiz_choice == 'TOF':
                    pass
                        # TODO enemy.hp -= player.atk
                        # TODO print(f'{enemy.name} has {enemy.hp} health!')
                else:
                    print('Not a move try again.')
                # Nicholas: TODO Must add player lose health
        elif battle_choice == 'Block':
            pass  # Need To Implement Block









