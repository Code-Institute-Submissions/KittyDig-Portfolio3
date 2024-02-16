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
        while True:
            ''' generates random starting coordinates for the ship '''
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            ''' creates a list of ship coordinates based on the size and orientation '''
            ship_coordinates = []
            for i in range(ship_size):
                if orientation == 'H':
                    ship_coordinates.append((row, col + i))
                else:
                    ship_coordinates.append((row + i, col))

            ''' checks if the ship can be placed without overlapping with ships already on the board '''
            if all(0 <= r < self.size and 0 <= c < self.size and self.grid[r][c] == ' ' for r, c in ship_coordinates):
                self.ships.append(ship_coordinates)
                for r, c in ship_coordinates:
                    self.grid[r][c] = 'S'  # marks as part of the ship
                break

    def receive_attack(self, row, col):
        ''' processes an attack and update the board '''
        pass

    def all_ships_sunk(self):
        ''' checks if all ships are sunk '''
        pass