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

    print("\nEnter character: [GC / WR]")
    char = input("\t- ").upper().strip()
    pl_name = input("Enter the characters name\n\t- ").title().strip()
    if char == 'GC' or char == 'GC'[0:len(char)]:
        player_character = Player.Player(pl_name, 120, 5, 60)
    elif char == 'WR' or char == 'WR'[0:len(char)]:
        player_character = Player.Player(pl_name, 75, 12, 80)
    # Inputs and Creating objects for character...
    while char != 'GC' or char != 'GC'[0:len(char)] or char == 'WR' or char == 'WR'[0:len(char)]:
        print("\nEnter character: [GC / WR]")
        char = input("\t- ").upper().strip()
        sleep(1.2)
        if char == 'GC' or char == 'GC'[0:len(char)]:
            player_character = Player.Player(pl_name, 120, 5, 80)
        elif char == 'WR' or char == 'WR'[0:len(char)]:
            player_character = Player.Player(pl_name, 75, 12, 120)

    print("Creating Character...")
    sleep(1.2)
    print("Success, transporting character to metaverse...")
    os.system('cls')

    # runs the intro story text
    Story.intro()
    sleep(3)

    # Battle 1 dialogue
    Story.battle1()
    sleep(1.2)
    print("Huh?")
    sleep(.2)
    if player_character.hp <= 0: #runs game over if player dead
        Story.game_over()


    # Assigning the enemy object
    enemy_obj = Creature.Creature(30, 'Craig', 'Operator', random.randint(50,90), 12)
    print("ENCOUNTER")

    # Sets up battle
    Battle.assignment(enemy_obj, player_character)
    Battle.battling(False, Battle.Option_battle_list)

    #Shop and battle 2 dialogue
    print("You find a strange building in portland..")
    sleep(.5)
    print("looks like a store..", end=' ')
    sleep(.34)
    print("You decide to head inside")

    Shop.shop(player_character)

    enemy_obj = Creature.Creature(60, 'CHEEF THEEF - Neurichlas', 'EPIC', random.randint(50,65), 18)
    Story.battle2()
    sleep(1.2)

    # Sets up battle
    Battle.assignment(enemy_obj, player_character)
    Battle.battling(False, Battle.Option_battle_list)

    if player_character.hp <= 0: #runs game over if player dead
        Story.game_over()

    # Increases user stats
    print("LEVEL UP!!!\n\tATTACK UP!!\n\tDEFENSE UP!!\n\tHP INCREASED!!!")
    player_character.atk += 20
    player_character.deff += 2
    player_character.hp += 15

    # Shop and battle 3 dialogue
    enemy_obj = Creature.Creature(100, 'The Amalgam', 'EPIC', random.randint(95,140), 14)

    print('You find another shop..')
    sleep(1.2)
    Shop.shop(player_character)

    Story.battle3()
    sleep(1.2)

    # Sets up battle
    Battle.assignment(enemy_obj, player_character)
    Battle.battling(False, Battle.Option_battle_list)

    if player_character.hp <= 0:  # runs game over if player dead
        Story.game_over()

    # Increases user stats
    print("LEVEL UP!!!\n\tATTACK UP!!\n\tDEFENSE UP!!\n\tHP INCREASED!!!")
    player_character.atk += 30
    player_character.deff += 4
    player_character.hp += 30

    # BOSS BATTLE!!!!!
    enemy_obj = Boss.Boss('The PYTHON - Syed', 200, 20, 150)

    print('You find another shop..')
    sleep(1.2)
    Shop.shop(player_character)

    Story.battle3()
    sleep(1.2)

    # Sets up battle
    Battle.assignment(enemy_obj, player_character)
    Battle.battling(False, Battle.Option_battle_list)

    if player_character.hp <= 0:  # runs game over if player dead
        Story.game_over()

    # Increases user stats
    print("LEVEL UP!!!\n\tATTACK UP!!\n\tDEFENSE UP!!\n\tHP INCREASED!!!")
    player_character.atk += 30
    player_character.deff += 4
    player_character.hp += 30



main()