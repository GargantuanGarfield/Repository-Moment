from time import sleep
import hazbin


# Opens story dialogue leading into the first player battle.
def battle1():
    battle1 = open('battle1-portland.txt', 'r')
    for i in range(5):
        print(battle1.readline())
        sleep(.87)
    battle1.close()


# Opens story dialogue leading into the second player battle.
def battle2():
    battle2 = open('battle2-thieves', 'r')
    for i in range(8):
        print(battle2.readline())
        sleep(.87)
    battle2.close()


# Opens story dialogue leading into the third player battle.
def battle3():
    battle3_pt1 = open('battle3-hazbinhotel', 'r')
    battle3_pt2 = open('battle3-hazbinhotel-p2', 'r')

    for i in range(8):
        print(battle3_pt1.readline())
        sleep(.87)

    for line in hazbin.Hazbin.splitlines():
        print(line)
        sleep(.1)

    for i in range(8):
        print(battle3_pt2.readline())
        sleep(.87)

    battle3_pt1.close()
    battle3_pt2.close()


# Opens story dialogue leading into the fourth player battle.
def battle4():
    battle4 = open('battle4-boss', 'r')
    for i in range(13):
        print(battle4.readline())
        sleep(.87)
    battle4.close()


# Outro dialogue
def outro():
    outro = open('outro', 'r')
    for i in range(14):
        print(outro.readline())
        sleep(.87)
    outro.close()
