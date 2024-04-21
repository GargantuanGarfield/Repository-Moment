# Will Vanderploeg
import pickle
import os


# Sorts, then saves the highscore in a binary file
def savehighscore(score, name, names, scores_list):
    try:
        high = open("Highscores.dat", "wb")
        scores_list.append(score)
        names.append(name)
        score_table_temp = {names[i]: scores_list[i] for i in range(len(names))}  # reference dictionary
        scores_list.sort(reverse=True)
        scores_table = {}
        # This is what pieces back the new dictionary
        for value in scores_list:
            for item in score_table_temp:
                if value == score_table_temp[item]:  # Checks if the combo matches the correct combo in the reference dictionary
                    scores_table[item] = value
        pickle.dump(scores_table, high)
        high.close()
        return scores_table

    except FileNotFoundError:
        print("File not found")


# Reads a binary file to retrieve past highscores
# Splits the dictionary into its keys and values and returns them
def readhighscores():
    high = open("Highscores.dat", 'rb')
    try:
        score_table = pickle.load(high)
    except EOFError:
        score_table = {}
    names = list(score_table.keys())
    scores = list(score_table.values())
    names, scores, redo = check(names, scores)  # redo isn't used here, just to make the program happy
    high.close()
    return names, scores  # returns the specific aspects of Highscores.dat

# Displays all the highscores, sorted and in nice format
def displayscores(scores, clear=True):
    if clear is True:
        os.system('cls')
    print("High Scores:")
    print("________________________")
    counter = 0
    for value in scores:
        counter += 1
        print(f"{counter}: {value} -- {scores[value]}")

# Function to keep line counts down, by optimally using all the function specified in this file
# Also allows the specification of whether the function should return the score_table
def full_process(score, name, return_table=False):
    names, scores = readhighscores()
    score_table = savehighscore(score, name, names, scores)
    names, scores, redo = check(names, scores)
    if redo is True:  # This is where the redo value tells the program to either save again or continue
        score_table = savehighscore(score, name, names, scores)
    if return_table is True:
        return score_table
    else:
        displayscores(score_table)


def check(names, scores):
    redo = False
    if len(names) == 0:  # Checks if the Highscores.dat function is empty and adds a placeholder to ward off errors
        names.append("placeholder")
        scores.append(0)
        print("\n-No scores found-\n")
    elif len(names) != 0 and "placeholder" in names:  # Will get rid of it if a real value is in the file
        redo = True  # returns redo to tell the program to save again so the placeholder will never be displayed
        delete1 = names.index("placeholder")
        delete2 = scores.index(0)
        del names[delete1]
        del scores[delete2]
    return names, scores, redo

