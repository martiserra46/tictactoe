class TicTacToe():
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.dim_size = 3

    def print(self):
        for row in self.board:
            print('| ' + ' | '.join(row) + ' |')

    def make_move(self, row, col, piece):
        if self.can_move(row, col):
            self.board[row][col] = piece
            return True
        return False

    def can_move(self, row, col):
        return 0 <= row and row <= self.dim_size - 1 and 0 <= col and col <= self.dim_size - 1 and self.board[row][col] == ' '
    
    def is_full(self):
        for row in self.board:
            for value in row:
                if value == ' ':
                    return False
        return True
    
    def num_empty_spaces(self):
        num = 0
        for row in self.board:
            for value in row:
                if value == ' ':
                    num += 1
        return num
    
    def has_won(self, piece):
        for row in range(self.dim_size):
            if self.board[row][0] == piece and self.board[row][0] == self.board[row][1] and self.board[row][1] == self.board[row][2]:
                return True
        for column in range(self.dim_size):
            if self.board[0][column] == piece and self.board[0][column] == self.board[1][column] and self.board[1][column] == self.board[2][column]:
                return True
        if self.board[0][0] == piece and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return True
        if self.board[2][0] == piece and self.board[2][0] == self.board[1][1] and self.board[1][1] == self.board[0][2]:
            return True
        return False