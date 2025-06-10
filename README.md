# Tic Tac Toe

A simple command-line implementation of the classic Tic Tac Toe game built with the help of Amazon Q CLI.

## Description

This Tic Tac Toe game allows two players to take turns marking spaces on a 3x3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Features

- Interactive command-line interface
- Two-player gameplay
- Clear visual representation of the game board
- Win detection for horizontal, vertical, and diagonal matches
- Draw detection when the board is full
- Option to play multiple rounds

## Screenshots

<img src="screenshots/Screenshot%202025-06-01%20115616.png" alt="AWS Q CLI Screenshot" width="300"/>

<img src="screenshots/Screenshot%202025-06-01%20115716.png" alt="Code Screenshot" width="300"/>

<img src="screenshots/Screenshot%202025-06-01%20113949.png" alt="Gameplay Screenshot" width="300"/>


## 🎬 Demo Video

[Watch the Tic Tac Toe demo](https://youtu.be/uFgzl_i4thA?si=ZMIGTvMT09qkINYs)

## Installation

### Prerequisites

- Python 3.6 or higher

### Setup

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/tic-tac-toe.git
   cd tic-tac-toe
   ```

2. No additional dependencies are required as the game uses Python's standard library.

## How to Play

1. Run the game:
   ```
   python tic_tac_toe.py
   ```

2. Players take turns entering their moves by specifying the position on the board (1-9).
   The positions correspond to:
   ```
   1 | 2 | 3
   ---------
   4 | 5 | 6
   ---------
   7 | 8 | 9
   ```

3. The game will display the updated board after each move and announce the winner or a draw.

4. After a game ends, you'll be prompted to play again.

## Game Rules

- Player 1 uses 'X' and Player 2 uses 'O'
- Players take turns placing their marks on empty spaces
- The first player to get three marks in a row (horizontally, vertically, or diagonally) wins
- If all spaces are filled and no player has three in a row, the game is a draw

## Development

This project was developed with assistance from Amazon Q CLI, showcasing how AI can help in creating simple yet functional games.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Built with the assistance of Amazon Q CLI
- Inspired by the classic Tic Tac Toe game
