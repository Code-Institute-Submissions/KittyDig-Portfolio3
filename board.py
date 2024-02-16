# board.py
import random

class Board:
    def __init__(self, size):
        ''' initialise the game board '''
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]  # empty grid
        self.ships = []  # list to store ship coordinates

    def display(self, show_ships=False):
        ''' displays the board '''
        pass

    def place_ship(self, ship, row, col, orientation):
        ''' places a ship on the board '''
        pass

    def receive_attack(self, row, col):
        ''' processes an attack and update the board '''
        pass

    def all_ships_sunk(self):
        ''' checks if all ships are sunk '''
        pass