from search import *

class MissCnnibalsVariant(Problem):

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        """ Define goal state and initialilze a problem"""
        initial = (N1,N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)

    def actions (