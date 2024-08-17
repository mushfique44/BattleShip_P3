# note: all time.sleep() functions are implemented to add a delay so that the
# google sheet
# quota limits are not hit and code doesnt break

# Importing time and gspread to be able access the features it provides
# importing classes creds and radiant from its funtions library
import time
import gspread
from google.oauth2.service_account import Credentials
from random import randint

# google IAM configurations
# configuration specifies what the user has access to
# The scope lists the APIs that the  program should access in order to run.
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

# constant variables to access creds file with the scope access
# and gspread authorise method, and pass scoped creds
# and sheets variable to access the Battleship_P3 spreadsheet from
# the google sheets
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Battleship_P3')

# Setting variables that will read the google sheets tabs
frBYfr = SHEET.worksheet('4BY4')
comp_frBYfr = SHEET.worksheet('comp4BY4')
fiveBYfive = SHEET.worksheet('5BY5')
comp_fiveBYfive = SHEET.worksheet('comp5BY5')
blank_frBYfr = SHEET.worksheet('blank4BY4')

# variables that determine a 4x4 board or 5x5
GAME_ONE = frBYfr.get_all_values()
GAME_TWO = fiveBYfive.get_all_values()


# setting up a function that will print the battleship board
def play_board():

    print("")
    print("-- Player 1 Board: --")
    # for a range of to 1-5 print all the values of each row 1-5
    # from 4x4 tab
    for x in range(5):
        print(frBYfr.row_values(x+1))
    print("-- Computers Board: --")
    # for a range of to 1-5 print all the values of each row 1-5
    # from blank 4x4 computer tab
    for x in range(5):
        print(blank_frBYfr.row_values(x+1))
    print("")
    # battleship board symbols
    print(("('0' is empty / 'X' is Ship / '@'"
           "is hit Ship /'#' missed guess)\n"))


# function that does a random pick to position a ship for computer
def random_ship():

    # set x, y a random number between 1-4
    x = randint(1, 4)
    y = randint(1, 4)

    # set variable to equal the value of the cell postion of the
    # two random numbers as row and colm
    rand_val = comp_frBYfr.cell(y+1, x+1).value

    # if the value of the cell is 'X' then run the randomiser of x and y again
    # otherwise update that cell so it equals the value 'X'
    if rand_val == "X":
        random_ship()
    else:
        rand_cell = comp_frBYfr.update_cell(y + 1, x + 1, "X")


# function for player to pick where to place their ships
def pick_ship_location():

    # pick the colomn by choosing a-d
    pick_colm = input("Pick a colomn between a-d (needs to be lowercase): ")
    # validation so that the pick is between a-d else pick again
    while True:
        # converting the leter pick into a number to use later in the code
        if pick_colm == "a":
            pick_colm = 1
            break
        elif pick_colm == "b":
            pick_colm = 2
            break
        elif pick_colm == "c":
            pick_colm = 3
            break
        elif pick_colm == "d":
            pick_colm = 4
            break
        else:
            pick_colm = input(("Please pick between a-d"
                               "(needs to be lowercase): "))

    # pick the row between 1-4
    pick_row = input("Pick a row between 1-4: ")
    print("")
    # validation to make sure pick is between 1-4 else pick again
    while True:
        if pick_row == "1":
            pick_row = 1
            break
        elif pick_row == "2":
            pick_row = 2
            break
        elif pick_row == "3":
            pick_row = 3
            break
        elif pick_row == "4":
            pick_row = 4
            break
        else:
            pick_row = input("Please pick a number between 1-4: ")
            print("")

    # variable equals the value of the cell of the row colm
    # position of the pick
    val = frBYfr.cell(pick_row + 1, pick_colm + 1).value

    # if the variable doesnt equal 'X' then update the value of cell to 'X'
    # else make the player pick again
    if val != "X":
        upt_cell = frBYfr.update_cell(int(pick_row) + 1, pick_colm + 1, "X")
    else:
        print("-- Location already picked. Please pick again --\n")
        pick_ship_location()


# function to restart the game and reset the board
def restart_game():

    print("restarting board...")
    print("please wait a minute to restart...\n")

    # set x and i, rows and colm, to equal 1-4 consecutivly and update the
    # cells for each i and x postion cell
    for x in range(4):
        for i in range(4):
            restart_player = frBYfr.update_cell(x+2, i+2, "0")
            restart_comp = comp_frBYfr.update_cell(x+2, i+2, "0")
            restart_comp = blank_frBYfr.update_cell(x+2, i+2, "0")

    # exit program
    print("Game End!")
    exit()


# function for computer the guess randomly
def comp_guess():

    # set variables to randomly equal value 1-4
    x1 = randint(1, 4)
    y1 = randint(1, 4)

    # variable to equal value of cell of the random row colm
    rand_guess = frBYfr.cell(x1 + 1, y1 + 1).value

    # if the random guess cell value equal '0' then display 'computer missed'
    # and update the cell of the player 4x4 board to display that it has
    # been missed hit
    if rand_guess == "0":
        print("Computer missed\n")
        upt_comp_miss = frBYfr.update_cell(x1 + 1, y1 + 1, "#")
    # if the guess value is '#' that means this has already been guessed
    # so the function is run again so it can guess again
    elif rand_guess == "#":
        comp_guess()
    # if the guess value is '@' that means this has already been guessed
    # so the function is run again so it can guess again
    elif rand_guess == "@":
        comp_guess()
    # if the guess value equals "X" then that means the computer
    # has guessed correctly
    # and will update with '@' to show it has been hit
    elif rand_guess == "X":
        print("Computer has hit your ship\n")
        upt_comp_hit = frBYfr.update_cell(x1+1, y1+1, "@")


