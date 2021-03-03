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

    def minimax(self, target_depth, board):
        if(self.moves==0):
            print(self.BOARD_SIZE/2)
            return(int(self.BOARD_SIZE/2),int(self.BOARD_SIZE/2))
        else:
            moves =[]
            moves_score = []
            print("start")
            for row in range(self.BOARD_SIZE):
                for single in range(self.BOARD_SIZE):
                    if (board[row][single] == 0):
                        new_move = np.copy(board)
                        new_move[row][single] = 2
                        moves.append(new_move)
                        new_move_score = yourFunction(board)
                        moves_score.append(new_move_score)

            
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

    def move(self, board):
        print(board)
        x_location, y_location = self.minimax(5,board)
        self.moves+=1
        return (x_location,y_location)

    



    #def calculate_score(self, board):


"""class Node:
    self.parent;
    self.children = [];
    self.score;

    def __init__(self, parent):
        self.parent = parent
"""

