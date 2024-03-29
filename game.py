# game.py

from board import Board
from player import Player
import random


class BattleshipsGame:
    def __init__(self, player2_type):
        ''' initializes the game '''
        self.player1 = Player("Player 1")
        if player2_type == "computer":
            self.player2 = Player("Computer")
        else:
            self.player2 = Player("Player 2")
        self.board1 = Board(size=5, player=1)
        self.board2 = Board(size=5, player=2)

    def setup_game(self):
        ''' sets up the game, including board size and placing the ships '''
        for _ in range(2):  # places 2 ships on each board
            self.board1.place_ship(2, random.choice(['H', 'V']))
            self.board2.place_ship(2, random.choice(['H', 'V']))

    def play(self):
        ''' main game loop '''
        print("""
  ____        _   _   _           _     _  
 |  _ \      | | | | | |         | |   (_)
 | |_) | __ _| |_| |_| | ___  ___| |__  _ _ __  ___
 |  _ < / _` | __| __| |/ _ \/ __| '_ \| | '_ \/ __|
 | |_) | (_| | |_| |_| |  __/\__ \ | | | | |_) \__ \ 
 |____/ \__,_|\__|\__|_|\___||___/_| |_|_| .__/|___/
                                         | |
                                         |_|
Rules:
1. You have a fleet of ships on a 5x5 grid
2. Ships are placed randomly either horizontally or vertically
3. Each player takes turns guessing the coordinates to attack
4. 'X' represents a hit, 'O' represents a miss
5. The first player to sink all the opponent's ships wins.
        """)

        while not (self.board1.all_ships_sunk() or self.board2.all_ships_sunk()):
            # player 1's turn
            guess1 = self.player1.make_guess(self.board2)
            result1 = self.board2.receive_attack(*guess1)
            print(f"{self.player1.name} attacks {guess1} - Result: {result1}")
            self.board2.display()

            if self.board2.all_ships_sunk():
                break

            # player 2's turn
            if self.player2.name == "Computer":
                guess2 = self.computer_make_guess(self.board1)
            else:
                guess2 = self.player2.make_guess(self.board1)

            result2 = self.board1.receive_attack(*guess2)
            print(f"{self.player2.name} attacks {guess2} - Result: {result2}")
            self.board1.display()

        # game over, declare the winner
        if self.board1.all_ships_sunk():
            print(f"{self.player2.name} wins!")
        else:
            print(f"{self.player1.name} wins!")

    def computer_make_guess(self, board):
        # generates a random guess for the computer player
        row = random.randint(1, board.size)
        col = random.randint(1, board.size)
        return row, col


if __name__ == "__main__":
    game = BattleshipsGame(player2_type="computer")
    game.setup_game()
    game.play()

    # some of the code for the structure and logic for
    # ship placement and player turns
    # in this section was derived from code found on:
    # https://pythondex.com/python-battleship-game
    # https://github.com/gbrough/battleship/blob/main/single_player.py with accompanying video: https://www.youtube.com/watch?app=desktop&v=tF1WRCrd_HQ
    # ascii text was generated using https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20