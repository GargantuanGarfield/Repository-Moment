#
# Co-coded by pretty much everyone.
# 4/17/24
# Main function for game
import Filesaver
import Player

def main():

    test_player = Player.Player("Liam", 0, 0, 100, 'chilling', '', '', 96)
    names, scores = Filesaver.readhighscores()
    score_table = Filesaver.savehighscore(test_player.score, test_player.name, names, scores)
    Filesaver.displayscores(score_table)





main()