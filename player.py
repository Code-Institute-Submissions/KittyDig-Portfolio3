# player.py

class Player:
    def __init__(self, name):
        """ initializes the player """
        self.name = name

    def make_guess(self, opponent_board):
        """ gets the player's guess """
        while True:
            try:
                row = int(input(f"{self.name}, enter the row for your guess: "))
                col = int(input(f"{self.name}, enter the column for your guess: "))

                # checks if the input is within the valid range,
                # if it is not, it tells the user it is an invalid move
                if 1 <= row <= opponent_board.size and 1 <= col <= opponent_board.size:
                    return row, col
                else:
                    print("Invalid move. Please enter valid row and column numbers.")

            except ValueError:
                print("Invalid input. Please enter numeric values for row and column.")


# structure and logic in this section
# was derived from code found on:
# https://codereview.stackexchange.com/questions/164697/game-of-battleship-2-player-python
