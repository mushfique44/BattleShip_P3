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
def random_ship():
    x = randint(1, 4)
    y = randint(1, 4)

    rand_cell = comp_frBYfr.update_cell(y +1, x + 1, "X")
    print(x, y)

def pick_ship_location():
    while True: 
        pick_colm = input("Pick a colomn between A-D: ")
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
            return False

    pick_row = input("Pick a row between 1-4: ")
    upt_cell = frBYfr.update_cell(pick_colm + 1, int(pick_row) + 1, "X")
    # pick = (pick_colm, int(pick_row))
    # print(pick)



def welcome_page():

    print("Welcome to the Battleships Game:")
    print("1: 4x4 grid")

    data_int = input("Please select 1 to start game: ")
    while data_int != "1":
        data_int = input("Please enter 1: ")
    else:
        print("Player 1 Board:")
        for x in range(5):
            print(frBYfr.row_values(x+1))
        print("Computers Board:")
        for x in range(5):
            print(blank_frBYfr.row_values(x+1))
        print("")

    pick_ship_location()
    random_ship()


    

welcome_page()


def comp_board_picks():
    return 0
    
def restart_game():
    restart_r = input("Type 'r' to Restart game: ")
    if restart_r == "r":
        for x in range(4):
            for i in range(4):
                restart_player = frBYfr.update_cell(x+2, i+2, "0")
                restart_comp = comp_frBYfr.update_cell(x+2, i+2, "0")
    else:
        


restart_game()

