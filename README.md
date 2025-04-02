# Tic-Tac-Toe

## Description
This is a simple Tic-Tac-Toe game implemented in Python. The player competes against an AI opponent using the Minimax algorithm, which ensures an optimal strategy.

## Technologies Used
- Python 3

## How to Run

1. Make sure you have Python 3 installed on your computer.
2. Clone this repository:
   ```sh
   git clone https://github.com/BenitoTM/Jogo_da_velha.git
   ```
3. Navigate to the project directory:
   ```sh
   cd Jogo_da_velha
   ```
4. Run the main script:
   ```sh
   python jogo_da_velha.py
   ```

## How to Play
- The player plays against an AI opponent.
- The board is a 3x3 grid.
- The player takes turns against the AI, selecting an available position to place their symbol ('X' or 'O').
- The AI uses the Minimax algorithm to make optimal moves.
- The game ends when a player completes a row, column, or diagonal with their symbol, or when all positions are filled (resulting in a draw).

## Example Gameplay
```
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 

Player (X), choose a number: 5

 1 | 2 | 3 
-----------
 4 | X | 6 
-----------
 7 | 8 | 9 

AI (O) chooses position: 1

 O | 2 | 3 
-----------
 4 | X | 6 
-----------
 7 | 8 | 9 
```
