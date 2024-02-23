# Battleships Game

![startScreen](images/startScreen.png)

## Table of Contents
1. [User Experience](#user-experience)
   - [User Stories](#user-stories)
2. [Installation](#installation)
3. [Design](#design)
   - [Colors](#colors)
   - [Design Inspiration](#design-inspiration)
4. [Features](#features)
   - [Gameplay](#gameplay)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
   - [User Testing](#user-testing)
7. [Bugs/Issues](#bugsissues)
   - [Fixed](#fixed)
   - [Unfixed](#unfixed)
8. [Deployment](#deployment)
9. [Credits](#credits)
   - [Design](#design)
   - [Python](#python)
10. [Acknowledgements](#acknowledgements)

## User Experience

### User Stories
- As a player, I want to understand the rules of the game.
- I want an interactive and engaging gaming experience.
- I want clear feedback on my moves.
- I want it to be clear which player is me and which is my opponent.

## Installation
- Clone the repository: `git clone https://github.com/KittyDig/Portfolio3`
- Navigate to the project directory: `cd Portfolio3`
- Run the game: `python run.py`

## Design

### Colors
- I used red and a blue / purple colour to differentiate between the two players boards.

![colours](images/colours.png)

### Design Inspiration
- The design was inspired by classic Battleships games with a focus on simplicity and clarity for the player.

## Features

### Gameplay
- Players take turns guessing coordinates to attack the opponent's fleet.
- 'X' represents a hit, 'O' represents a miss.
- The first player to sink all opponent's ships wins.

## Technologies Used
- Python

## Testing

### User Testing
- Gathered feedback from friends and family for testing the game to see if it was both enjoyable and easy to understand.
- Resolved an issue with board size, it was too big, based on user testing, the game was too large to be enjoyable for a quick game.

### Validator
- Used the website https://extendsclass.com/python-tester.html to validate my code, and it found no syntax errors.

![validator](images/validator.png)

## Bugs/Issues

### Fixed
- Resolved an issue with the board size, the game counted 0 as a viable section of the board, which was not correct. This was fixed by using row -= 1 col -= 1 to zero index the board.
- Resolved an issue with valid inputs, the game would crash whenever a user would either put a space or a non-numerical input as a turn. This was fixed by updating the player.py code to include a catch that gives the player an error if they try to input any value that is not on the board.

### Unfixed
- No known issues at the moment.

## Deployment
- The game can be run locally by following the installation steps:
- Clone the repository: `git clone https://github.com/KittyDig/Portfolio3`
- Navigate to the project directory: `cd Portfolio3`
- Run the game: `python run.py`

## Credits

### Design
- For the design, I used https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal to help me understand how to add colour to the game.
- The design is basic, with one board red for one player, and one board blue / purple for another player.

### Python
- Thanks to the open-source battleships projects that helped me to understand the main concepts of the game:
  - [GitHub - gbrough Python Battleship Game](https://github.com/gbrough/battleship/blob/main/single_player.py) with accompanying video: [YouTube](https://www.youtube.com/watch?app=desktop&v=tF1WRCrd_HQ)
  - [Codecademy Forum - cloud2236863496](https://discuss.codecademy.com/t/excellent-battleship-game-written-in-python/430605)
  - [Code Review Stack Exchange - Haliax](https://codereview.stackexchange.com/questions/232013/a-simple-battleship-game)
  - [Pythondex - Jarvis Silva](https://pythondex.com/python-battleship-game)
  - [Bigmonty12 - Austin Montgomery, Avery Smith](https://bigmonty12.github.io/battleship)
  - [Stack Overflow - joeld, Peter Mortensen](https://stackoverflow.com/questions/287871/how-do-i-print-colored-text-to-the-terminal)

## Acknowledgements
- Thank you to my mentor Spencer for all of the guidance and help with this project!