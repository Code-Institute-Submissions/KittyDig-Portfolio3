# game.py

from board import Board
from player import Player
import random

class BattleshipsGame:
    def __init__(self):
        ''' initialises the game '''
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.board1 = Board(size=5)
        self.board2 = Board(size=5)

    def setup_game(self):
        ''' sets up the game, including board size and placing the ships '''
        for _ in range(2): # places 2 ships on the board
            self.board1.place_ship(2, random.choice(['H', 'V']))
            self.board2.place_ship(2, random.choice(['H', 'V']))

    def play(self):
        ''' main game loop '''
        print("Welcome to Battleships!")
        print("Rules:")
        print("1. You have a fleet of ships on a 5x5 grid")
        print("2. Ships are placed randomly either horizontally or vertically")
        print("3. Each player takes turns guessing the coordinates to attack")
        print("4. 'X' represents a hit, 'O' represents a miss")
        print("5. The first player to sink all the opponent's ships wins.")
        print()
        
        while not (self.board1.all_ships_sunk() or self.board2.all_ships_sunk()):
            # player 1s turn
            guess1 = self.player1.make_guess(self.board2)
            result1 = self.board2.receive_attack(*guess1)
            print(f"{self.player1.name} attacks {guess1} - Result: {result1}")
            self.board2.display()

            if self.board2.all_ships_sunk():
                break

            # player 2s turn
            guess2 = self.player2.make_guess(self.board1)
            result2 = self.board1.receive_attack(*guess2)
            print(f"{self.player2.name} attacks {guess2} - Result: {result2}")
            self.board1.display()

            # game over, declare the winner
        if self.board1.all_ships_sunk():
            print(f"{self.player2.name} wins!")
        else:
            print(f"{self.player1.name} wins!")
            
if __name__ == "__main__":
    game = BattleshipsGame()
    game.setup_game()
    game.play()

    # some of the code for the structure and logic in this section was derived from code found on:
    # https://pythondex.com/python-battleship-game
    # https://github.com/gbrough/battleship/blob/main/single_player.py with accompanying video: https://www.youtube.com/watch?app=desktop&v=tF1WRCrd_HQ