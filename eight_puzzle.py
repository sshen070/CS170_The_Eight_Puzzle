# Eight Puzzle Solver
# Supports:
# 1) Uniform Cost Search (UCS)
# 2) A* with Misplaced Tile heuristic
# 3) A* with Manhattan Distance heuristic
import random

# Default States
trivial =  [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]
veryEasy = [[1, 2, 3],
            [4, 5, 6],
            [7, 0, 8]]
easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]
doable = [[0, 1, 2],
        [4, 5, 3],
        [7, 8, 6]]
oh_boy = [[8, 7, 1],
            [6, 0, 2],
            [5, 4, 3]]

default_states = [trivial, veryEasy, easy, doable, oh_boy]


goal_state = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 0]]

class puzzleState:
    def __init__(self, currPuzzle):
        self.state = currPuzzle 
        self.prev = None

    
    
def randomPuzzle():
    return default_states[random.randint(0, len(default_states) - 1)]

def printPuzzle(self):
    puzzle_str = ''
    for i in range (len(self.state)):
        for j in range (len(self.state[i])):
            if j != len(self.state[i]) - 1:
                puzzle_str += str(self.state[i][j]) + ' '
                continue
            puzzle_str += str(self.state[i][j]) + '\n'

    print(puzzle_str)


def main():
    puzzle_mode = input("Welcome to an 8-Puzzle Solver. Type '1' to use a default puzzle, "
    "or '2' to create your own."+ '\n')

    if puzzle_mode == "1":
        puzzle1 = puzzleState(randomPuzzle())
        printPuzzle(puzzle1)

    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
        "Please only enter valid 8-puzzles. Enter the puzzle demilimiting " 
        + "the numbers with a space. Type RETURN only when finished." + '\n')

        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")

        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()

        # Matrix positions must be ints
        for i in range (0, 3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])

        puzzle1 = puzzleState([[puzzle_row_one][puzzle_row_two][puzzle_row_three]])

if __name__ == '__main__':
    main()
