# run.py
from game import BattleshipsGame

def main():
    print("Choose your opponent:")
    print("1. Play against Another Player")
    print("2. Play against Computer")

    choice = input("Enter 1 or 2: ")

    # logic to ask the player if they want to play against another player or computer
    if choice == "1":
        game = BattleshipsGame(player2_type="human")
    elif choice == "2":
        game = BattleshipsGame(player2_type="computer")
    else:
        print("Invalid choice. Please enter 1 or 2.")
        return

    game.setup_game()
    game.play()

if __name__ == "__main__":
    main()

# a much more basic version of def main() in this section was derived from code found on:
# https://codereview.stackexchange.com/questions/164697/game-of-battleship-2-player-python