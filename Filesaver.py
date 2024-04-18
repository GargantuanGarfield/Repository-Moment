import pickle
import os



def savehighscore(score, name, names, scores_list):
    try:
        high = open("Highscores.dat", "wb")
        scores_list.append(score)
        names.append(name)
        score_table_temp = {names[i]: scores_list[i] for i in range(len(names))}
        print(scores_list)
        scores_list.sort(reverse=True)
        scores_table = {}
        for value in scores_list:
            for item in score_table_temp:
                if value == score_table_temp[item]:
                    scores_table[item] = value
        pickle.dump(scores_table, high)
        high.close()
        print("\nFile Saved\n")
    except FileNotFoundError:
        print("File not found")


def readhighscores():
    high = open("Highscores.dat", 'rb')
    score_table = pickle.load(high)
    names = list(score_table.keys())
    values = list(score_table.values())
    high.close()
    return score_table, names, values


def displayscores(scores):
    os.system('cls')
    print("High Scores")
    print("________________________")
    counter = 0
    for value in scores:
        counter += 1
        print(f"{counter}: {value} -- {scores[value]}")


values = []
names = []


while True:
    name = input("What is your name?:\n")
    score = int(input("What is your score?:\n"))
    scores, names, values = readhighscores()
    savehighscore(score, name, names, values)
    scores, names, values = readhighscores()
    print(scores)
    displayscores(scores)

