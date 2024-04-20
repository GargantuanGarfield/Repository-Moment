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
import Shop, sprites_and_shii
from time import sleep
import os

#Main function : Gavin
def main():
    os.system('cls')
    for line in sprites_and_shii.title_card.splitlines():
        print(f"{line}")
        sleep(.45)
    print('\n\n')
    sleep(1.2)



    print("Choose your character:")
    sleep(.8)
    for line in sprites_and_shii.characters.splitlines():
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
            player_character = Player.Player(pl_name, 120, 5, 80)
            break
        elif char == 'WR' or char == 'WR'[0:len(char)]:
            player_character = Player.Player(pl_name, 75, 12, 120)
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
    enemy_obj = Creature.Creature( 'Craig', 'Operator', random.randint(100, 130), 12, 30)
    os.system('cls')
    print(f"ENCOUNTER - A wild {enemy_obj.name} approaches")

    # Sets up battle
    Battle.battling(False, Battle.Option_battle_list, player_character, enemy_obj)

    if player_character.hp <= 0: #runs game over if player dead
        Story.game_over()




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
    enemy_obj = Creature.Creature('CHEEF THEEF - Neurichlas', 'EPIC', random.randint(110, 140), 18, 60)
    Story.battle2()
    input("\n - Press ENTER button to continue - \n\t\t")

    # Sets up battle
    Battle.battling(False, Battle.Option_battle_list, player_character, enemy_obj)

    if player_character.hp <= 0: #runs game over if player dead
        Story.game_over()

    os.system('cls')
    # Increases user stats
    print("LEVEL UP!!!\n\tATTACK UP!!\n\tDEFENSE UP!!\n\tHP INCREASED!!!")
    print(f'atk += 20')
    print(f'deff += 2')
    print(f'hp += 15')
    player_character.atk += 20
    player_character.deff += 2
    player_character.hp += 15

    # Shop and battle 3 dialogue
    enemy_obj = Creature.Creature('The Amalgam', 'EPIC', random.randint(150, 190), 14, 100)
    os.system('cls')
    print('You find another shop..')
    sleep(1.2)
    Shop.shop(player_character)
    os.system('cls')

    Story.battle3()
    input("\n - Press ENTER button to continue - \n\t\t")

    # Sets up battle
    os.system('cls')
    Battle.battling(False, Battle.Option_battle_list, player_character, enemy_obj)

    if player_character.hp <= 0:  # runs game over if player dead
        Story.game_over()

    os.system('cls')
    # Increases user stats
    print("LEVEL UP!!!\n\tATTACK UP!!\n\tDEFENSE UP!!\n\tHP INCREASED!!!")
    print(f'atk += 30')
    print(f'deff += 4')
    print(f'hp += 30')
    player_character.atk += 30
    player_character.deff += 4
    player_character.hp += 30

    # BOSS BATTLE!!!!!
    enemy_obj = Boss.Boss('The PYTHON - Syed', 250, 20, 150)
    os.system('cls')
    print('You find network chuck\'s swap shop shop..')
    sleep(1.2)
    Shop.shop(player_character)
    os.system('cls')

    Story.battle4()
    input("\n - Press ENTER button to continue - \n\t\t")

    # Sets up battle
    os.system('cls')
    BossBattle.battling(True, Battle.Option_battle_list, player_character, enemy_obj)

    if player_character.hp <= 0:  # runs game over if player dead
        Story.game_over()

    os.system('cls')




main()