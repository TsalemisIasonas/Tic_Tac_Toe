import numpy as np
import random
class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)
        self.corners = [(0,0),(0,2),(2,0),(2,2)]
        self.edges = [(0,1),(1,0),(1,2),(2,1)]
        self.first_move = []
        self.current_player_move = [0,0]

    def play(self):
        print('Select who plays first')
        first_player = int(input('Press 1 for CPU, 2 for Player:\t'))
        move = 1
        if first_player == 1:
            while True:
                res = self.check_winner()
                if res == 2:
                    print('Player Wins !')
                    break
                if res == 1:
                    print('CPU Wins !')
                    break

                print('\nCPU Played:')
                self.cpu_first(move)

                res = self.check_winner()
                if res == 2:
                    print('Player Wins !')
                    break
                if res == 1:
                    print('CPU Wins !')
                    break

                if self.is_board_full():
                    print("Draw")
                    break

                self.player_move()
                move+=1
        else:
            while True:
                res = self.check_winner()
                if res == 2:
                    print('Player Wins !')
                    break
                if res == 1:
                    print('CPU Wins !')
                    break

                self.player_move()

                res = self.check_winner()
                if res == 2:
                    print('Player Wins !')
                    break
                if res == 1:
                    print('CPU Wins !')
                    break
                if self.is_board_full():
                    print("Draw")
                    break
                
                print('\nCPU Played:')
                self.cpu_second(move)
                move+=1
            

    def draw_board(self):
        dict = {0:" ",1:"x",2:"o"}
        for i in range(2):
            print(' ' * 3, dict[self.board[i, 0]], '|', dict[self.board[i, 1]], '|', dict[self.board[i, 2]])
            print(' ', '-' * 13)
        print(' ' * 3, dict[self.board[2, 0]], '|', dict[self.board[2, 1]], '|', dict[self.board[2, 2]], '\n')

    def player_move(self):
        position = tuple(input('Give position on board:\n'))
        xdim = int(position[0]) - 1
        ydim = int(position[-1]) - 1
        self.current_player_move[0] = xdim
        self.current_player_move[1] = ydim
        if self.board[xdim, ydim] == 0:
            self.board[xdim, ydim] = 2   # mark with 2 for player
            self.draw_board()
            return
        else:
            print('Blocked cell')
            self.player_move()

    def first_action(self,mark):
        for row in range(3):    #for row in np.nditer(arr):
            if list(self.board[row]).count(0) == 1 and list(self.board[row]).count(mark) == 2:
                pos = list(self.board[row]).index(0)
                self.board[row][pos] = 1
                self.draw_board()
                return True
        for col in range(3):
            if list(self.board[:, col]).count(0) == 1 and list(self.board[:, col]).count(mark) == 2:
                pos = list(self.board[:,col]).index(0)
                self.board[:,col][pos] = 1
                self.draw_board()
                return True
            
        ## TODO the diagnal check can be fixed
        
        diag = list(self.board.diagonal())
        reverse_diag = list(np.fliplr(self.board).diagonal())

        if diag.count(mark) == 2 and diag.count(0) == 1:
            self.board[diag.index(0),diag.index(0)] = 1
            self.draw_board()
            return True
        
        if reverse_diag.count(mark) == 2 and reverse_diag.count(0) == 1:
            if reverse_diag.index(0) == 0:
                self.board[0,2] = 1
            if reverse_diag.index(0) == 1 :
                self.board[1,1] = 1
            if reverse_diag.index(0) == 2:
                self.board[2,0] = 1
            self.draw_board()
            return True
            
        return False
        

    def winning_play(self):
        return self.first_action(1)

    def block(self):
        return self.first_action(2)

    def first_two_moves(self):          # looks to win on current move, then to block on current move
        completed_move = self.winning_play()
        if not completed_move:
            completed_move = self.block()
        return completed_move

    def computer_move(self):            # makes a move if all the previous strategies are not needed
        xdim = random.randint(0, 2)
        ydim = random.randint(0, 2)
        if self.board[xdim, ydim] == 0:
            self.board[xdim, ydim] = 1   # mark with 1 for computer
            self.draw_board()
            return
        else:
            self.computer_move()

    def cpu_second(self,move):          ## controls the flow of the game if the player had the first move
        if not self.first_two_moves():
            if move == 1:
                if self.board[1][1] == 2:
                    xdim, ydim = random.choice(self.corners)
                    self.board[xdim][ydim] = 1
                    self.draw_board()
                else:
                    self.board[1][1] = 1
                    self.draw_board()
            else:                           
                self.computer_move()


    def cpu_first(self,move):           ## controls the flow of the game if the cpu had the first move
        player_played = (self.current_player_move[0],self.current_player_move[1])
        if not self.first_two_moves():
            if move == 1:
                xdim, ydim = random.choice(self.corners)
                self.first_move.append(xdim)
                self.first_move.append(ydim)
                self.board[xdim][ydim] = 1
                self.draw_board()
            elif move == 2 and (self.board[1][1] == 2 or player_played in self.corners):
                xdim = self.first_move[0] - 2
                if xdim < 0: xdim = 2
                ydim = self.first_move[1] - 2
                if ydim < 0: ydim = 2
                if self.board[xdim][ydim] == 0: 
                    self.board[xdim][ydim] = 1
                    self.draw_board()
                else: 
                    while True:
                        x,y = random.choice(self.corners)
                        if self.board[x][y] == 0:
                            break
                    self.board[x][y] = 1
                    self.draw_board()

            elif move == 2 and (player_played in self.edges):
                x,y = player_played
                if self.first_move[1] == y:
                    self.board[self.first_move[0]][abs(self.first_move[1]-2)] = 1
                    self.draw_board()
                else:
                    self.board[abs(self.first_move[0]-2)][self.first_move[1]] = 1
                    self.draw_board()

            elif move == 3:
                count = 0
                for i in self.corners:
                    x,y = i
                    if self.board[x][y] == 0:
                        count +=1
                if count == 2: # 2 free corners, cpu always plays in a corner for the first two moves
                    self.board[1][1] =1
                    self.draw_board()
                elif count ==1:
                    while True:
                        x,y = random.choice(self.corners)
                        if self.board[x][y] == 0:
                            break
                    self.board[x][y] = 1
                    self.draw_board()
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
