# Solution to Advent of Code 2025
# Day 4: Printing Department

#### SUMMARY OF TASKS ####
# 1. Read the grid into a matrix 
# 2. Traverse through each matrix element, check the 8 adjacent tiles (if available) 
# 3. Increment a counter and if count <= 4, append into a list of viable paper rolls


#### Helper Functions Goes Here (if any) ####

adjacent_coordinates = [(0, 1), (0, -1), (1, 1), (-1, -1), (1, 0), (-1, 0), (1, -1), (-1, 1)]
PAPER_ROLL = "@"


def read_paper_diagram(input_file):
    """
    Return a nested list from reading <input_file>.
    """
    with open(input_file) as paper_diagram:
        return [list(item for item in line) for line in paper_diagram.read().split()]
    
# Helper to print out the diagram for sanity check
def print_paper_diagram(matrix):
    for row in matrix:
        print("".join(row))
    
    
def is_accessible(row, col, matrix, num_check):
    """
    Return if matrix[row][col] is an accessible paper roll.
    """
    num_row, num_col = len(matrix), len(matrix[0])
    count = 0

    # Out of bounds check
    if not (0 <= row < num_row and 0 <= col < num_col):
        return False

    # Paper roll check
    if matrix[row][col] != PAPER_ROLL:
        return False

    # Iterate through each of the 8 adjacent tiles, check if it is a paper roll
    for coord in adjacent_coordinates:
        check_row, check_col = row + coord[0], col + coord[1]
        if 0 <= check_row < num_row and 0 <= check_col < num_col:
            if matrix[check_row][check_col] == PAPER_ROLL:
                count += 1
    
    return count < num_check 


def check_accessible(matrix, num_check):
    """
    Return a list of (row, col) tuples representing the (row, col) coordinates of item
    in <matrix> that has <= <num_check> of the same item in the 8 surrounding tiles.
    """
    num_row, num_col = len(matrix), len(matrix[0])
    accessible = []

    for row in range(num_row):
        for col in range(num_col):               
            if is_accessible(row, col, matrix, num_check):
                accessible.append((row, col))
    return accessible


def solve(input_file):
    """
    Produce the solution to Day 4: Printing Department
    """
    paper_diagram = read_paper_diagram(input_file)
    accessible_paper = check_accessible(paper_diagram, 4)
    return len(accessible_paper)


#### SUMMARY OF TASKS  (Part 2) ####
# 1. Add on top of solution from part 1, find accessible papers first
# 2. Make a queue of accessible, while queue is not empty, pop the first element -> convert into '.'
# 3. Check adjecent tiles if they are accessible, add them to the queue

#### Helper Functions For Part 2 Goes Here (if any) ####
def check_removable(matrix, num_check):
    """
    Return a list of (row, col) tuples representing the (row, col) coordinates of item
    in <matrix> that has <= <num_check> of the same item in the 8 surrounding tiles.
    """
    accessibles = check_accessible(matrix, num_check)
    mtx = matrix.copy()

    removables = accessibles.copy()

    while removables:
        row, col = removables.pop()
        
        mtx[row][col] = '.'

        for coord in adjacent_coordinates:
            check_row, check_col = row + coord[0], col + coord[1]
            if is_accessible(check_row, check_col, mtx, num_check) and (check_row, check_col) not in accessibles:
                removables.append((check_row, check_col))
                accessibles.append((check_row, check_col))
    return accessibles

    


#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 4: Printing Department
    """
    paper_diagram = read_paper_diagram(input_file)
    removable_paper = check_removable(paper_diagram, 4)
    return len(removable_paper)


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution to part 1 is {solve(input)}.")

    print(f"The solution to part 2 is {solve_part2(input)}.")