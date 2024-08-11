import gspread
from google.oauth2.service_account import Credentials
from random import randint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('Battleship_P3')

frBYfr = SHEET.worksheet('4BY4')
comp_frBYfr = SHEET.worksheet('comp4BY4')
fiveBYfive = SHEET.worksheet('5BY5')
comp_fiveBYfive = SHEET.worksheet('comp5BY5')
blank_frBYfr = SHEET.worksheet('blank4BY4')

GAME_ONE = frBYfr.get_all_values()
GAME_TWO = fiveBYfive.get_all_values()
def play_board():
    print("")
    print("-- Player 1 Board: --")
    for x in range(5):
        print(frBYfr.row_values(x+1))
    print("-- Computers Board: --")
    for x in range(5):
        print(blank_frBYfr.row_values(x+1))
    print("")
    print("('0' is empty / 'X' is Ship / '@' is hit Ship / '#' missed guess)\n")

def random_ship():
    x = randint(1, 4)
    y = randint(1, 4)

    rand_val = comp_frBYfr.cell(x, y).value
    if rand_val == "X":
        x = randint(1, 4)
        y = randint(1, 4)

        rand_val = comp_frBYfr.cell(x, y).value
    else:
        rand_cell = comp_frBYfr.update_cell(y +1, x + 1, "X")
    
    print(x, y)

def pick_ship_location():
    
    pick_colm = input("Pick a colomn between a-d (needs to be lowercase): ")
    while True: 
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
            pick_colm = input("Please pick between a-d (needs to be lowercase): ")

    pick_row = input("Pick a row between 1-4: ")
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

    val = frBYfr.cell(pick_row + 1, pick_colm + 1).value

    if val != "X":
        upt_cell = frBYfr.update_cell(int(pick_row) + 1, pick_colm + 1, "X")
    else:
        print("-- Location already picked. Please pick again --")
        pick_ship_location()
    #print(val)


def restart_game():
    restart_r = input("Type 'r' to Restart game: ")
    print("restarting...")
    print("please wait a minute to restart...")
    if restart_r == "r":
        for x in range(4):
            for i in range(4):
                restart_player = frBYfr.update_cell(x+2, i+2, "0")
                restart_comp = comp_frBYfr.update_cell(x+2, i+2, "0")
                restart_comp = blank_frBYfr.update_cell(x+2, i+2, "0")
                
    else:
        print("enter 'r' to Restart: ")

def comp_guess():
    x1 = randint(1, 4)
    y1 = randint(1, 4)

    rand_guess = frBYfr.cell(x1 + 1, y1 + 1).value

    if rand_guess == "0":
        print("Computer missed")
        upt_comp_miss = frBYfr.update_cell(x1 + 1, y1 + 1,'#')
    elif rand_guess == "#":
        comp_guess()
    elif rand_guess == "X":
        print("Computer has hit your ship")
        upt_comp_hit = frBYfr.update_cell(x1+1, y1+1, "@")


def play_game():

    print("-- Guess the locations of the computers ships --\n")
    play_board()
    game_winner()
    hit_colm = input("Pick a colomn between a-d (needs to be lowercase): ")
    while True: 
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
            hit_colm = input("Please pick between a-d (needs to be lowercase): ")

    hit_row = input("Pick a row between 1-4: ")
    while True:
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

    hit_val = comp_frBYfr.cell(hit_row + 1, hit_colm + 1).value

    if hit_val == "X":
        print("Congrats that was a hit")
        upt_hit_cell = comp_frBYfr.update_cell(int(hit_row) + 1, hit_colm + 1, "@")
        upt_hit__blank_cell = blank_frBYfr.update_cell(int(hit_row) + 1, hit_colm + 1, "@")
        print("You can guess again.\n")
        play_game()
    elif hit_val == "#":
        print("You have already guesses this location. Please guess again.\n")
        play_game()
    elif hit_val == "@":
        print("You have hit a ship in this location already. Please guess again.\n")
        play_game()
    else:
        print("That was a miss. Try again next turn!")
        upt_miss_cell = comp_frBYfr.update_cell(int(hit_row) + 1, hit_colm + 1, "#")
        upt_hit__blank_cell = blank_frBYfr.update_cell(int(hit_row) + 1, hit_colm + 1, "#")
        comp_guess()
        play_game()

def game_winner():
    
    
    win_count = comp_frBYfr.findall("@")
    win_comp_count = frBYfr.findall("@")

    if len(win_count) == 2:
        print("You have WON!")
        exit()

    if len(win_comp_count) == 2:
        print("You lose!")
        exit()

def start_game():

    #game_winner()
    print("~~ Welcome to the Battleships Game: ~~\n")
    print("1: 4x4 grid\n")

    data_int = input("Please select 1 to start game: ")
    while data_int != "1":
        data_int = input("Please enter 1: ")
    else:
        play_board()

    print("-- Please pick location of First ship --\n")
    pick_ship_location()

    print("-- Please pick location of SECOND ship --\n")
    pick_ship_location()

    print("-- Please pick location of THIRD ship --\n")
    pick_ship_location()

    random_ship()
    random_ship()
    random_ship()

    print("-- Ships are all ready! Time to take out the computers ships!! --\n")
    print("Are ready to continue? ")
    yes_no = input("enter 'y' for yes OR 'n' for no: ")
    print("")
    if yes_no == "y":
        play_game()
        comp_guess()
    elif yes_no == "n":
        restart_game()
    else:
        yes_no = input("Please enter 'y' or 'n': ")

    
    

start_game()


