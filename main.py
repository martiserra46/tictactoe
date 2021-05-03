from ticTacToe import TicTacToe
from player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer

class Game():
    def __init__(self):
        pass
    
    def play(self, players):
        ticTacToe = TicTacToe()

        turn = 0

        while not ticTacToe.has_won(players[0].piece) and not ticTacToe.has_won(players[1].piece) and not ticTacToe.is_full():
            ticTacToe.print()
            player = players[turn % 2]
            row, col = player.get_movement(ticTacToe)
            ticTacToe.make_move(row, col, player.piece)
            turn += 1
            print()
        
        ticTacToe.print()

        print()
        
        if ticTacToe.has_won(players[0].piece):
            print(f"{players[0].piece} has won!!!")
        elif ticTacToe.has_won(players[1].piece):
            print(f"{players[1].piece} has won!!!")
        else:
            print("It is a tie!!!")


game = Game()
players = [HumanPlayer('X'), GeniusComputerPlayer('O')]
game.play(players)