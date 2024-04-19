#
# GAVIN
# 4/18/24
# Main function for game
import Boss
import Player
import Creature
import Story
import Shop, sprites_and_shii
from time import sleep
import os


def main():
    for line in sprites_and_shii.title_card.splitlines():
        print(f"{line}")
        sleep(.45)
    print('\n\n')
    sleep(1.2)

    # Character select : Gavin
    print("Choose your character:")
    sleep(.8)
    for line in sprites_and_shii.characters.splitlines():
        print(line)
        sleep(.34)
    print("\nEnter character: [GC / WR]")
    char = input("\t- ").upper().strip()
    pl_name = str(input("Enter the characters name\n\t- ").title().strip())
    sleep(1.2)
    print("Creating Character...")
    sleep(1.2)
    print("Success, transporting character to metaverse...")

    # Creating objects for character...
    if char == 'GC' or char == 'GC'[0:len(char)]:
        player_character = Player.Player(pl_name, 120, 5, 80)
    elif char == 'WR' or char == 'WR'[0:len(char)]:
        player_character = Player.Player(im GOING TO KILL MYSELF, 75, 12, 120)
    print(player_character.name)
    player_character.stats()

main()