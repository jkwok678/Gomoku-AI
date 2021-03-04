import numpy as np
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
    def genMaxMoves(board):
        moves =[]
        for row in range(self.BOARD_SIZE):
            for single in range(self.BOARD_SIZE):
                if (board[row][single] == 0):
                    new_move = np.copy(board)
                    new_move[row][single] = 1
                    moves.append(new_move)
        return moves
    #A method to generate opponent moves
    def genMinMoves(board):
        moves =[]
        for row in range(self.BOARD_SIZE):
            for single in range(self.BOARD_SIZE):
                if (board[row][single] == 0):
                    new_move = np.copy(board)
                    new_move[row][single] = -1
                    moves.append(new_move)
        return moves
        
    def alphaBeta(self, board,curr_depth, max_depth, max_play, alpha,beta):
        if (curr_depth==max_depth):
            return 0 #evaluation of position
        
        if max_play== True:
            max_score=-1000000
            moves = genMaxMoves(board)
            for move in moves:
                score = minimax2(move, curr_depth+1, max_depth, False, alpha, beta)
                max_score = max(score, max_score)
                alpha = max(alpha, score)
                if (beta<= alpha)
                    break
            return max_score
        else:
            min_score = 1000000
            moves = genMinMoves(board)
            for move in moves:
                score = minimax2(move, curr_depth+1, max_depth, True, alpha, beta)
                min_score = min(score, min_score)
                beta = min(beta, score)
                if beta <= alpha:
                    break
            return min_score


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

    def generateNewMoves(board):
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
                    moves_score.append(new_move_score)
        return moves, moves_score
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


    def move(self, board):
        print(board)
        alpha = -1000000
        beta = 1000000
        score = alphaBeta(board,0, 5, True, alpha,beta)
        moves = generateNewMoves(board)
        x = 0
        y = 0
        for move in moves:
            result = 0
            #move = heuristic algorthim
            if move == score:
                for row in move:
                    for single in row:
                        if single==2:
                            x= row
                            y = single

        return (x,y)

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