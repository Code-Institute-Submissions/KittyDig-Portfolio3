# run.py
from game import BattleshipsGame

def main():
    while True:
        try:
            # logic for giving the player the option to choose between a computer controlled opponant or another person
            print("Choose your opponent:")
            print("1. Play against a local player")
            print("2. Play against the computer")

            choice = int(input("Enter 1 or 2: "))
                        
            if choice == 1:
                player_type = "human"
            elif choice == 2:
                player_type = "computer"
            else:
                print("Invalid choice. Please enter 1 or 2.")
                continue  # goes back to the beginning of the loop

            game = BattleshipsGame(player2_type=player_type)
            game.setup_game()
            game.play()
            break  # exits the loop if the game has been played

        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()

# a much more basic version of def main() in this section was derived from code found on:
# https://codereview.stackexchange.com/questions/164697/game-of-battleship-2-player-python