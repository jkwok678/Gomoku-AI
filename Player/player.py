import numpy as np
import math
class GomokuAgent:
    def __init__(self, ID, BOARD_SIZE, X_IN_A_LINE):
        self.ID = ID
        self.BOARD_SIZE = BOARD_SIZE
        self.X_IN_A_LINE = X_IN_A_LINE
        self.first = True

    def move(self, board):
        return (0,0)

class Player(GomokuAgent):
    def __init__(self, ID, BOARD_SIZE, X_IN_A_LINE):
        self.moves = 0
        self.ID = ID
        self.BOARD_SIZE = BOARD_SIZE
        self.X_IN_A_LINE = X_IN_A_LINE

    def minimax2(self, depth, board, max):
        if (depth==0):
            return 0 #evaluation of position
        
        # Max player moves
        if max== True:
            max_score=-1000000
            moves = genMaxMoves(board)
            for move in moves:
                score = minimax2(move, depth-1, False)
                #max score = to new max score if new number is higher
                max_score = max(score, max_score)
            return max_score
            #Min player moves
        else:
            min_score = 1000000
            moves = genMinMoves(board)
            for move in moves:
                score = minimax2(move, depth-1, True)
                #min score = to new min score if new number is lower
                min_score = min(score, min_score)
            return min_score
    # A method to generate moves for ourselves
    def genMaxMoves(self,board):
        moves =[]
        for row in range(self.BOARD_SIZE):
            for single in range(self.BOARD_SIZE):
                if (board[row][single] == 0):
                    new_move = np.copy(board)
                    if (self.first):
                        new_move[row][single] = 1
                    else:
                        new_move[row][single] = -1
                    moves.append(new_move)
        return moves
    #A method to generate opponent moves
    def genMinMoves(self,board):
        moves =[]
        for row in range(self.BOARD_SIZE):
            for single in range(self.BOARD_SIZE):
                if (board[row][single] == 0):
                    new_move = np.copy(board)
                    if (self.first):
                        new_move[row][single] = -1
                    else:
                        new_move[row][single] = 1
                    moves.append(new_move)
        return moves
        
    def alphaBetaR(self, board,curr_depth, max_depth, max_play, alpha,beta):
        if (curr_depth==max_depth):
            return self.totalScore2(board),board
        
        if max_play== True:
            max_score=-1000000
            moves = self.genMaxMoves(board)
            for move in moves:
                score,board = self.alphaBetaR(move, curr_depth+1, max_depth, False, alpha, beta)
                max_score = max(score, max_score)
                alpha = max(alpha, score)
                if beta<= alpha:
                    break
            return max_score,board
        else:
            min_score = 1000000
            moves = self.genMinMoves(board)
            for move in moves:
                score,board = self.alphaBetaR(move, curr_depth+1, max_depth, True, alpha, beta)
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
        counters = np.count_nonzero(board)
        if(counters<2):
            if (counters ==0):
                self.first = True
            else:
                self.first = False

        alpha = -1000000
        beta = 1000000
        score,board_move = self.alphaBetaR(board,0, 3, True, alpha,beta)
        for row in range(self.BOARD_SIZE):
            for column in range(self.BOARD_SIZE):
                if board_move[row][column]!=board[row][column]:
                    x = row
                    y = column
        """moves = self.genMaxMoves(board)
        moves2 = self.generateNewMoves(board)
        x = 0
        y = 0
        print(score)
        for move_index in range(len(moves)):
            result = 0
            move_score =self.totalScore2(moves[move_index])
            print(move_score)
            if move_score == score:
                new_move = moves2[move_index]
                for row in new_move:
                    for single in row:
                        if single==2:
                            x = row
                            y = single
        """
        return (x,y)

    def totalScore(self, board):
        
        score_player = 0
        score_player = score_player + scoreHorizontal(board,1)
        score_player = score_player + scoreVertical(board,1)
        score_player = score_player + scoreDiagonal(board,1)
        score_other_player = 0
        score_other_player = score_other_player + scoreHorizontal(board,-1)
        score_other_player = score_other_player + scoreVertical(board,-1)
        score_other_player = score_other_player + scoreDiagonal(board,-1)
        total_score = score_player - score_other_player

        return total_score
     
    def scoreHorizontal(self,board,number):
        rows,cols = board.shape
        score = 0
        for row in range(rows):
            for single in range(cols):
                if(single<cols-self.X_IN_A_LINE):
                    print(board[row, single:single+X_IN_A_LINE])
                    #score= score + pattern_match()
        return score

    def scoreVertical(self, board, number):
        rows,cols = board.shape
        score = 0
        for column in range(cols):
            for single in range(rows):
                if(single<rows-self.X_IN_A_LINE):
                    print(board[single:single+X_IN_A_LINE, column])
                    #score= score + pattern_match()
        return score

    def scoreDiagonal(seld, board, number):
        rows,cols = board.shape
        negative_diagonal = -1 *((math.ceil(rows/2)) + math.floor(rows/2) -1)
        print(negative_diagonal)
        flip_board = np.copy(board)
        flip_board = np.flipud(flip_board)
        positive_diagonal = (math.ceil(rows/2)) + math.floor(rows/2)
        print(positive_diagonal)
        for x in range(negative_diagonal, positive_diagonal):
            print(np.diagonal(board,x))
             #score= score + pattern_match()
        for x in range(negative_diagonal, positive_diagonal):
            print(np.diagonal(flip_board,x))
            #score= score + pattern_match()
        return 0

    def patternMatch(section):
        return 0


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

"""
class Node:
    self.parent
    self.children = []
    self.state
    self.score =0
    self.depth

    def __init__(self, parent, state, score, depth):
        self.parent = parent
        self.state = state
        self.score = score
        self.depth = depth
"""

"""

    def minimax(self, target_depth, board):
        # first move at the centre
        if(self.moves==0):
            print(self.BOARD_SIZE/2)
            return(int(self.BOARD_SIZE/2),int(self.BOARD_SIZE/2))
        else:
            root  = Node(None, board, score)
            #moves,moves_score = generateNewMoves(board)
            #recursive function to generate moves and scores?
            recursiveMiniMax(board, 5, 1,root, 0)

            for x in moves:
            max_score_index = max_score.index(max(moves_score))        
            move_to_take = moves[max_score_index]
            x_pos = 0
            y_pos = 0
            for row in range(self.BOARD_SIZE):
                for single in range(self.BOARD_SIZE):
                    if (move_to_take[row][single] == 2): 
                        x_pos = row
                        y_pos = single

            print("end")
            return(x_pos,x_pos)
"""

"""
    def recursiveMiniMax(board, target_depth, currentDepth,parent):
        moves,moves_score = generateNewMoves(board)
        for move in moves:
            new_node = Node(parent, moves, scores)
            parent.children.append(new_node)
            new_board = np.copy(moves)
            for row in new_board:
                for single in row:
                    if single==2:
                        single=1
            if (currentDepth<target_depth):
                recursiveMiniMax(new_board,target_depth,currentDepth, new_node)
 """     