#
# Gavin and Will
# 4/whatever/24
# fucntions for the text element of story parts
import random
from time import sleep
import Main

# Will Vanderploeg:
# Displays the intro one line at a time using the intro.txt file
def intro():
    year = random.randrange(224, 8427)
    print(f"\n\nThe year is {year}")
    sleep(.87)
    intro = open("intro.txt", "r")
    for i in range(12):
        print(intro.readline().strip())
        sleep(.87)
    intro.close()


# Gavin M.
def game_over():
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
            print("You feel a stange surging of determi--")
            sleep(.8)
            print("\tEmpowerment..", end=" ")
            sleep(1)
            print("Anyway lets try again.")
            Main.main()
            break
        elif again == 'n':
            quit()
        else:
            print('huh?')
            sleep(4)
            print("\nTry again? (y/n)")
            again = input("\t").lower()

game_over()
