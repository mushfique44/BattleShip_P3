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

GAME_ONE = frBYfr.get_all_values()
GAME_TWO = fiveBYfive.get_all_values()



def welcome_page():

    print("Welcome to the Battleships Game:")
    print("1: 4x4 grid")

    data_int = input("Please select 1 to start game: ")
    while data_int != "1":
        data_int = input("Please enter 1: ")
    else:
        print("Player 1 Board:")
        for x in range(4):
            print(frBYfr.row_values(x+1))
        print("Computers Board:")
        for x in range(4):
            print(comp_frBYfr.row_values(x+1))
        
        
    

welcome_page()

def comp_board_picks():
    return 0
    
def random_ship():
    return randint(0, 5)

    
