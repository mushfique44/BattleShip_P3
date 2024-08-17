![Battleships](https://github.com/mushfique44/BattleShip_P3/blob/main/images/battleship_img.jpeg)

Welcome,

To Battleships. This is a stratergy guessing board game. It is played between a user and a computer where each player gets their own 4x4 grid, in which they can place their 1x1 ships in. Each player will place 3 ships. Then the user will have a guess as to where the computers ship is located and then vice versa for the computer. Once either player guesses the correct position of all 3 ships they win the game.

The grid is displayed as shown below.

![Battleship Board](https://github.com/mushfique44/BattleShip_P3/blob/main/images/battleship_board.jpeg)

Here is the live version of this game

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

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
