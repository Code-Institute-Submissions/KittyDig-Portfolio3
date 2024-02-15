from board import Board
from player import Player

class BattleshipsGame:
    def __init__(self):
        # initialises the game
        self.player1 = Player("Player 1")
        self.player2 = Player("Player 2")
        self.board1 = Board(size=10)
        self.board2 = Board(size=10)

    def setup_game(self):
        # sets up the game, including board size and placing the ships
        pass

    def play(self):
        # main game loop
        pass