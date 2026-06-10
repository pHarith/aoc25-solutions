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
    
def check_accessible(matrix, num_check):
    """
    Return a list of (row, col) tuples representing the (row, col) coordinates of item
    in <matrix> that has <= <num_check> of the same item in the 8 surrounding tiles.
    """
    num_row, num_col = len(matrix), len(matrix[0])
    accessible = []

    for i in range(num_row):
        for j in range(num_col):
            if matrix[i][j] == PAPER_ROLL:
                count = 0
                for coord in adjacent_coordinates:
                    check_i, check_j = i + coord[0], j + coord[1]
                    if 0 <= check_i < num_row and 0 <= check_j < num_col:
                        if matrix[check_i][check_j] == PAPER_ROLL:
                            count += 1
                
                if count < num_check:
                    accessible.append((i, j))

    return accessible


def solve(input_file):
    """
    Produce the solution to Day 4: Printing Department
    """
    paper_diagram = read_paper_diagram(input_file)
    accessible_paper = check_accessible(paper_diagram, 4)
    return len(accessible_paper)

#### Helper Functions For Part 2 Goes Here (if any) ####


#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 4: Printing Department
    """
    return


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution is {solve(input)}.")