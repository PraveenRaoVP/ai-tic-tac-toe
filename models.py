import random

class Player:
    def __init__(self, name, symbol, is_ai=False):
        self.name = name
        self.symbol = symbol
        self.is_ai = is_ai
    
    def get_opponent_symbol(self):
        return 'O' if self.symbol == 'X' else 'X'

class Game:
    def __init__(self, player1, player2):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.players = [player1, player2]
        self.current_player = 0  # Index of the current player

    def make_move(self, row, col):
        if self.board[row][col] == '':
            self.board[row][col] = self.players[self.current_player].symbol
            self.current_player = (self.current_player + 1) % 2
        else:
            raise ValueError('Invalid move')
    
    def print_board(self):
        for row in self.board:
            print(row)
    
    def check_winner(self):
        # Check rows
        for row in self.board:
            if row[0] == row[1] == row[2] != '':
                return True

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != '':
                return True

        # Check diagonals
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True

        return False
    
    def check_tie(self):
        for row in self.board:
            for cell in row:
                if cell == '':
                    return False
        return True

class AI(Player):
    def __init__(self, name, symbol):
        super().__init__(name, symbol, is_ai=True)
    
    def make_move(self, game):
        opponent_symbol = self.get_opponent_symbol()

        # Check if the AI can win in the next move
        for row in range(3):
            for col in range(3):
                if game.board[row][col] == '':
                    game.board[row][col] = self.symbol
                    if game.check_winner():
                        return
                    game.board[row][col] = ''

        # Check if the opponent can win in the next move and block them
        for row in range(3):
            for col in range(3):
                if game.board[row][col] == '':
                    game.board[row][col] = opponent_symbol
                    if game.check_winner():
                        game.board[row][col] = self.symbol
                        return
                    game.board[row][col] = ''

        # If neither the AI nor the opponent can win in the next move, choose a random empty cell
        empty_cells = [(row, col) for row in range(3) for col in range(3) if game.board[row][col] == '']
        if empty_cells:
            row, col = random.choice(empty_cells)
            game.board[row][col] = self.symbol
            return

        # Check if the center cell is empty
        if game.board[1][1] == '':
            game.board[1][1] = self.symbol
            return

        # Check if the opponent played in a corner cell and play in the center cell
        for row in range(0, 3, 2):
            for col in range(0, 3, 2):
                if game.board[row][col] == opponent_symbol:
                    game.board[1][1] = self.symbol
                    return

        # Check if the opponent played in the center cell and play in a corner cell
        if game.board[1][1] == opponent_symbol:
            for row in range(0, 3, 2):
                for col in range(0, 3, 2):
                    if game.board[row][col] == '':
                        game.board[row][col] = self.symbol
                        return

        # Play in any empty cell
        for row in range(3):
            for col in range(3):
                if game.board[row][col] == '':
                    game.board[row][col] = self.symbol
                    return

if __name__ == "__main__":
    # Example usage:
    player1 = Player("Player 1", "X")
    player2 = AI("AI", "O")
    tic_tac_toe_game = Game(player1, player2)

    # Make some moves
    tic_tac_toe_game.make_move(0, 0)
    tic_tac_toe_game.make_move(1, 1)
    tic_tac_toe_game.make_move(2, 2)

    # Print the current state of the board
    tic_tac_toe_game.print_board()

    # Check for a winner or tie
    if tic_tac_toe_game.check_winner():
        print(f"{tic_tac_toe_game.players[tic_tac_toe_game.current_player].name} wins!")
    elif tic_tac_toe_game.check_tie():
        print("It's a tie!")
    