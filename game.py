# game.py

from board import Board
from player import Player
import random

class BattleshipsGame:
    def __init__(self):
        ''' initialises the game '''
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.board1 = Board(size=10)
        self.board2 = Board(size=10)

    def setup_game(self):
        ''' sets up the game, including board size and placing the ships '''
        for _ in range(2): # places 2 ships on the board
            self.board1.place_ship(2, random.choice(['H', 'V']))
            self.board2.place_ship(2, random.choice(['H', 'V']))

    def play(self):
        ''' main game loop '''
        while not (self.board1.all_ships_sunk() or self.board2.all_ships_sunk()):
            # player 1s turn
            guess1 = self.player1.make_guess(self.board2)
            result1 = self.board2.receive_attack(*guess1)
            print(f"{self.player1.name} attacks {guess1} - Result: {result1}")

            if self.board2.all_ships_sunk():
                break

            ''' game over, declare the winner '''
        if self.board1.all_ships_sunk():
            print(f"{self.player2.name} wins!")
        else:
            print(f"{self.player1.name} wins!")
            
if __name__ == "__main__":
    game = BattleshipsGame()
    game.setup_game()
    game.play()