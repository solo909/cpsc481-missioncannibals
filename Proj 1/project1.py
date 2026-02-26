from search import *

class MissCannibalsVariant(Problem):

    def __init__(self, N1=4, N2=4, goal=(0, 0, False)):
        initial = (N1, N2, True)
        self.N1 = N1
        self.N2 = N2
        super().__init__(initial, goal)

    def goal_test(self, state):
        return state == self.goal

    def result(self, state, action):
        m, c, onLeft = state

        m_move = action.count('M')
        c_move = action.count('C')

        if onLeft:
            return (m - m_move, c - c_move, False)
        else:
            return (m + m_move, c + c_move, True)

    def actions(self, state):
        m, c, onLeft = state
        valid_actions = []

        for m_move in range(4):
            for c_move in range(4):

                total = m_move + c_move
                if total < 1 or total > 3:
                    continue

                action = ('M' * m_move) + ('C' * c_move)

                if onLeft:
                    if m_move > m or c_move > c:
                        continue
                    new_m = m - m_move
                    new_c = c - c_move
                else:
                    if m_move > (self.N1 - m) or c_move > (self.N2 - c):
                        continue
                    new_m = m + m_move
                    new_c = c + c_move

                right_m = self.N1 - new_m
                right_c = self.N2 - new_c

                if new_m > 0 and new_m < new_c:
                    continue
                if right_m > 0 and right_m < right_c:
                    continue
                valid_actions.append(action)

        return valid_actions

if __name__ == '__main__':
    mc = MissCannibalsVariant(4, 4)

    path = depth_first_graph_search(mc).solution()
    print(path)

    path = breadth_first_graph_search(mc).solution()
    print(path)