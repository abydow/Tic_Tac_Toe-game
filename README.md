# Tic_Tac_Toe-game

A Python implementation of the classic Tic-Tac-Toe game played in the terminal. It supports two human players alternating turns, with board display, input validation, win/draw detection, and replay capability.

---

## Overview

This project simulates the classic Tic-Tac-Toe game where two players take turns marking spaces in a 3×3 grid. The goal is to place three respective marks (X or O) in a horizontal, vertical, or diagonal row before the opponent.

---

## Code Structure and Logic

The whole game logic is encapsulated in a single class named `tictactoe`.

### Class: `tictactoe`

This class models the game board, player turns, and the full game flow.

#### Attributes:

- `board` (list of str): Represents the 3x3 game board as a list of 9 elements. Each element is `' '` (empty), `'X'`, or `'O'`.
- `current_player` (str): Tracks whose turn it is, either `'X'` or `'O'`. The game starts with `'X'`.

#### Methods:

- `__init__(self)`  
  Initializes the game with an empty board and sets the starting player to `'X'`.

- `display_board(self)`  
  Prints the current state of the board in a user-friendly 3x3 grid format showing player marks.

- `display_positions(self)`  
  Prints the board positions (1 to 9) mapped to indexes, aiding players in choosing their moves.

- `make_move(self, position)`  
  Attempts to place the current player's mark at the given 1-based `position` (1-9).  
  Returns `True` if the move is successful (empty spot), else `False`.

- `check_winner(self)`  
  Checks all possible winning patterns (rows, columns, diagonals).  
  Returns the mark `'X'` or `'O'` if a winner is found, otherwise `None`.

- `is_board_full(self)`  
  Returns `True` if there are no empty spaces left on the board (a draw), else `False`.

- `switch_player(self)`  
  Switches the current player from `'X'` to `'O'` or vice versa.

- `reset_game(self)`  
  Clears the board and resets the current player to `'X'`, preparing for a new game.

- `play(self)`  
  The main game loop:
  - Welcomes players and displays the board and position guide.
  - Prompts current player for a move.
  - Validates input and move legality.
  - Updates the board and checks for a win or draw.
  - Switches players or ends the game accordingly.
  - Offers the option to replay after a game ends.

---

## How To Run

1. Save the script as `tic_tac_toe.py`.
2. Run the script from the terminal or command prompt:

3. Follow the on-screen prompts to enter your moves (1-9) and play against another human player.

---

## Gameplay Summary

- The game board has 9 positions numbered 1 to 9.
- Players take turns entering the position number where they want to place their mark ('X' or 'O').
- The first player to align three marks in a row, column, or diagonal wins.
- If all 9 positions are filled with no winner, the game ends in a draw.
- After game conclusion, players can choose to play again or exit.

---

## Additional Notes

- Input validation ensures players cannot choose occupied positions or enter invalid numbers.
- The board is printed after every move to visualize changes.
- Friendly prompts and messages guide players throughout the game.
- Interrupting the program (Ctrl+C) exits gracefully with a message.

---

Feel free to clone, modify, and extend this simple Tic-Tac-Toe implementation!

---

## License

This project is open source and available under the MIT License.

---



