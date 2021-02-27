class GomokuAgent:
    def __init__(self, ID, BOARD_SIZE, X_IN_A_LINE):
        self.ID = ID
        self.BOARD_SIZE = BOARD_SIZE
        self.X_IN_A_LINE = X_IN_A_LINE

    def move(self, board):
        return (0,0)

class Player(GomokuAgent):

    def move(self, board):
        print(board)
        return (0, 0)

    #def minimax(self, target_depth):

    #def calculate_score(self, board):


"""class Node:
    self.parent;
    self.children = [];
    self.score;

    def __init__(self, parent):
        self.parent = parent
"""

