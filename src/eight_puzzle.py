# Eight Puzzle Solver
# 1) Uniform Cost Search (UCS)
# 2) A* with Misplaced Tile heuristic
# 3) A* with Manhattan Distance heuristic

import heapq
import time

goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]


class puzzleState:
    def __init__(self, currPuzzle):
        self.state = currPuzzle
        self.prev = None
        self.cost = 0

def printPuzzle(self):
    puzzle_str = ''
    for i in range (len(self.state)):
        for j in range (len(self.state[i])):
            if j != len(self.state[i]) - 1:
                puzzle_str += str(self.state[i][j]) + ' '
                continue
            puzzle_str += str(self.state[i][j]) + '\n'

    print(puzzle_str)


def findOpenSpot(self):
    for i in range (len(self.state)):
        for j in range (len(self.state[i])):
            if (self.state[i][j] == 0):
                return i, j


# Find all possible state transistions
def findNeighborStates(puzzle):
    neighbors = []

    # Contains x & y coords
    x_coord, y_coord = findOpenSpot(puzzle)
    # print (x_coord, y_coord)

    # Compare with x & y coords to see if transition possible
    transitions_values = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    for transition in transitions_values:

        # Potential transition in x-axis
        if (transition[0] != 0):
            
            # If empty spot '0' is not in the leftmost or rightmost column
            # Check if state is within bounds
            if x_coord + transition[0] >= 0 and x_coord + transition[0] < len(puzzle.state):
                
                # Copy over puzzle state as template and swap values
                new_state = puzzleState(deepCopy(puzzle))
                
                # Swap
                swap_coord = new_state.state[x_coord + transition[0]][y_coord]
                new_state.state[x_coord + transition[0]][y_coord] = new_state.state[x_coord][y_coord]
                new_state.state[x_coord][y_coord] = swap_coord

                neighbors.append(new_state)

        # Potentail transition in y-axis
        if (transition[1] != 0):
            # Same idea for y. If empty spot '0' is not in the first or last (3rd) row
            if y_coord + transition[1] >= 0 and y_coord + transition[1] < len(puzzle.state[0]):
                
                # Copy over puzzle state as template
                new_state = puzzleState(deepCopy(puzzle))

                # Swap
                swap_coord = new_state.state[x_coord][y_coord + transition[1]]
                new_state.state[x_coord][y_coord + transition[1]] = new_state.state[x_coord][y_coord]
                new_state.state[x_coord][y_coord] = swap_coord

                neighbors.append(new_state)

    return neighbors

# Deep copy required to create new puzzle state
def deepCopy(self):
    puzzle_copy = [[0 for _ in range(len(self.state))] for _ in range(len(self.state[0]))]

    for i in range (len(self.state)):
        for j in range (len(self.state[i])):
            puzzle_copy[i][j] = self.state[i][j]

    return puzzle_copy


def isGoalState(puzzle):
    for i in range (len(puzzle.state)):
        for j in range (len(puzzle.state[i])):
            if (puzzle.state[i][j] != goal_state[i][j]):
                return False
    return True
            
            
def puzzleToString(puzzle):
    set_state = ''
    for i in range (len(puzzle.state)):
        for j in range (len(puzzle.state[i])):
            set_state += str(puzzle.state[i][j])
    return set_state


def uniform_cost_search(puzzle, search_type):
    # Use as heap to find state with least cost
    queue = []
    max_queue_size = 0

    # Keep track of visited states to prevent searching repeated states
    # visited = []
    # https://www.w3schools.com/PYTHON/python_sets_add.asp
    visited = set([])
    
    # Tuple to keep track of cost & puzzle state
    puzzle_tuple = (puzzle.cost, 0, puzzle)
    heapq.heappush(queue, puzzle_tuple)

    counter = 1
    while (queue):
        least_cost = heapq.heappop(queue)
        cost, n_scheduled, pop_puzzle = least_cost
        cost = int(cost)

        visited.add(puzzleToString(pop_puzzle))

        # If goal state reached, exit loop
        if (isGoalState(pop_puzzle)):

            # Depth of the solution state, number of nodes expanded, max queue size, puzzle 
            return cost, counter, max_queue_size, pop_puzzle
        
        neighbors = findNeighborStates(pop_puzzle)
        for i in range (len(neighbors)):
            
            if puzzleToString(neighbors[i]) in visited:
                continue

            neighbors[i].prev = pop_puzzle
            h_n = 0

            # If A* Misplaced Tile Heuristic
            if (search_type == 2):
                h_n = numMisplacedTiles(neighbors[i])
            
            if (search_type == 3):
                h_n = manhattanDistanceHeuristic(neighbors[i])

            neighbors[i].cost = pop_puzzle.cost + 1

            # For UCS no heuristic (h(n) = 0) 
            f_n = neighbors[i].cost + h_n

            # Tuple compared in sequential order
            # Break ties between states with the same costs (counter)
            puzzle_tuple = (f_n, counter,  neighbors[i])
            # print(puzzle_tuple)
            heapq.heappush(queue, puzzle_tuple)

            # Keep track of the max queue size
            if (len(queue) > max_queue_size):
                max_queue_size = len(queue)

            counter += 1
        

# Return number of misplaced tiles (matches tiles in goal state)
def numMisplacedTiles(puzzle):
    misplaced_tiles_h = 0

    for i in range (len(puzzle.state)):
        for j in range (len(puzzle.state[i])):
            if (puzzle.state[i][j] != goal_state[i][j]):
                
                # If state is '0' no need to keep track
                # Empty tile will swap with last tile
                if (puzzle.state[i][j] == 0):
                    continue
                misplaced_tiles_h += 1

    return misplaced_tiles_h


def manhattanDistanceHeuristic(puzzle):
    tot_manhattan_distance = 0
    # goal_arr = createGoalArray()

    for i in range (len(puzzle.state)):
        for j in range (len(puzzle.state[i])):
            # if (puzzle.state[i][j] != goal_state[i][j]):
            if (puzzle.state[i][j] == 0):
                continue
            tot_manhattan_distance += findManhattanDistance(puzzle.state[i][j], (i, j))
    
    return tot_manhattan_distance


def findManhattanDistance(tile_number, coords):
    x_coord, y_coord = coords
    
    # How many times number divisible by size of array? --> row number
    row_number = int((tile_number - 1)/len(goal_state))

    # Each row & column start at index 0
    # Last element in each row is divisible by len(goal_state)
    column_number = (tile_number - 1) % len(goal_state)

    # Find difference in x & y components
    return abs(x_coord - row_number) + abs(y_coord - column_number)

def traceBack(puzzle):
    full_path = [puzzle]

    while (puzzle.prev):
        puzzle = puzzle.prev
        full_path.append(puzzle)

    full_path.reverse()

    print(f'Original Puzzle:' )
    printPuzzle(full_path[0])

    for i in range (1, len(full_path)):
        print(f'Step {i}:')
        printPuzzle(full_path[i])



# def createGoalArray():
#     goal_state_array = []
#     puzzle_num = 1
#     for i in range (len(goal_state)):
#         for j in range (len(goal_state[i])):
#             goal_state_array.append((i, j))
#             puzzle_num += 1
    
#     goal_state_array[-1] = [(len(goal_state) - 1, len(goal_state) - 1)]
#     print(goal_state_array)
#     return goal_state_array