import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        
        # Game variables
        self.board = [str(i+1) for i in range(9)]
        self.buttons = []
        self.game_mode = "AI"
        self.ai_difficulty = "medium"
        self.current_player = "X"
        
        self.setup_menu()
        self.create_board()
        self.root.mainloop()
    
    def setup_menu(self):
        """Setup game mode and difficulty selection"""
        self.show_mode_selection()
        
        if self.game_mode == "AI":
            self.show_difficulty_selection()
    
    def show_mode_selection(self):
        """Show game mode selection dialog"""
        top = tk.Toplevel(self.root)
        top.title("Select Mode")
        top.grab_set()
        
        tk.Label(top, text="Choose Game Mode:", font=('Arial', 12)).pack(pady=10)
        
        def set_mode(mode):
            self.game_mode = mode
            top.destroy()
        
        tk.Button(top, text="Player vs AI", command=lambda: set_mode("AI"), width=15).pack(pady=5)
        tk.Button(top, text="Player vs Player", command=lambda: set_mode("2P"), width=15).pack(pady=5)
        
        self.center_window(top)
        self.root.wait_window(top)
    
    def show_difficulty_selection(self):
        """Show AI difficulty selection dialog"""
        top = tk.Toplevel(self.root)
        top.title("Select Difficulty")
        top.grab_set()
        
        tk.Label(top, text="Choose AI Difficulty:", font=('Arial', 12)).pack(pady=10)
        
        def set_diff(diff):
            self.ai_difficulty = diff
            top.destroy()
        
        difficulties = [
            ("Easy (Random)", "easy"),
            ("Medium (Smart)", "medium"),
            ("Hard (Minimax)", "hard")
        ]
        
        for text, diff in difficulties:
            tk.Button(top, text=text, command=lambda d=diff: set_diff(d), width=15).pack(pady=5)
        
        self.center_window(top)
        self.root.wait_window(top)
    
    def create_board(self):
        """Create the game board UI"""
        for i in range(9):
            button = tk.Button(
                self.root, 
                text=self.board[i], 
                width=8, 
                height=3, 
                font=('Arial', 20, 'bold'),
                command=lambda i=i: self.handle_move(i),
                bg='#f0f0f0',
                activebackground='#e0e0e0'
            )
            button.grid(row=i // 3, column=i % 3, padx=5, pady=5)
            self.buttons.append(button)
        
        reset_button = tk.Button(
            self.root, 
            text="Restart Game", 
            command=self.reset_game,
            font=('Arial', 12),
            bg='#ff6666',
            fg='white',
            activebackground='#ff4444'
        )
        reset_button.grid(row=3, column=0, columnspan=3, pady=10, sticky="we")
        
        # Configure grid weights for better resizing
        for i in range(3):
            self.root.grid_rowconfigure(i, weight=1)
            self.root.grid_columnconfigure(i, weight=1)
    
    def handle_move(self, position):
        """Handle player move"""
        if self.board[position] not in ['X', 'O']:
            self.board[position] = self.current_player
            self.update_board()
            
            if self.check_winner(self.current_player):
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.reset_game()
                return
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
                return
            
            self.switch_player()
            
            if self.game_mode == "AI" and self.current_player == "O":
                self.root.after(500, self.ai_move)
    
    def switch_player(self):
        """Switch current player"""
        self.current_player = "O" if self.current_player == "X" else "X"
    
    def ai_move(self):
        """Handle AI move based on difficulty"""
        available_moves = [i for i, x in enumerate(self.board) if x not in ['X', 'O']]
        
        if not available_moves:
            return
            
        if self.ai_difficulty == "easy":
            move = random.choice(available_moves)
        elif self.ai_difficulty == "medium":
            move = self.find_medium_move(available_moves)
        else:  # hard
            move = self.minimax_ai(available_moves)
        
        self.board[move] = "O"
        self.update_board()
        
        if self.check_winner("O"):
            messagebox.showinfo("Game Over", "Player O (AI) wins!")
            self.reset_game()
        elif self.is_draw():
            messagebox.showinfo("Game Over", "It's a draw!")
            self.reset_game()
        else:
            self.switch_player()
    
    def find_medium_move(self, available_moves):
        """Medium AI: Win if possible, block if needed, otherwise random"""
        # Check for winning move
        for move in available_moves:
            self.board[move] = "O"
            if self.check_winner("O"):
                self.board[move] = str(move+1)
                return move
            self.board[move] = str(move+1)
        
        # Check for blocking move
        for move in available_moves:
            self.board[move] = "X"
            if self.check_winner("X"):
                self.board[move] = str(move+1)
                return move
            self.board[move] = str(move+1)
        
        # If center is available, take it
        if 4 in available_moves:
            return 4
            
        # Otherwise random
        return random.choice(available_moves)
    
    def minimax_ai(self, available_moves):
        """Hard AI using minimax algorithm"""
        best_score = -float('inf')
        best_move = None
        
        for move in available_moves:
            self.board[move] = "O"
            score = self.minimax(0, False)
            self.board[move] = str(move + 1)
            
            if score > best_score:
                best_score = score
                best_move = move
        
        return best_move
    
    def minimax(self, depth, is_maximizing):
        """Minimax algorithm implementation"""
        # Base cases
        if self.check_winner("O"):
            return 10 - depth
        elif self.check_winner("X"):
            return depth - 10
        elif self.is_draw():
            return 0
        
        available_moves = [i for i, x in enumerate(self.board) if x not in ['X', 'O']]
        
        if is_maximizing:  # AI's turn
            best_score = -float('inf')
            for move in available_moves:
                self.board[move] = "O"
                score = self.minimax(depth + 1, False)
                self.board[move] = str(move + 1)
                best_score = max(score, best_score)
            return best_score
        else:  # Player's turn
            best_score = float('inf')
            for move in available_moves:
                self.board[move] = "X"
                score = self.minimax(depth + 1, True)
                self.board[move] = str(move + 1)
                best_score = min(score, best_score)
            return best_score
    
    def update_board(self):
        """Update the board UI"""
        for i, button in enumerate(self.buttons):
            if self.board[i] in ['X', 'O']:
                button.config(
                    text=self.board[i],
                    state=tk.DISABLED,
                    fg='red' if self.board[i] == 'X' else 'blue',
                    disabledforeground='red' if self.board[i] == 'X' else 'blue'
                )
            else:
                button.config(text="", state=tk.NORMAL)
    
    def check_winner(self, player):
        """Check if player has won"""
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
            (0, 4, 8), (2, 4, 6)              # Diagonal
        ]
        return any(all(self.board[i] == player for i in condition) for condition in win_conditions)
    
    def is_draw(self):
        """Check if game is a draw"""
        return all(cell in ['X', 'O'] for cell in self.board)
    
    def reset_game(self):
        """Reset the game"""
        self.board = [str(i+1) for i in range(9)]
        self.current_player = "X"
        for i, button in enumerate(self.buttons):
            button.config(
                text="",
                state=tk.NORMAL,
                fg='black',
                disabledforeground='black'
            )
    
    def center_window(self, window):
        """Center a window on screen"""
        window.update_idletasks()
        width = window.winfo_width()
        height = window.winfo_height()
        x = (window.winfo_screenwidth() // 2) - (width // 2)
        y = (window.winfo_screenheight() // 2) - (height // 2)
        window.geometry(f'{width}x{height}+{x}+{y}')

if __name__ == "__main__":
    TicTacToe()