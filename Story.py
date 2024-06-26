#
# Gavin and Will
# 4/whatever/24
# fucntions for the text element of story parts
import random
from time import sleep
import os
import hazbin
import Filesaver

# Will Vanderploeg:
# Displays the intro one line at a time using the intro.txt file
def intro():
    year = random.randrange(224, 8427)
    print(f"\n\nThe year is {year}")
    sleep(1)
    intro = open("intro.txt", "r")
    for i in range(12):
        print('| ' + intro.readline())
        sleep(2)
    intro.close()

# Gavin M.
def game_over(score, name):
    death = """\t\t░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
\t\t░   ░░░░░░   ░░░░░     ░░░░░░   ░░░░░   ░░░░░░░      ░░░░░   ░         ░      ░░░░
\t\t▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒▒   ▒▒▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒   ▒▒   ▒   ▒▒▒▒▒▒▒   ▒▒▒   ▒
\t\t▒▒▒   ▒   ▒▒▒▒   ▒▒▒▒▒▒▒▒   ▒   ▒▒▒▒▒   ▒▒▒▒▒▒▒   ▒▒▒▒   ▒   ▒   ▒▒▒▒▒▒▒   ▒▒▒▒   
\t\t▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓   ▓   ▓       ▓▓▓   ▓▓▓▓   
\t\t▓▓▓▓▓   ▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓▓   ▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓▓   
\t\t▓▓▓▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓▓▓   ▓▓   ▓▓▓▓▓   ▓▓▓▓▓▓▓   ▓▓▓   ▓▓   ▓   ▓▓▓▓▓▓▓   ▓▓▓   ▓
\t\t█████   ██████████     ████████      ██████████      █████   █         █      ████
\t\t██████████████████████████████████████████████████████████████████████████████████"""
    for line in death.splitlines():
        print(line)
        sleep(.34)
    print("Try again? (y/n)")
    again = input("\t").lower()
    print()
    while True:
        if again == 'y':
            print("You feel a strange surging of determi--")
            sleep(1.8)
            print("\t-Empowerment..")
            sleep(2)
            score_table = Filesaver.full_process(score, name, True)
            count = 5
            for time in range(5):
                os.system("cls")
                print(f"Continuing in: {count}")
                Filesaver.displayscores(score_table, False)
                sleep(1)
                count -= 1
            os.system('cls')
            sleep(1.5)
            print("Too bad :(")
            sleep(.75)
            print("you\'re literally dead..", end=' ')
            sleep(2)
            print('L')
            sleep(2)
            quit()
        elif again == 'n':
            Filesaver.full_process(score, name)
            sleep(5)
            quit()
        else:
            print('huh?')
            sleep(4)
            print("\nTry again? (y/n)")
            again = input("\t").lower()

# Liam
# Opens story dialogue leading into the first player battle.
def battle1():
    battle1 = open('battle1-portland.txt', 'r')
    for i in range(5):
        print('| ' + battle1.readline())
        sleep(2)
    battle1.close()


# Opens story dialogue leading into the second player battle.
def battle2():
    battle2 = open('battle2-thieves', 'r')
    for i in range(8):
        print('| ' + battle2.readline())
        sleep(2)
    battle2.close()


# Opens story dialogue leading into the third player battle.
def battle3():
    battle3_pt1 = open('battle3-hazbinhotel', 'r')
    battle3_pt2 = open('battle3-hazbinhotel-pt2', 'r')

    for i in range(8):
        print('| ' + battle3_pt1.readline())
        sleep(2)
    os.system('cls')

    for line in hazbin.Hazbin.splitlines():
        print(line)
        sleep(.1)
    for i in range(8):
        print('| ' + battle3_pt2.readline())
        sleep(2)

    battle3_pt1.close()
    battle3_pt2.close()


# Opens story dialogue leading into the fourth player battle.
def battle4():
    battle4 = open('battle4-boss', 'r')
    for i in range(13):
        print(battle4.readline())
        sleep(2)
    battle4.close()

# Outro dialogue
def outro():
    outro = open('outro', 'r')
    for i in range(14):
        print(outro.readline())
        sleep(2)
    outro.close()


