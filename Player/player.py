import numpy as np
import math
from sklearn.utils import shuffle

class GomokuAgent:
    def __init__(self, ID, BOARD_SIZE, X_IN_A_LINE):
        self.ID = ID
        self.BOARD_SIZE = BOARD_SIZE
        self.X_IN_A_LINE = X_IN_A_LINE
        


    def move(self, board):
        return (0,0)

class Player(GomokuAgent):
    def __init__(self, ID, BOARD_SIZE, X_IN_A_LINE):
        self.moves = 0
        self.ID = ID
        self.BOARD_SIZE = BOARD_SIZE
        self.X_IN_A_LINE = X_IN_A_LINE
        self.first = True
        self.my_last_x_move = 0
        self.my_last_y_move = 0
        self.oponent_last_x_move = 0
        self.oponent_last_y_move = 0
        self.old_board = np.zeros((BOARD_SIZE,BOARD_SIZE), dtype=int)
        self.turn = 0 

    def minimax2(self, depth, board, max):
        if (depth==0):
            return 0 #evaluation of position
        
        # Max player moves
        if max== True:
            max_score=-1000000
            moves = self.genMaxMoves(board)
            for move in moves:
                score = self.minimax2(move, depth-1, False)
                #max score = to new max score if new number is higher
                max_score = max(score, max_score)
            return max_score
            #Min player moves
        else:
            min_score = 1000000
            moves = self.genMinMoves(board)
            for move in moves:
                score = self.minimax2(move, depth-1, True)
                #min score = to new min score if new number is lower
                min_score = min(score, min_score)
            return min_score
    # A method to generate moves for ourselves
    def genMaxMoves(self,board, last_x_move, last_y_move):
         
        last_x_box_1 = last_x_move-2
        last_x_box_2 = last_x_move+2
        last_y_box_1 = last_y_move-2
        last_y_box_2 = last_y_move+2
        #Make sure the box doesn't go out of bounds
        if last_x_box_1 < 0:
           last_x_box_1 = 0
           #Increase box size in other direction
           last_x_box_2 = 6
        if last_x_box_2 > self.BOARD_SIZE:
           last_x_box_2 = self.BOARD_SIZE-1
           #Increase box size in other direction
           last_x_box_1 = 5
        if last_y_box_1 < 0:
           last_y_box_1 = 0
           #Increase box size in other direction
           last_y_box_2 = 6
        if last_y_box_2 > self.BOARD_SIZE:
           last_y_box_2 = self.BOARD_SIZE-1
           #Increase box size in other direction
           last_y_box_1 = 5

        moves =[]
        move_location =[]
        for row in range(last_y_box_1, last_y_box_2):
            for single in range(last_x_box_1, last_x_box_2):
                if (board[row][single] == 0):
                    new_move = np.copy(board)
                    if (self.first):
                        new_move[row][single] = 1
                    else:
                        new_move[row][single] = -1
                    move_location.append((row, single))
                    moves.append(new_move)
        moves_2, move_location_2 = shuffle(moves, move_location)
        return moves_2, move_location_2
    #A method to generate opponent moves
    def genMinMoves(self,board, last_x_move, last_y_move):
        
        last_x_box_1 = last_x_move-2
        last_x_box_2 = last_x_move+2
        last_y_box_1 = last_y_move-2
        last_y_box_2 = last_y_move+2
        if last_x_box_1 < 0:
           last_x_box_1 = 0
        if last_x_box_2 > self.BOARD_SIZE:
           last_x_box_2 = self.BOARD_SIZE-1
        if last_y_box_1 < 0:
           last_y_box_1 = 0
        if last_y_box_2 > self.BOARD_SIZE:
           last_y_box_2 = self.BOARD_SIZE-1
        moves =[]
        move_location =[]
        for row in range(last_y_box_1, last_y_box_2):
            for single in range(last_x_box_1, last_x_box_2):
                if (board[row][single] == 0):
                    new_move = np.copy(board)
                    if (self.first):
                        new_move[row][single] = -1
                    else:
                        new_move[row][single] = 1
                    move_location.append((row, single))
                    moves.append(new_move)
        moves_2, move_location_2 = shuffle(moves, move_location)
        return moves_2, move_location_2
        

    def alphaBetaR(self, board,curr_depth, max_depth, max_play, alpha,beta, last_x_move, last_y_move):
        if (curr_depth==max_depth):
            return self.totalScore2(board),board
        
        if max_play== True:
            max_score=-1000000
            moves,move_location = self.genMaxMoves(board, self.oponent_last_x_move, self.oponent_last_y_move)
            for index in range(len(moves)):
                move_x,move_y = move_location[index]
                score,board = self.alphaBetaR(moves[index], curr_depth+1, max_depth, False, alpha, beta, move_x, move_y)
                max_score = max(score, max_score)
                alpha = max(alpha, score)
                if beta<= alpha:
                    break
            return max_score,board
        else:
            min_score = 1000000
            moves, move_location = self.genMinMoves(board, self.oponent_last_x_move, self.oponent_last_y_move)
            for index in range(len(moves)):
                move_x,move_y = move_location[index]
                score,board = self.alphaBetaR(moves[index], curr_depth+1, max_depth, True, alpha, beta, move_x, move_y)
                min_score = min(score, min_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score,board

    def generateNewMoves(self,board):
        moves =[]
        moves_score =[]
        for row in range(self.BOARD_SIZE):
            for single in range(self.BOARD_SIZE):
                if (board[row][single] == 0):
                    new_move = np.copy(board)
                    new_move[row][single] = 2
                    moves.append(new_move)
                    # Place your evaluation function here
                    #new_move_score = yourFunction(board)
                    
        return moves
  


    def move(self, board):
        print(board)
        for x in range(self.BOARD_SIZE):
            for y in range(self.BOARD_SIZE):
                if (self.old_board[x][y] != board[x][y]):
                    self.oponent_last_x_move = x
                    self.oponent_last_y_move = y
        
        counters = np.count_nonzero(board)
        if(counters<2):
            if (counters ==0):
                self.first = True
            else:
                self.first = False

        alpha = -1000000
        beta = 1000000
        op_last_x = self.oponent_last_x_move
        op_last_y = self.oponent_last_y_move
        score,board_move = self.alphaBetaR(board,0, 4, True, alpha,beta , op_last_x, op_last_y)
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if board_move[row][column]!=board[row][column]:
                    x = row
                    y = column
        self.turn+=1
        self.old_board = board_move
        return (x,y)


    def totalScore2(self, board):
        score_player = 0
        score_player = score_player + self.lookHorizontal(board,1,-1)
        score_player = score_player + self.lookVertical(board,1,-1)
        score_player = score_player + self.lookDiagonal(board,1,-1)
        score_other_player = 0
        score_other_player = score_other_player + self.lookHorizontal(board,-1,1)
        score_other_player = score_other_player + self.lookVertical(board,-1,1)
        score_other_player = score_other_player + self.lookDiagonal(board,-1,1)
        total_score = score_player - score_other_player

        return total_score
        

    def lookHorizontal(self,board, our_number, opponent_number):
        score = 0 
        consecutive = 0
        open_endings = 0
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                #First check if it's the our piece
                if (board[row][column] == our_number):
                    consecutive += 1
                elif (board[row][column] == opponent_number):
                    score += self.score2(consecutive, open_endings)
                    consecutive = 0
                    open_endings = 0
                elif (board[row][column] == 0 and consecutive > 0):
                    open_endings += 1
                    score += self.score2(consecutive, open_endings)
                    consecutive = 0
                    open_endings = 1
                elif (board[row][column] == 0):
                    open_endings = 1
                elif (consecutive > 0):
                    score += self.score2(consecutive, open_endings)
                    consecutive = 0
                    open_endings = 0
                else:
                    open_endings = 0
            #Extra if statement for something that ends on the last row and last column
            if (consecutive > 0):
                score += self.score2(consecutive, open_endings)
                consecutive = 0
                open_endings = 0
        return score

    def lookVertical(self,board, our_number, opponent_number):
        score = 0 
        consecutive = 0
        open_endings = 0
        for column in range(self.BOARD_SIZE):
            for row in range(self.BOARD_SIZE):
                #First check if it's the our piece
                if (board[row][column] == our_number):
                    consecutive += 1
                elif (board[row][column] == opponent_number):
                    score += self.score2(consecutive, open_endings)
                    consecutive = 0
                    open_endings = 0
                elif (board[row][column] == 0 and consecutive > 0):
                    open_endings += 1
                    score += self.score2(consecutive, open_endings)
                    consecutive = 0
                    open_endings = 1
                elif (board[row][column]== 0):
                    open_endings = 1
                elif (consecutive>0):
                    score += self.score2(consecutive, open_endings)
                    consecutive = 0
                    open_endings = 0
                else:
                    open_endings = 0
            #Extra if statement for something that ends on the last row and last column
            if (consecutive>0):
                score += self.score2(consecutive, open_endings)
                consecutive =0
                open_endings = 0
        return score

    def lookDiagonal(self, board, our_number, opponent_number):
        score = 0 
        consecutive = 0
        open_endings = 0
        rows,cols = board.shape
        negative_diagonal = -1 * ((math.ceil(rows/2)) + math.floor(rows/2) -1)
        #negative_diagonal = -1 * ((math.ceil(rows/2)) + math.floor(rows/2) )
        flip_board = np.copy(board)
        flip_board = np.flipud(flip_board)
        positive_diagonal = (math.ceil(rows/2)) + math.floor(rows/2)
        #positive_diagonal = (math.floor(rows/2)) + math.floor(rows/2)
        for x in range(negative_diagonal, positive_diagonal):
            diagonal = np.diagonal(board,x)
            if (len(diagonal>0)):
                for index in range(len(diagonal)):
                    #First check if it's the our piece
                    if (diagonal[index] == our_number):
                        consecutive += 1
                    elif (diagonal[index] == opponent_number):
                        score += self.score2(consecutive, open_endings)
                        consecutive = 0
                        open_endings = 0
                    elif (diagonal[index] == 0 and consecutive > 0):
                        open_endings += 1
                        score += self.score2(consecutive, open_endings)
                        consecutive = 0
                        open_endings = 1
                    elif (diagonal[index] == 0):
                        open_endings = 1
                    elif (consecutive > 0):
                        score += self.score2(consecutive, open_endings)
                        consecutive = 0
                        open_endings = 0
                    else:
                        open_endings = 0
                #Extra if statement for something that ends on the last row and last column
                if (consecutive > 0):
                    score += self.score2(consecutive, open_endings)
                    consecutive = 0
                    open_endings = 0
            
        for x in range(negative_diagonal, positive_diagonal):
            diagonal = np.diagonal(flip_board,x)
            if (len(diagonal)>0):
                for index in range(len(diagonal)):
                    #First check if it's the our piece
                    if (diagonal[index] == our_number):
                        consecutive += 1
                    elif (diagonal[index] == opponent_number):
                        score += self.score2(consecutive, open_endings)
                        consecutive = 0
                        open_endings = 0
                    elif (diagonal[index] == 0 and consecutive > 0):
                        open_endings += 1
                        score += self.score2(consecutive, open_endings)
                        consecutive = 0
                        open_endings = 1
                    elif (diagonal[index] == 0):
                        open_endings = 1
                    elif (consecutive > 0):
                        score += self.score2(consecutive, open_endings)
                        consecutive = 0
                        open_endings = 0
                    else:
                        open_endings = 0
                #Extra if statement for something that ends on the last row and last column
                if (consecutive > 0):
                    score += self.score2(consecutive, open_endings)
                    consecutive = 0
                    open_endings = 0
            return score


    def score2(self, consecutive, open_endings):
        if (consecutive <5 and open_endings ==0):
            return 0
        
        if (consecutive == 4 and open_endings == 2):
            return 100
        elif (consecutive == 4 and open_endings == 1):
            return 10
        elif (consecutive == 3 and open_endings == 2):
            return 20
        elif (consecutive == 3 and open_endings == 1):
            return 7
        elif (consecutive == 2 and open_endings == 2):
            return 5
        elif (consecutive == 2 and open_endings == 1):
            return 4
        elif (consecutive == 1 and open_endings == 2):
            return 2
        elif (consecutive == 1 and open_endings == 1):
            return 1
        else:
            return 0
