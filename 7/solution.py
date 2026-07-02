# Solution to Advent of Code 2025
# Day 7: Laboratories

#### SUMMARY OF TASKS ####
# 1. Read the teleportation board
# 2. Grabbing the start coordinates 
# 3. Keep a list of nodes to visit and list of tuple of where split occurs
# 4. Traverse through nodes to visit, and pop off any nodes that are splitters 
# and add nodes to its left and right, until there are no nodes to visit
# 5. Return the length of all split lists


# Global Variables
START = "S"
SPLITTER = "^"
EMPTY = "."

#### Helper Functions Goes Here (if any) ####

def read_board(input_file):
    """
    Read a board of m row x n cols into a matrix.
    """
    with open(input_file, "r") as file:
        return [[space for space in row.strip()] for row in file]

def find_start(board):
    """
    Return the (row, column) of the START character on the board.
    Return -1 if not found.
    """
    
    for r, row in enumerate(board):
        for c, cell in enumerate(row):
            if cell == START:   
                # Return the coordinates of the cell with START
                return (r, c)

    raise ValueError("Start value not found in board.")

def solve(input_file):
    """
    Produce the solution to Day 7: Laboratories 
    """

    # Inner Helper Function to check if a cell is in bound of the board
    def is_in_bounds(cell):
        return (0 <= cell[0] < num_rows) and (0 <= cell[1] < num_cols)

    # Read the board into a matrix and get the coordinate of START
    board = read_board(input)
    start_row, start_col = find_start(board)

    num_rows, num_cols = len(board), len(board[0])

    # A list to track cells to visit and where splits occur
    to_visit = [(start_row, start_col)]
    split_occurences = []

    # Loop until there are no cells to visit
    while to_visit:
        # Remove visited cells
        curr = to_visit.pop()

        # Move downward
        next = (curr[0] + 1, curr[1])

        if is_in_bounds(next):
            # Visit in bound cell moved to
            to_visit.append(next)
            
            if board[next[0]][next[1]] == SPLITTER:
                # Cell is a splitter, remove cell from visit list 
                # as we cant move over a splitter
                to_visit.pop()

                # Store split as (cell_before_splitter, cell_with_splitter)
                split = (curr, next)

                if split not in split_occurences:
                    # New split - add to the list
                    split_occurences.append(split)

                    # Add cells to its left and right to be visited
                    to_visit.extend([(next[0], next[1] + 1), (next[0], next[1] - 1)])
                    
    return len(split_occurences)

#### SUMMARY OF TASKS (Part 2) ####
# 1. 
# 2. 
# 3.
# 4.


#### Helper Functions For Part 2 Goes Here (if any) ####




#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 7: Laboratories
    """
    
    def is_in_bounds(cell):
        """
        Inner Helper Function - return if cell is a valid coordinate in board
        """
        return (0 <= cell[0] < num_rows) and (0 <= cell[1] < num_cols)
    
    def dfs(row, col):
        """
        Inner Helper Function - Perform dfs starting from coordinate (row, col).
        Return the number of possible split timelines from (row, col) to the bottom of the board.
        """
        # Return 0 if the tile is out of bounds
        if not is_in_bounds((row, col)):
            return 0
        
        # Return 1 if the next move downwards is the end
        if row == num_rows - 1:     # last row
            return 1
        
        # This coordinate has been visited and the number of split timelines recorded
        if memo[row][col] != -1:
            return memo[row][col]
        
        # Tile is a splitter
        if board[row][col] == SPLITTER:
            # Split the particle into left and right respectively
            left = dfs(row, col - 1) if is_in_bounds((row, col - 1)) and board[row][col - 1] == EMPTY else 0
            right = dfs(row, col + 1) if is_in_bounds((row, col + 1)) and board[row][col + 1] == EMPTY else 0

            # Combine the number of split timelines
            result = left + right
        else:
            if is_in_bounds((row+1, col)):  # Tile is an empty slot
                result = dfs(row+1, col)    # Takes the result of the tile below it (they are on the same timeline)

        # Store the result in memoization matrix
        memo[row][col] = result
        return result

    # Read the board into a matrix and get the coordinate of START
    board = read_board(input)
    start = find_start(board)

    num_rows, num_cols = len(board), len(board[0])

    # Initialize a matrix of -1 to represent tiles on the board not visited
    # and store the number of split timelines starting from any (row, col)
    memo = [[-1] * num_cols for _ in range(num_rows)]
                    
    return dfs(*start)


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution to part 1 is {solve(input)}.")
    print(f"The solution to part 2 is {solve_part2(input)}.")