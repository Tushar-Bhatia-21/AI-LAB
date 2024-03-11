import math

# Represents the Tic-Tac-Toe board
class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    # Prints the board
    def print_board(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    # Checks if the game is over
    def game_over(self):
        for row in self.board:
            if row.count('X') == 3 or row.count('O') == 3:
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] and self.board[0][col] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] and self.board[0][0] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] and self.board[0][2] != ' ':
            return True
        return False

    # Gets empty cells on the board
    def get_empty_cells(self):
        return [(i, j) for i in range(3) for j in range(3) if self.board[i][j] == ' ']

    # Makes a move on the board
    def make_move(self, row, col, player):
        self.board[row][col] = player

    # Undo the move on the board
    def undo_move(self, row, col):
        self.board[row][col] = ' '

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing_player, alpha, beta):
    if board.game_over() or depth == 0:
        if board.game_over():
            if is_maximizing_player:
                return -1
            else:
                return 1
        else:
            return 0

    if is_maximizing_player:
        max_eval = -math.inf
        for row, col in board.get_empty_cells():
            board.make_move(row, col, 'O')
            eval = minimax(board, depth - 1, False, alpha, beta)
            board.undo_move(row, col)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for row, col in board.get_empty_cells():
            board.make_move(row, col, 'X')
            eval = minimax(board, depth - 1, True, alpha, beta)
            board.undo_move(row, col)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

# Function to find the best move using Minimax
def find_best_move(board):
    best_move = (-1, -1)
    best_eval = -math.inf
    for row, col in board.get_empty_cells():
        board.make_move(row, col, 'O')
        eval = minimax(board, 5, False, -math.inf, math.inf)  # Depth is set to 5
        board.undo_move(row, col)
        if eval > best_eval:
            best_eval = eval
            best_move = (row, col)
    return best_move

# Main function to play Tic-Tac-Toe
def play_tic_tac_toe():
    board = Board()
    while not board.game_over():
        board.print_board()
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        board.make_move(row, col, 'X')
        if board.game_over():
            break
        best_move = find_best_move(board)
        board.make_move(best_move[0], best_move[1], 'O')
    board.print_board()
    if 'O' in board.board[0]:
        print("You lose!")
    elif 'X' in board.board[0]:
        print("You win!")
    else:
        print("It's a draw!")

# Play Tic-Tac-Toe
play_tic_tac_toe()
