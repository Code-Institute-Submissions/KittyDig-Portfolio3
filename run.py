# run.py
from game import BattleshipsGame

def main():
    ''' creates an instance of the BattleshipsGame class '''
    game = BattleshipsGame()

    ''' sets up the game '''
    game.setup_game()

    ''' plays the game '''
    game.play()

if __name__ == "__main__":
    main()


# a much more basic version of def main() in this section was derived from code found on:
# https://codereview.stackexchange.com/questions/164697/game-of-battleship-2-player-python