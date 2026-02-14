from eight_puzzle import *

import random
import matplotlib.pyplot as plt


# Default States
trivial =  [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 0]]

easy = [[1, 2, 0],
        [4, 5, 3],
        [7, 8, 6]]

medium_1 = [[1, 2, 3],
            [5, 0, 6],
            [4, 7, 8]]

medium_2 = [[1, 3, 6],
            [5, 0, 2],
            [4, 7, 8]]

hard_1 = [[1, 3, 6],
               [5, 0, 7],
               [4, 8, 2]]

hard_2 = [[7, 1, 2],
               [4, 8, 5],
               [6, 3, 0]]

very_hard = [[8, 7, 1],
                 [6, 0, 2],
                 [5, 4, 3]]

# challenging_2 = [[2, 8, 3],
#                  [1, 6, 4],
#                  [7, 0, 5]]

extreme = [[8, 7, 6],
              [5, 4, 3],
              [2, 1, 0]]


default_states = [trivial, easy, medium_1, medium_2, hard_1, hard_2, very_hard, extreme]


def randomPuzzle(states_selection):
    return states_selection[random.randint(0, len(states_selection) - 1)]


def init_default_puzzle_mode():
    selected_difficulty = input(
        "You wish to use a default puzzle. Please enter a desired difficulty on a scale from 0 to 5." + '\n')
    
    if selected_difficulty == "0":
        print("Difficulty of 'Trivial' selected.")
        return puzzleState(trivial)
    
    elif selected_difficulty == "1":
        print("Difficulty of 'Easy' selected.")
        return puzzleState(easy)
    
    elif selected_difficulty == "2":
        states_selection = [medium_1, medium_2]
        print("Difficulty of 'Medium' selected.")
        return puzzleState(randomPuzzle(states_selection))
    
    elif selected_difficulty == "3":
        states_selection = [hard_1, hard_2]
        print("Difficulty of 'Hard' selected.")
        return puzzleState(randomPuzzle(states_selection))
    
    elif selected_difficulty == "4":
        print("Difficulty of 'Very Hard' selected.")
        return puzzleState(very_hard)
    
    elif selected_difficulty == "5":
        print("Difficulty of 'Extreme' selected.")
        return puzzleState(extreme)
    
    else:
        print("Random Puzzle!")
        return puzzleState(randomPuzzle(default_states))


def select_and_init_algorithm():
    algorithm = input("Select algorithm. (1) for Uniform Cost Search, (2) for the Misplaced Tile Heuristic, "
                      "or (3) the Manhattan Distance Heuristic." + '\n')
    
    algorithm = int(algorithm)

    if (algorithm >= 1 and algorithm < 4):
        return algorithm
    else:
        return 3

def print_statistics(cost, counter, max_queue_size, elapsed_time, final_puzzle):

    traceBack(final_puzzle)
    print(f"Algorithm executed in {elapsed_time:.4f} seconds")
    print(f'Solution Depth: {cost}')
    print(f'Nodes Expanded: {counter}')
    print(f'Max Queue Size: {max_queue_size}')



