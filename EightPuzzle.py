from search import *

eight_puzzle = EightPuzzle((1, 2, 3, 5, 7, 4, 8, 6, 0)) # <- change this

class EightPuzzle(Problem):

    def __init__(self, initial, goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        super().__init__(initial, goal)
    def goal_test(self, state):
        return state == self.goal

    def find_blank_square(self, state):
        """Return the index of the blank square in a given state"""
        return state.index(0)

    
    greedy_best_first_graph_search = best_first_graph_search

    def astar_search(problem, h=None, display=False):
        h = memoize(h or problem.h, 'h')
        return best_first_graph_search(problem, lambda n: n.path_cost + h(n), display)


    def actions(self, state):
        possible_actions = ['UP', 'DOWN', 'LEFT', 'RIGHT']
        index_blank_square = self.find_blank_square(state)

        if index_blank_square == 0:
            return ['DOWN','RIGHT']
        if index_blank_square == 1:
            return ['DOWN','LEFT','RIGHT']
        if index_blank_square == 2:
            return ['LEFT','DOWN']
        if index_blank_square == 3:
            return ['DOWN','RIGHT','UP']
        if index_blank_square == 4:
            return ['DOWN','RIGHT','UP','LEFT']
        if index_blank_square == 5:
            return ['DOWN','UP','LEFT']
        if index_blank_square == 6:
            return ['UP','RIGHT']
        if index_blank_square == 7:
            return ['LEFT','RIGHT','UP']
        if index_blank_square == 8:
            return ['UP','LEFT']
    
    def result(self, state, action):
        """ Given state and action, return a new state that is the result of the action.
        Action is assumed to be a valid action in the state """

        # blank is the index of the blank square
        blank = self.find_blank_square(state)
        new_state = list(state)

        delta = {'UP': -3, 'DOWN': 3, 'LEFT': -1, 'RIGHT': 1}
        neighbor = blank + delta[action]
        new_state[blank], new_state[neighbor] = new_state[neighbor], new_state[blank]

        return tuple(new_state)

        
        

if __name__ == '__main__':   
    #solution = depth_first_graph_search(eight_puzzle).solution()
    #print(solution)
    #solution = breadth_first_graph_search(eight_puzzle).solution()
    #print(solution)
    print(breadth_first_graph_search(eight_puzzle, display=True).solution())
    print(astar_search(eight_puzzle, h=None, display=True).solution()) 
    #print(eight_puzzle.actions((0, 1, 2, 3, 4, 5, 6, 7, 8)))
    #print(eight_puzzle.result((0, 1, 2, 3, 4, 5, 6, 7, 8), 'DOWN'))
    #print(breadth_first_graph_search(eight_puzzle).solution())
