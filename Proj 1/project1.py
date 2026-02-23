from search import *

class MissCannibalsVariant(Problem):

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """ Define goal state and initialilze a problem"""
        initial = (N1,N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)

    def actions (self, state):
        M_left, C_left, boat = state
        possible_moves = []             # Stores legal moves

        moves = [
            (1,0),(2,0),(3,0),          # All possible moves
            (0,1),(0,2),(0,3),
            (1,1),(2,1),(1,2)
        ]

        for m, c in moves:

            if boat:                    # If boat is currently on the left, calculate new m or c on the left
                new_M = M_left - m
                new_C = C_left - c

            else:
                new_M = M_left + m      # If boat is currently on the right , the boat is then coming back to 
                new_C = C_left + c      # the left so add their value to the left

            if self.is_valid(new_M, new_C):     # Check if left side counts are valid 

                possible_moves.append((m, c))   # If values are legal then add to possible moves
        
        return possible_moves
