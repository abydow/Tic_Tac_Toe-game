class tictactoe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  
        self.current_player = 'X'

    def display_board(self):
        print("\n   |   |   ")
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("___|___|___")
        print("   |   |   ")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")
        print("   |   |   \n")  

    def display_positions(self):
        print("\n   |   |   ")
        print(" 1 | 2 | 3 ")
        print("___|___|___")       
        print("   |   |   ")
        print(" 4 | 5 | 6 ")        
        print("___|___|___")
        print("   |   |   ")
        print(" 7 | 8 | 9 ")
        print("   |   |   \n")

    def make_move(self, position):
        if self.board[position - 1] == ' ':
            self.board[position - 1] = self.current_player
            return True
        return False
    
    def check_winner(self):
        win_patterns = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)  
        ]
        for pattern in win_patterns:
            if self.board[pattern[0]] == self.board[pattern[1]] == self.board[pattern[2]] != ' ':
                return self.board[pattern[0]]
        return None
    
    def is_board_full(self):
        return ' ' not in self.board
    
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'

    def play(self):
        print("="*30)
        print("Welcome to Tic-Tac-Toe!")
        print("="*30)

        while True:
            self.display_positions()
            self.display_board()

            try:
                position = int(input(f"Player {self.current_player}, enter your move (1-9): "))
                if position < 1 or position > 9:
                    print("Invalid position. Please choose a number between 1 and 9.")
                    continue
                if not self.make_move(position):
                    print("Position already taken. Try again.")
                    continue
                winner = self.check_winner()
                if winner:
                    self.display_board()
                    print(f"Player {winner} wins!")
                    break
                if self.is_board_full():
                    self.display_board()
                    print("It's a draw!")
                    break
                self.switch_player()

            except ValueError:
                print("Invalid input. Please enter a number between 1 and 9.")
            except KeyboardInterrupt:
                print("\nThanks for playing!")
                break
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again == 'yes' or play_again == 'y':
            self.reset_game()
            self.play()
        if play_again == 'no' or play_again == 'n':
            print("Thanks for playing!")

        else:
            print("Invalid input. Exiting the game.")
        
if __name__ == "__main__":
    game = tictactoe()
    game.play()
    
