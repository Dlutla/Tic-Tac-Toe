# ❌⭕ Tic-Tac-Toe (Console Edition)

A classic interactive Tic-Tac-Toe game running entirely in the command line interface. This project features enhanced terminal formatting using external packages to deliver a clean and structured gaming experience.

## Tech Stack & Dependencies
* **Language:** Python 3
* **Libraries:** Third-party packages specified in `requirements.txt` (used for advanced CLI formatting and table rendering).

## Key Features
* **Interactive CLI Board:** Dynamic 3x3 grid rendering in the terminal after every move:
  ```text
    X |   | O
   ---+---+---

      | X |  
   ---+---+---
    O |   | X
  ```
* **Smart Input Validation:** Prevents invalid moves, grid-overflows, or accidental overwriting of existing symbols.
* **Win/Draw Detection:** Built-in algorithmic engine checking rows, columns, and diagonals for winning combinations or tie scenarios.

---

## Installation & Setup

Follow these steps to clone the project, configure the virtual environment, install the required libraries, and launch the game:

### 1. Clone the repository
Clone the project using **SSH** (recommended) or HTTPS and navigate to the directory:
```bash
git clone https://github.com/Dlutla/Tic-Tac-Toe.git
cd Tic-Tac-Toe
```

### 2. Create and activate a virtual environment
* **On Windows:**
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```
* **On macOS/Linux:**
  ```bash
  python3 -m venv venv
  source venv/bin/activate
  ```

### 3. Install dependencies
Install all required libraries specified for the project execution:
```bash
pip install -r requirements.txt
```

### 4. Run the game
Launch the script directly using Python inside your active environment:
```bash
python main.py
```

---

## How to Play
1. The game is played on a grid that's 3 squares by 3 squares.
2. Players take turns putting their marks (`X` or `O`) in empty squares.
3. To make a move, enter the row and column coordinates when prompted in the console.
4. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
5. When all 9 squares are full, the game ends in a tie if no player has 3 marks.
