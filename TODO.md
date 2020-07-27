## The work needed to get a working tik-tak-toe
These are the different steps that I took to get the work done, so they are not the exact steps as our game will have different functionalities.
1. Get the user input of the players through `sys`.
2. Create the board array.
3. Define the first show board function to be displayed at the start of the game.
4. `play_game()` function to define the play game functionality.
  1. Checking the number of turns during the game.
  2. Have the turn variable for the two players.
  3. Check if the player wants to quit the game.
  4. Check if the the place is taken.
5. `print_board()` function to update the board during the game.
6. `check_win()` function to decide if any of the players won the game.
7. `restart()` function to allow the users to restart the game after the turns are over or if one of the players won the game.