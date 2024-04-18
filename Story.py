
import random
from time import sleep
# Will Vanderploeg:
# Displays the intro one line at a time using the intro.txt file
def intro():
    year = random.randrange(224, 8427)
    print(f"\n\nThe year is {year}")
    sleep(1)
    intro = open("intro.txt", "r")
    for i in range(12):
        print(intro.readline())
        sleep(.87)
    intro.close()

intro()
