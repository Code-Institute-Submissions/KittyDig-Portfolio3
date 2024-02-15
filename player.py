# player.py

class Player:
    def __init__(self, name):
        """ initializes the player """
        self.name = name

    def make_guess(self, opponent_board):
        """ gets the player's guess """
        row = int(input(f"{self.name}, enter the row for your guess: "))
        col = int(input(f"{self.name}, enter the column for your guess: "))
        return row, col