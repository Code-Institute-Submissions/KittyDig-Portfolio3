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
        print("   " + " ".join(str(i) for i in range(1, self.size + 1)))
        for i in range(self.size):
            row = [str(i + 1)] + [str(cell) for cell in self.grid[i]]
            print(" ".join(row))
        print()

    def place_ship(self, ship_size, orientation):
        ''' places a ship on the board '''
        while True:
            # generates random starting coordinates for the ship
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)

            # creates a list of ship coordinates based on the size and orientation
            ship_coordinates = []
            for i in range(ship_size):
                if orientation == 'H':
                    ship_coordinates.append((row, col + i))
                else:
                    ship_coordinates.append((row + i, col))

            # checks if the ship can be placed without overlapping with ships already on the board
            if all(0 <= r < self.size and 0 <= c < self.size and self.grid[r][c] == ' ' for r, c in ship_coordinates):
                self.ships.append(ship_coordinates)
                for r, c in ship_coordinates:
                    self.grid[r][c] = ' '  # marks as part of the ship
                break

    def receive_attack(self, row, col):
        ''' processes an attack and update the board '''
        if not (1 <= row <= self.size) or not (1 <= col <= self.size):
            return "Invalid move"

        # adjusts the row and column to be 0-indexed
        row -= 1
        col -= 1

        if self.grid[row][col] == 'X':
            return "Already attacked this position"

        # checks if the attack hits a ship
        hit_ship = None
        for ship in self.ships:
            if (row, col) in ship:
                hit_ship = ship
                break

        if hit_ship:
            self.grid[row][col] = 'X'  # marks the attack as hit
            hit_ship.remove((row, col))  # removes the hit coordinate from the ship
            if not hit_ship:  # if the ship is sunk
                return "Sunk"
            return "Hit"

        self.grid[row][col] = 'O'  # marks the attack as miss
        return "Miss"

    def all_ships_sunk(self):
        ''' checks if all ships are sunk '''
        return all(not ship for ship in self.ships)


# some of the code for the structure and logic in this section was derived from code found on:
# https://codereview.stackexchange.com/questions/232013/a-simple-battleship-game
# https://pythondex.com/python-battleship-game
# https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605
# https://bigmonty12.github.io/battleship