import pickle

scores_list = [12, 14, 20, 18, 100]
names = ["nick", "will", "gavin", "liam", "mew"]
def savehighscore(score, name):
    try:
        high = open("Highscores.dat", "wb")
        scores_list.append(score)
        names.append(name)
        score_table = {scores_list[i]: names[i] for i in range(len(names))}
        score_table = dict(sorted(score_table.items()))
        print(score_table)
        pickle.dump(score_table, high)
        high.close()
    except FileNotFoundError:
        print("File not found")


def readhighscores():
    high = open("Highscores.dat", 'rb')
    score_table = pickle.load(high)
    high.close()
    return score_table

def displayscores():
    pass