# function to have the player to start guessing
def play_game():

    print("-- Guess the locations of the computers ships --\n")

    # variable equals value of players input of a-d for colm
    hit_colm = input("Pick a colomn between a-d (needs to be lowercase): ")
    # validation so player input is between a-d or player inputs again
    while True:
        # convert all the letters to a number to use later in code
        if hit_colm == "a":
            hit_colm = 1
            break
        elif hit_colm == "b":
            hit_colm = 2
            break
        elif hit_colm == "c":
            hit_colm = 3
            break
        elif hit_colm == "d":
            hit_colm = 4
            break
        else:
            hit_colm = input(("Please pick between a-d"
                              " (needs to be lowercase): "))

    # same thing for row selection, player input between 1-4
    hit_row = input("Pick a row between 1-4: ")
    print("")
    # validation again so input is between 1-4
    while True:
        # convert the input to a number
        if hit_row == "1":
            hit_row = 1
            break
        elif hit_row == "2":
            hit_row = 2
            break
        elif hit_row == "3":
            hit_row = 3
            break
        elif hit_row == "4":
            hit_row = 4
            break
        else:
            hit_row = input("Please pick a number between 1-4: ")
            print("")

    # variable equal the cell value of the player row and colm input
    hit_val = comp_frBYfr.cell(hit_row + 1, hit_colm + 1).value

    # checking if variable value is 'X'
    # if so then the player has hit a ship and the blank
    # comp board and hidden comp board
    # is updated with '@' value to show a ship was hit
    if hit_val == "X":
        print("Congrats that was a hit\n")
        upt_hit_cell = comp_frBYfr.update_cell(int(hit_row) + 1,
                                               hit_colm + 1, "@")
        upt_hit__blank_cell = blank_frBYfr.update_cell(int(hit_row) + 1,
                                                       hit_colm + 1, "@")
        # then the computer guess function is run after player guess
        comp_guess()
    # if variable value is '#' then player guess function is run again as this
    # is a location that has already been guessed
    elif hit_val == "#":
        print(("You have already guesses this location."
               "Please guess again.\n"))
        play_game()
    # if value is '@' then player guesses again as this is a location
    # that has been guessed and a ship was hit
    elif hit_val == "@":
        print(("You have hit a ship in this location already."
               " Please guess again.\n"))
        play_game()
    # else anything else means the guess was a miss and the location is
    # updated to '#' so it is shown that it has been guessed on both boards
    else:
        print("That was a miss. Try again next turn!\n")
        upt_miss_cell = comp_frBYfr.update_cell(int(hit_row) + 1,
                                                hit_colm + 1, "#")
        upt_hit__blank_cell = blank_frBYfr.update_cell(int(hit_row) + 1,
                                                       hit_colm + 1, "#")
        comp_guess()


# function to determine if player or computer has won
def game_winner():

    # list out all of the '@' values are on both hidden comp and player voards
    win_count = comp_frBYfr.findall("@")
    win_comp_count = frBYfr.findall("@")

    # if length of the list of '@' on the hidden comp board is
    # equal to 3 then the player wins and the restart function is run
    # to end game
    if len(win_count) == 3:
        print("You have WON!\n")
        restart_game()
    # if length of the list of '@' on the player board is
    # equal to 3 then the computer wins and the restart function is run to
    # end game
    if len(win_comp_count) == 3:
        print("You lose!\n")
        restart_game()


# this function is to start the program and acts as a home page
def start_game():

    # grid size selection choice (currently only one option)
    print("")
    print("~~ Welcome to the Battleships Game: ~~\n")
    print("1: 4x4 grid\n")

    # read player input and check if it is value 1 or repeat until
    # 1 is selected
    data_int = input("Please select 1 to start game: ")
    while data_int != "1":
        data_int = input("Please enter 1: ")
    else:
        # display boards
        time.sleep(5)
        play_board()

    # run players first ship pick  by running pick ship function
    print("-- Please pick location of First ship --\n")
    pick_ship_location()
    time.sleep(2)

    # run players second ship pick  by running pick ship function
    print("-- Please pick location of SECOND ship --\n")
    pick_ship_location()
    time.sleep(2)

    # run players third ship pick  by running pick ship function
    print("-- Please pick location of THIRD ship --\n")
    pick_ship_location()
    time.sleep(2)

    # run the comp random ship function three time to have comp pick
    # 3 ship locations
    random_ship()
    random_ship()
    random_ship()
    time.sleep(2)
    # ask player if they want to continue or if they want to restart
    print(("-- Ships are all ready! Time to take out the computers"
           " ships!! --\n"))
    print("Are ready to continue? ")
    yes_no = input("enter 'y' to continue or anything else to restart: ")
    print("")
    # input if not 'y' then restart else start the guesses
    if yes_no != "y":
        restart_game()
    else:
        # while the game winner function is empty/ no winner is determined yet
        # then display the boards and run the play game funtion
        while game_winner() == None:
            print("Loading Board... \n")
            time.sleep(5)
            play_board()
            time.sleep(5)
            play_game()
        # else when a game winner is determined then run the game winner
        # function
        # which will display winner and end game
        else:
            time.sleep(5)
            play_board()
            time.sleep(5)
            game_winner()


# start program with start game function
start_game()
