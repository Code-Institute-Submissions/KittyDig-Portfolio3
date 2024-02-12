# run.py
from game import BattleshipsGame

def main():
    # creates an instance of the BattleshipsGame class
    game = BattleshipsGame()

    # sets up the game
    game.setup_game()

    # plays the game
    game.play()

if __name__ == "__main__":
    main()