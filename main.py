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

# Add game mode selection at startup
def choose_mode():
    global game_mode
    top = tk.Toplevel(root)
    top.title("Select Mode")
    top.grab_set()  # Tambahkan ini supaya fokus

    tk.Label(top, text="Choose Game Mode:", font=('Arial', 12)).pack(pady=10)
    
    def set_mode(mode):
        global game_mode
        game_mode = mode
        top.destroy()
    
    tk.Button(top, text="Player vs AI", command=lambda: set_mode("AI"), width=15).pack(pady=5)
    tk.Button(top, text="Player vs Player", command=lambda: set_mode("2P"), width=15).pack(pady=5)

# Modify player_move function
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
            
        # Switch player (no AI in 2P mode)
        next_player = 'O' if current_player == 'X' else 'X'
        if game_mode == "AI" and next_player == "O":
            root.after(500, lambda: ai_move(buttons, board))

# Add difficulty selection
def choose_difficulty():
    global ai_difficulty
    top = tk.Toplevel(root)
    top.title("Select Difficulty")
    
    tk.Label(top, text="Choose AI Difficulty:", font=('Arial', 12)).pack(pady=10)
    
    def set_diff(diff):
        global ai_difficulty
        ai_difficulty = diff
        top.destroy()
    
    tk.Button(top, text="Easy (Random)", command=lambda: set_diff("easy"), width=15).pack(pady=5)
    tk.Button(top, text="Medium (Smart)", command=lambda: set_diff("medium"), width=15).pack(pady=5)
    tk.Button(top, text="Hard (Minimax)", command=lambda: set_diff("hard"), width=15).pack(pady=5)

# Enhanced AI function
def ai_move(buttons, board):
    available_moves = [i for i, x in enumerate(board) if x not in ['X', 'O']]
    
    if ai_difficulty == "easy":
        move = random.choice(available_moves)
    
    elif ai_difficulty == "medium":
        # Medium AI: Wins if possible, blocks if needed, otherwise random
        for player in ['O', 'X']:
            for move in available_moves:
                board_copy = board.copy()
                board_copy[move] = player
                if check_winner(board_copy, player):
                    break
            else:
                continue
            break
        else:
            move = random.choice(available_moves)
    
    elif ai_difficulty == "hard":
        # Minimax algorithm placeholder
        move = minimax_ai(board, available_moves)
    
    board[move] = 'O'
    update_board(buttons, board)
    
    if check_winner(board, 'O'):
        messagebox.showinfo("Game Over", "Player O wins!")
    elif is_draw(board):
        messagebox.showinfo("Game Over", "It's a draw!")

def minimax_ai(board, available_moves):
    # Minimax algorithm implementation
    best_score = -float('inf')
    best_move = None
    
    for move in available_moves:
        board[move] = 'O'  # AI makes a move
        score = minimax(board, 0, False)
        board[move] = str(move + 1)  # Undo move
        
        if score > best_score:
            best_score = score
            best_move = move
    
    return best_move

def minimax(board, depth, is_maximizing):
    # Base cases
    if check_winner(board, 'O'):
        return 10 - depth
    elif check_winner(board, 'X'):
        return depth - 10
    elif is_draw(board):
        return 0
    
    available_moves = [i for i, x in enumerate(board) if x not in ['X', 'O']]
    
    if is_maximizing:  # AI's turn
        best_score = -float('inf')
        for move in available_moves:
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = str(move + 1)
            best_score = max(score, best_score)
        return best_score
    else:  # Player's turn
        best_score = float('inf')
        for move in available_moves:
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = str(move + 1)
            best_score = min(score, best_score)
        return best_score
    
def main():
    global root, game_mode, ai_difficulty
    root = tk.Tk()
    root.title("Tic-Tac-Toe")

    # Default settings
    game_mode = "AI"
    ai_difficulty = "medium"

    # Tampilkan pilihan mode
    choose_mode()
    root.wait_window(root.winfo_children()[-1])  # Tunggu sampai pilih mode

    if game_mode == "AI":
        choose_difficulty()
        root.wait_window(root.winfo_children()[-1])  # Tunggu sampai pilih difficulty
    
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