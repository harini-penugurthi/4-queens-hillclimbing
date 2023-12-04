import random

def initial_state(board_size):
    """Generate a random initial state for the board."""
    return [random.randint(0, board_size - 1) for _ in range(board_size)]

def conflicts(state, row, col):
    """Count the number of conflicts for a given queen."""
    count = 0
    for i in range(len(state)):
        if i != row:
            if state[i] == col or abs(i - row) == abs(state[i] - col):
                count += 1
    return count

def total_conflicts(state):
    """Count the total number of conflicts on the board."""
    total = 0
    for i in range(len(state)):
        total += conflicts(state, i, state[i])
    return total

def min_conflict(state, max_steps):
    """Solve the Four-Queens problem using min-conflict hill climbing."""
    for _ in range(max_steps):
        if total_conflicts(state) == 0:
            return state  # Solution found
        row = random.randint(0, len(state) - 1)
        col = min_conflict_value(state, row)
        state[row] = col
    return None  # No solution found within the given steps

def min_conflict_value(state, row):
    """Find the column with the minimum conflicts for a given queen."""
    min_conflict_count = float('inf')
    min_conflict_col = -1
    for col in range(len(state)):
        conflict_count = conflicts(state, row, col)
        if conflict_count < min_conflict_count:
            min_conflict_count = conflict_count
            min_conflict_col = col
    return min_conflict_col

def print_solution(state):
    """Print the board with queens placed."""
    for row in range(len(state)):
        line = ""
        for col in range(len(state)):
            line += "Q" if state[row] == col else "."
        print(line)

if __name__ == "__main__":
    board_size = 4
    initial_board = initial_state(board_size)
    
    print("Initial Board:")
    print_solution(initial_board)

    solution = min_conflict(initial_board, max_steps=1000)

    if solution:
        print("\nSolution:")
        print_solution(solution)
    else:
        print("\nNo solution found within the given steps.")