def main():

    puzzle_mode = input("Welcome to my 8-Puzzle Solver. Type '1' to use a default puzzle, "
    "or '2' to create your own."+ '\n')

    if puzzle_mode == "1":
        puzzle = init_default_puzzle_mode()
        algorithm = select_and_init_algorithm()
        
        if algorithm == 1:
            print('\nRunning Uniform Cost Search...')
        if algorithm == 2:
            print('\nRunning Misplaced Tile Heuristic...')
        if algorithm == 3:
            print('\nRunning Manhattan Distance Heuristic...')

            
        
        start_time = time.perf_counter()
        cost, counter, max_queue_size, final_puzzle = uniform_cost_search(puzzle, algorithm)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time
        
        
        print_statistics(cost, counter, max_queue_size, elapsed_time, final_puzzle)

    if puzzle_mode == "2":
        print("Enter your puzzle, using a zero to represent the blank. " +
            "Please only enter valid 8-puzzles. Enter the puzzle demilimiting " +
            "the numbers with a space. RET only when finished." + '\n')
        
        puzzle_row_one = input("Enter the first row: ")
        puzzle_row_two = input("Enter the second row: ")
        puzzle_row_three = input("Enter the third row: ")

        puzzle_row_one = puzzle_row_one.split()
        puzzle_row_two = puzzle_row_two.split()
        puzzle_row_three = puzzle_row_three.split()

        for i in range(0, 3):
            puzzle_row_one[i] = int(puzzle_row_one[i])
            puzzle_row_two[i] = int(puzzle_row_two[i])
            puzzle_row_three[i] = int(puzzle_row_three[i])

        state = [puzzle_row_one, puzzle_row_two, puzzle_row_three]
        puzzle = puzzleState(state)

        algorithm = select_and_init_algorithm()

        if algorithm == 1:
            print('\nRunning Uniform Cost Search...')
        if algorithm == 2:
            print('\nRunning Misplaced Tile Heuristic...')
        if algorithm == 3:
            print('\nRunning Manhattan Distance Heuristic...')

        start_time = time.perf_counter()
        cost, counter, max_queue_size, final_puzzle = uniform_cost_search(puzzle, algorithm)
        end_time = time.perf_counter()
        elapsed_time = end_time - start_time

        print_statistics(cost, counter, max_queue_size, elapsed_time, final_puzzle)
    
    if puzzle_mode == "3":

        # Keep track of depth per puzzle
        depth = []

        # Experiment 1 (Depth vs Time per algorithm)
        ucs_time = []
        misplaced_tiles_time = []
        manhattan_distance_time = []

        # Experiment 2 (Memory Usage vs Time per algorithm)
        ucs_states_queue = []
        misplaced_tiles_states_queue = []
        manhattan_states_queue = []

        for i in range (len(default_states)):

            state = default_states[i]

            # Uniform Cost Search
            puzzle = puzzleState(state)

            start_time = time.perf_counter()
            cost, counter, max_queue_size, final_puzzle = uniform_cost_search(puzzle, 1)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"Algorithm executed in {elapsed_time:.4f} seconds, Cost: {cost}")

            ucs_states_queue.append(max_queue_size)            
            ucs_time.append(elapsed_time)


            # A* with Misplaced Tile Heuristic
            puzzle = puzzleState(state)

            start_time = time.perf_counter()
            cost, counter, max_queue_size, final_puzzle = uniform_cost_search(puzzle, 2)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"Algorithm executed in {elapsed_time:.4f} seconds, Cost: {cost}")

            misplaced_tiles_states_queue.append(max_queue_size)
            misplaced_tiles_time.append(elapsed_time)


            # A* with Manhattan Distance Heuristic
            puzzle = puzzleState(state)

            start_time = time.perf_counter()
            cost, counter, max_queue_size, final_puzzle = uniform_cost_search(puzzle, 3)
            end_time = time.perf_counter()
            elapsed_time = end_time - start_time
            print(f"Algorithm executed in {elapsed_time:.4f} seconds, Cost: {cost}")

            manhattan_states_queue.append(max_queue_size)
            manhattan_distance_time.append(elapsed_time)

            depth.append(cost)


        # Experiment 1 Plot
        plt.figure()
        plt.plot(depth, ucs_time, marker='o')
        plt.plot(depth, misplaced_tiles_time, marker='o')
        plt.plot(depth, manhattan_distance_time, marker='o')

        plt.xlabel("Solution Depth")
        plt.ylabel("Time (seconds)")
        plt.title("Solution Depth vs Time for 8-Puzzle Algorithms")
        plt.legend(["Uniform Cost Search", "A* Misplaced Tile", "A* Manhattan Distance"])

        plt.show()


        # Experiment 2 Plot
        plt.figure()
        plt.plot(depth, ucs_states_queue, marker='o')
        plt.plot(depth, misplaced_tiles_states_queue, marker='o')
        plt.plot(depth, manhattan_states_queue, marker='o')

        plt.xlabel("Solution Depth")
        plt.ylabel("Memory Usage (Max Queue Size)")
        plt.title("Memory Usage vs Time for 8-Puzzle Algorithms")
        plt.legend(["Uniform Cost Search", "A* Misplaced Tile", "A* Manhattan Distance"])

        plt.show()



if __name__ == '__main__':
    main()
