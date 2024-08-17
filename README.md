![Battleships](https://github.com/mushfique44/BattleShip_P3/blob/main/images/battleship_img.jpeg)

# Welcome To Battleships

This is a stratergy guessing board game. It is played between a user and a computer where each player gets their own 4x4 grid, in which they can place their 1x1 ships in. Each player will place 3 ships. Then the user will have a guess as to where the computers ship is located and then vice versa for the computer. Once either player guesses the correct position of all 3 ships they win the game.

The grid is displayed as shown below.

![Battleship Board](https://github.com/mushfique44/BattleShip_P3/blob/main/images/battleship_board.jpeg)

Here is the live version of this game

## How to play

- Aim of the game is take out all of the opponents ships

- Firstly the game will ask what grid size you will want to play (currently there is only one size)
- The game board will be displayed and will be empty
- - -
- Then the next section of the game will request the player to input where they will like to locate their ships on the grid
  - The ship sizes are 1x1 and the player will be able to place three ships
  - It will ask you to enter a column position between a-b (case sensitive) and a row position between 1-4
- Once all ship positions have been selected, the computer will locate its ships
- - - 
- The second section of the game is the guessing part
- Each turn the player will be ask to select a position to try and hit the opponents ship
  - The same as before, it will ask you to enter a column position between a-b (case sensitive) and a row position between 1-4
    - If the player hits a ship the board will be updated with a '@' symbol on that location
    - If the player misses the board will be update with a '#' on that location
- After each guess the computer will make its own guess and the same rules apply to the computer
- - -
- The game will end when either you or the computer hits all the ships
  - Game will end and the board will be reset back to empty

## Features

### Current Features

- Grid size selection 
  - can only select a 4x4 grid

![Grid selection]()

- Player custom ship selection
  - user can input each ship location
  - user can see its own ships locations for reference

![Player ship selection]()

- Computer random ship selection
  - three random ships are located for the computer
  - these ships are hidden to the user  

![comp hidden board]()

- Players guess locations of ship
  - user input guess
  - computer does random guess

![Player and comp guess]()

- Game board is displayed
  - Original empty board displayed
  - Displayed after ships have been positioned
  - Displayed after every turn of guess

![Empty board]()

![Board with ships]()

  - Display of all the symbols

![Board after a guess]()

- Input validation and error-checking
  - user has to pick 4x4 grid to start game
  - user cannot enter colm outside the range of letters a-d (case sensitive)
  - user cannot enter row outside the range of 1-4
  - user cannot guess the same location of a previous guess

![grid selection error]()

![colm a-d selection error]()

![row 1-4 selection error]()

![repeat guess error]()

#### All of these are being stored in a google sheet worksheet
- And code uses gspread features.
- So all input and output can be changed through google worksheets and also a saved feature can be implemented

### Future features

- Implement multiple grid sizes, i.e. 3x3/5x5/6x6 etc.
- Have the ship sizes be different, like the traditional way, such as a 4x1 ship and other sizes
- Have power up features, for example one larger radious hit per game for each player
- Have the ability to save and resume the game from where user left at 

## Data configure

- For this project, I used google sheets to model the board. This was done using the gspread functions and credentials to hide sensitive infomation
- The google sheets worksheet used has multiple sheets;
  - A sheet for the players board
  - A sheet for the hidden computer board
  - A sheet for the computer board with the ships
  - And other size grid sheets for future feature use
- The boards are created as a table style format, 
  - with A-D for the headings of the columns and 1-4 for the headings of the rows 
  - and '0' as ways to represent empty cells on the board and will be updated with the appropriate symbols when game is played

- gsread features are used in the code to access the google sheets, such as,
  - SHEET = GSPREAD_CLIENT.open('Battleship_P3')
  - SHEET.worksheet('blank4BY4')

- I used this way of modelling the board, so I can add features like saving and features like storing different game modes and easier way of referencing the board data

## Testing

- I have tested this project by doing the following;
  - using a PEP8 linter and getting rid of all the errors (one error on pep8 but doesnt error the code but breaks code when changed)
  - testing manually by putting in invalid inputs, such as, numbers instead of string and vise versa, picking inputs thats a repeated, etc.
  - tests have been done on local terminal as well as Heroku app terminal

### Bugs

#### Solved bugs
- computer was guessing multiple times per guess
  - the computer guess function was running in two different functions, so I had to remove one
- 

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
