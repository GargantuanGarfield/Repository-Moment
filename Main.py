#
# GAVIN
# 4/18/24
# Main function for game
import random

import Battle
import Boss
import Player
import Creature
import Story
import Shop, sprites
from time import sleep
import os
import Filesaver

#Main function : Gavin
def main():
    os.system('cls')
    for line in sprites.title_card.splitlines():
        print(f"{line}")
        sleep(.45)
    print('\n\n')
    sleep(1.2)



    print("Choose your character:")
    sleep(.8)
    for line in sprites.characters.splitlines():
        print(line)
        sleep(.34)

    char = ''
    pl_name = input("Enter the characters name\n\t- ").title().strip()
    # Inputs and Creating objects for character...
    while True:
        print("\nEnter character: [GC / WR]")
        char = input("\t- ").upper().strip()
        sleep(1.2)
        if char == 'GC' or char == 'GC'[0:len(char)]:
            player_character = Player.Player(pl_name, 135, 5, 80)
            break
        elif char == 'WR' or char == 'WR'[0:len(char)]:
            player_character = Player.Player(pl_name, 100, 12, 120)
            break



    print("Creating Character...")
    sleep(1.2)
    print("Success, transporting character to metaverse...")
    sleep(2)
    os.system('cls')
    player_character.HELP()
    input("\n - Press ENTER button to continue - \n\t\t")
    os.system('cls')
    # runs the intro story text
    Story.intro()
    input("\n - Press ENTER button to continue - \n\t\t")
    os.system('cls')

    # Battle 1 dialogue
    Story.battle1()
    sleep(1.2)
    print("Huh?")
    input("\n - Press ENTER button to continue - \n\t\t")

    # Assigning the enemy object
    enemy_obj = Creature.Creature( 'Craig', 'Operator', random.randint(70, 80), 12, 30)
    os.system('cls')
    print(f"ENCOUNTER - A wild {enemy_obj.name} approaches")

    # Sets up battle
    Battle.battling(Battle.Option_battle_list, player_character, enemy_obj)

    if player_character.hp <= 0: #runs game over if player dead
        Story.game_over(player_character.score, pl_name)




    #Shop and battle 2 dialogue
    os.system('cls')
    print("You find a strange building in portland..")
    sleep(.5)
    print("looks like a store..", end=' ')
    input("\n - Press ENTER button to continue - \n\t\t")
    sleep(.34)
    print("You decide to head inside")

    Shop.shop(player_character)

    os.system('cls')
    enemy_obj = Creature.Creature('CHEEF THEEF - Neurichlas', 'EPIC', random.randint(75, 110), 18, 60)
    Story.battle2()
    input("\n - Press ENTER button to continue - \n\t\t")

    # Sets up battle
    Battle.battling(Battle.Option_battle_list, player_character, enemy_obj)

    if player_character.hp <= 0: #runs game over if player dead
        Story.game_over(player_character.score, pl_name)

    os.system('cls')
    # Increases user stats
    print("LEVEL UP!!!\n\tATTACK UP!!\n\tDEFENSE UP!!\n\tHP INCREASED!!!")
    print(f'atk += 30')
    print(f'deff += 8')
    print(f'hp += 30')
    player_character.atk += 30
    player_character.deff += 8
    player_character.hp += 30

    # Shop and battle 3 dialogue
    enemy_obj = Creature.Creature('The Amalgam', 'EPIC', random.randint(80, 95), 14, 85)
    os.system('cls')
    print('You find another shop..')
    sleep(1.2)
    Shop.shop(player_character)
    os.system('cls')

    Story.battle3()
    input("\n - Press ENTER button to continue - \n\t\t")

    # Sets up battle
    os.system('cls')
    Battle.battling(Battle.Option_battle_list, player_character, enemy_obj)

    if player_character.hp <= 0:  # runs game over if player dead
        Story.game_over(player_character.score, pl_name)

    os.system('cls')
    # Increases user stats
    print("LEVEL UP!!!\n\tATTACK UP!!\n\tDEFENSE UP!!\n\tHP INCREASED!!!")
    print(f'atk += 60')
    print(f'deff += 10')
    print(f'hp += 55')
    player_character.atk += 60
    player_character.deff += 10
    player_character.hp += 55

    # BOSS BATTLE!!!!!
    enemy_obj = Boss.Boss('The PYTHON - Syed', 110, 20, 125)
    os.system('cls')
    print('You find network chuck\'s swap shop shop..')
    sleep(1.2)
    Shop.shop(player_character)
    os.system('cls')

    Story.battle4()
    input("\n - Press ENTER button to continue - \n\t\t")

    # Sets up battle
    os.system('cls')
    Battle.battling(Battle.Option_battle_list, player_character, enemy_obj)

    if player_character.hp <= 0:  # runs game over if player dead
        Story.game_over(player_character.score, pl_name)

    os.system('cls')
    Story.outro()
    Filesaver.full_process(player_character.score, pl_name)
    sleep(5)






main()