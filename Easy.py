import numpy as np
import random

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)

    def play(self):
        print('Select who plays first')
        first_player = int(input('Press 1 for CPU, 2 for Player:\t'))
        while True:
            #res = self.check_winner()
            if self.check_winner() == 2:
                print('Player Wins !')
                break
            if self.check_winner() == 1:
                print('CPU Wins !')
                break
            if self.is_board_full():
                print("Draw")
                break
            if first_player == 1:
                self.computer_move()
            else:
                self.player_move()

            first_player = 3 - first_player    # switch players (1 -> 2, 2 -> 1)

    def draw_board(self):
        for i in range(2):
            print(' ' * 3, self.board[i, 0], '|', self.board[i, 1], '|', self.board[i, 2])
            print(' ', '-' * 13)
        print(' ' * 3, self.board[2, 0], '|', self.board[2, 1], '|', self.board[2, 2], '\n')

    def player_move(self):
        position = tuple(input('Give position on board:\n'))
        xdim = int(position[0]) - 1
        ydim = int(position[-1]) - 1
        if self.board[xdim, ydim] == 0:
            self.board[xdim, ydim] = 2   # mark with 2 for player
            self.draw_board()
            return
        else:
            print('Blocked cell')
            self.player_move()

    def computer_move(self):
        xdim = random.randint(0, 2)
        ydim = random.randint(0, 2)
        if self.board[xdim, ydim] == 0:
            self.board[xdim, ydim] = 1   # mark with 1 for computer
            print('CPU Played:')
            self.draw_board()
            return
        else:
            self.computer_move()

    def check_winner(self):
        # Check rows
        for i in range(3):
            if self.board[i, 0] == self.board[i, 1] == self.board[i, 2]:
                return self.board[i, 0]
        # Check columns
        for j in range(3):
            if self.board[0, j] == self.board[1, j] == self.board[2, j]:
                return self.board[0, j]
        # Check diagonals
        if self.board[0, 0] == self.board[1, 1] == self.board[2, 2]:
            return self.board[0, 0]
        if self.board[0, 2] == self.board[1, 1] == self.board[2, 0]:
            return self.board[0, 2]
        return 0

    def is_board_full(self):
        return np.all(self.board != 0)

if __name__ == '__main__':
    game = TicTacToe()
    game.play()
