import tkinter as tk
from tkinter import messagebox
import random

def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    return any(all(board[i] == player for i in condition) for condition in win_conditions)

def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

def update_board(buttons, board):
    for i, button in enumerate(buttons):
        button.config(text=board[i], state=tk.DISABLED if board[i] in ['X', 'O'] else tk.NORMAL)

def player_move(i, buttons, board, current_player):
    if board[i] not in ['X', 'O']:
        board[i] = current_player
        update_board(buttons, board)
        
        if check_winner(board, current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game(buttons, board)
            return
        elif is_draw(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game(buttons, board)
            return
            
        # Switch to AI
        root.after(500, lambda: ai_move(buttons, board))

def ai_move(buttons, board):
    available_moves = [i for i, x in enumerate(board) if x not in ['X', 'O']]
    
    # Simple AI: first check for winning move, then blocking move, then random
    for player in ['O', 'X']:
        for move in available_moves:
            board_copy = board.copy()
            board_copy[move] = player
            if check_winner(board_copy, player):
                board[move] = 'O'
                update_board(buttons, board)
                if check_winner(board, 'O'):
                    messagebox.showinfo("Game Over", "Player O (AI) wins!")
                    reset_game(buttons, board)
                elif is_draw(board):
                    messagebox.showinfo("Game Over", "It's a draw!")
                    reset_game(buttons, board)
                return
    
    # If no winning or blocking move, choose random
    move = random.choice(available_moves)
    board[move] = 'O'
    update_board(buttons, board)
    
    if check_winner(board, 'O'):
        messagebox.showinfo("Game Over", "Player O (AI) wins!")
        reset_game(buttons, board)
    elif is_draw(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game(buttons, board)

def reset_game(buttons, board):
    for button in buttons:
        button.config(text="", state=tk.NORMAL)
    for i in range(9):
        board[i] = str(i + 1)

def main():
    global root
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    
    board = [str(i+1) for i in range(9)]
    buttons = []

    for i in range(9):
        button = tk.Button(root, text=board[i], width=10, height=3, font=('Arial', 20),
                          command=lambda i=i: player_move(i, buttons, board, 'X'))
        button.grid(row=i // 3, column=i % 3)
        buttons.append(button)
    
    reset_button = tk.Button(root, text="Restart Game", command=lambda: reset_game(buttons, board), 
                           font=('Arial', 12))
    reset_button.grid(row=3, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()