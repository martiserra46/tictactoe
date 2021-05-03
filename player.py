import random
import math

class Player():
    def __init__(self, piece):
        self.piece = piece
    
    def get_movement(self, ticTacToe):
        pass

class HumanPlayer(Player):
    def get_movement(self, ticTacToe):
        valid_position = False
        while not valid_position:
            try:
                result = input("row,col: ").split(",")
                row, col = int(result[0]), int(result[1])
                if not ticTacToe.can_move(row, col):
                    raise ValueError
                valid_position = True
            except Exception:
                print("Invalid value. Try again")
        return row, col

class RandomComputerPlayer(Player):
    def get_movement(self, ticTacToe):
        valid_position = False
        while not valid_position:
            row = random.randint(0, 3)
            column = random.randint(0, 3)
            valid_position = ticTacToe.can_move(row, column)
        return row, column

class GeniusComputerPlayer(Player):
    def get_movement(self, ticTacToe):
        (row, column) = self.get_score(ticTacToe, self.piece)['movement']
        return row, column
    
    def get_score(self, ticTacToe, piece):
        if self.is_final_state(ticTacToe):
            return self.score_final_state(ticTacToe)
        
        list_scores = self.obtain_possible_scores(ticTacToe, piece)

        best_score = self.obtain_best_score(list_scores, piece)

        return best_score

    def is_final_state(self, ticTacToe):
        return ticTacToe.has_won('X') or ticTacToe.has_won('O') or ticTacToe.is_full()
    
    def score_final_state(self, ticTacToe):
        if ticTacToe.has_won('X'):
            score = 1 * (ticTacToe.num_empty_spaces() + 1)
        elif ticTacToe.has_won('O'):
            score = -1 * (ticTacToe.num_empty_spaces() + 1)
        elif ticTacToe.is_full():
            score = 0
        return {'movement': (None, None), 'score': score}
    
    def obtain_possible_scores(self, ticTacToe, piece):
        list_scores = []
        other_piece = 'O' if piece == 'X' else 'X'
        for row in range(ticTacToe.dim_size):
            for col in range(ticTacToe.dim_size):
                if ticTacToe.board[row][col] == ' ':
                    ticTacToe.board[row][col] = piece
                    score = self.get_score(ticTacToe, other_piece)
                    score['movement'] = (row, col)
                    list_scores.append(score)
                    ticTacToe.board[row][col] = ' '
        return list_scores
    
    def obtain_best_score(self, list_scores, piece):
        if piece == 'X':
            max_score = {'movement': (None, None), 'score': -math.inf}
            for i in range(len(list_scores)):
                if list_scores[i]['score'] > max_score['score']:
                    max_score = list_scores[i]
            return max_score
        if piece == 'O':
            min_score = {'movement': (None, None), 'score': math.inf}
            for i in range(len(list_scores)):
                if list_scores[i]['score'] < min_score['score']:
                    min_score = list_scores[i]
            return min_score