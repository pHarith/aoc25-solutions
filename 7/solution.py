# Solution to Advent of Code 2025
# Day 7: Laboratories

#### SUMMARY OF TASKS ####
# 1. Read the teleportation board
# 2. Grabbing the start coordinates 


# Global Variables
START = "S"
SPLITTER = "^"

#### Helper Functions Goes Here (if any) ####

def read_board(input_file):
    """
    Read a board of m row x n cols into a matrix.
    """
    with open(input_file, "r") as file:
        return [[space for space in row.strip()] for row in file]

def find_start(board):
    num_rows, num_cols = len(board), len(board[0])
    
    # TODO: Return the row, col of the start object (S)
    for row in range(num_rows):
        for col in range(num_cols):
            if board[row][col] == START:
                return (row, col)

    return (-1, -1)

def split_count(board):
    num_rows, num_cols = len(board), len(board[0])
    split_count = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if board[row][col] == SPLITTER:
                split_count += 1

    return split_count



def solve(input_file):
    """
    Produce the solution to Day 7: Laboratories 
    """
    def is_in_bounds(cell):
        return (0 <= cell[0] < num_rows) and (0 <= cell[1] < num_cols)


    # TODO: return the number of times the tachyon beam is split
    board = read_board(input)
    start = find_start(board)

    num_rows, num_cols = len(board), len(board[0])
    to_visit = [start]
    split_occurences = []

    while to_visit:
        curr = to_visit.pop()

        next = (curr[0] + 1, curr[1])

        if is_in_bounds(next):
            to_visit.append(next)
            
            if board[next[0]][next[1]] == SPLITTER:
                
                to_visit.pop()

                split = (curr, next)

                if split not in split_occurences:
                    split_occurences.append(split)
                    to_visit.extend([(next[0], next[1] + 1), (next[0], next[1] - 1)])
                    
    return len(split_occurences)

#### Helper Functions For Part 2 Goes Here (if any) ####


#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 7: Laboratories
    """
    return


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution is {solve(input)}.")