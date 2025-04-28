# Tic-Tac-Toe Game 🎮 (GUI Version)

![Tic-Tac-Toe Gameplay](https://via.placeholder.com/600x400?text=Tic-Tac-Toe+Screenshot)  
_A modern, flexible, and fun implementation of the classic Tic-Tac-Toe with multiple modes and AI difficulty!_

## Table of Contents

- [Features](#features-)
- [How to Play](#how-to-play-)
- [Installation](#installation-)
- [Running the Game](#running-the-game-)
- [Technical Details](#technical-details-)
- [Future Improvements](#future-improvements-)
- [Contributing](#contributing-)

## Features ✨

🎯 **Core Gameplay**

- Player vs Player mode
- Player vs Computer (AI) mode
- Classic 3x3 grid interface
- Automatic win or draw detection
- Game restart anytime

🤖 **AI Opponent**

- Easy: Random moves
- Medium: Smart moves (attempts to win or block player)
- Hard: Perfect play using Minimax algorithm

🖥️ **User Experience**

- Clean and responsive Tkinter GUI
- Mode and difficulty selection before starting
- Instant visual feedback
- Simple and intuitive controls

## How to Play 🎮

1. **Launch the Game**

   - Launch the application to begin
   - Choose between Player vs Player or Player vs AI

2. **(If Player vs AI) Choose Difficulty**

   - Easy: Random moves
   - Medium: Smart moves
   - Hard: Minimax, unbeatable

3. **Making Moves**

   - Player X always moves first
   - Click on an empty cell to place your mark
   - If playing against AI, the AI responds automatically

4. **Winning**

   - Get three of your marks in a row (horizontally, vertically, or diagonally)
   - The game automatically detects a win or draw and shows a message

5. **Restarting**

   - Click the "Restart Game" button to start a new match anytime

## Installation ⚙️

### Prerequisites

- Python 3.6 or higher
- Tkinter (usually included with Python)

### Setup

```bash
# Clone the repository (if applicable)
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
```

### Running the game

```bash
python tictactoe.py
```

## Technical Details 🔧

- Language: Python 3
- Library: Tkinter for GUI
- AI: Random, Smart Blocking, and Minimax algorithm
- Gameplay Logic: Win detection, draw detection, dynamic board update
- User Flow: Mode selection → Difficulty selection (if needed) → Gameplay

## Future Improvements 🚀

- Add sound effects for moves and win notifications
- Add score tracking (number of wins/draws)
- Add player name input
- Create an online multiplayer version

## Contributing 🤝

Pull requests are welcome!
For major changes, please open an issue first to discuss what you would like to change.
