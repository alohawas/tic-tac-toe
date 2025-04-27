import tkinter as tk
from tkinter import messagebox
import random

# Fungsi untuk memeriksa apakah pemain menang
def check_winner(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

# Fungsi untuk memeriksa apakah permainan seri
def is_draw(board):
    return all(cell in ['X', 'O'] for cell in board)

# Fungsi untuk mengupdate tampilan
def update_board(buttons, board):
    for i, button in enumerate(buttons):
        button.config(text=board[i], state=tk.DISABLED if board[i] in ['X', 'O'] else tk.NORMAL)

# Fungsi untuk menangani klik tombol pemain
def player_move(i, buttons, board, current_player):
    if board[i] not in ['X', 'O']:
        board[i] = current_player
        update_board(buttons, board)
        if check_winner(board, current_player):
            messagebox.showinfo("Game Over", f"Player {current_player} wins!")
            reset_game(buttons, board)
        elif is_draw(board):
            messagebox.showinfo("Game Over", "It's a draw!")
            reset_game(buttons, board)
        else:
            current_player.set('O' if current_player.get() == 'X' else 'X')
            if current_player.get() == 'O':  # AI turn
                ai_move(buttons, board)

# Fungsi untuk gerakan AI (komputer)
def ai_move(buttons, board):
    available_moves = [i for i, x in enumerate(board) if x not in ['X', 'O']]
    move = random.choice(available_moves)
    board[move] = 'O'
    update_board(buttons, board)
    if check_winner(board, 'O'):
        messagebox.showinfo("Game Over", "Player O (AI) wins!")
        reset_game(buttons, board)
    elif is_draw(board):
        messagebox.showinfo("Game Over", "It's a draw!")
        reset_game(buttons, board)
    else:
        current_player.set('X')

# Fungsi untuk mereset permainan
def reset_game(buttons, board):
    for button in buttons:
        button.config(text="", state=tk.NORMAL)
    for i in range(9):
        board[i] = str(i + 1)
    current_player.set('X')

# Membuat GUI menggunakan Tkinter
def main():
    root = tk.Tk()
    root.title("Tic-Tac-Toe")
    
    current_player = tk.StringVar(value='X')
    
    board = [str(i+1) for i in range(9)]  # Papan permainan
    buttons = []

    for i in range(9):
        button = tk.Button(root, text=board[i], width=10, height=3, font=('Arial', 20),
                           command=lambda i=i: player_move(i, buttons, board, current_player.get()))
        button.grid(row=i // 3, column=i % 3)
        buttons.append(button)
    
    # Tombol reset
    reset_button = tk.Button(root, text="Restart Game", command=lambda: reset_game(buttons, board), font=('Arial', 12))
    reset_button.grid(row=3, column=0, columnspan=3, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
