import gspread
from google.oauth2.service_account import Credentials

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

    print("Welcome! Please chose board size by entering:")
    print("1: 4by4 grid")
    print("2: 5by5 grid")

    data_int = input("Chose between 1 or 2: ")
    if data_int == "1":
        print(frBYfr.row_values(1))
        print(frBYfr.row_values(2))
        print(frBYfr.row_values(3))
        print(frBYfr.row_values(4))                        
    else:
        print(fiveBYfive.row_values(1))
        print(fiveBYfive.row_values(2))
        print(fiveBYfive.row_values(3))
        print(fiveBYfive.row_values(4))
        print(fiveBYfive.row_values(5))

welcome_page()

def comp_board_picks():
    print("")
