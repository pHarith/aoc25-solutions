# Solution to Advent of Code 2025
# Day 6: Trash Compactor

#### SUMMARY OF TASKS ####
# 1. Read the math problems from file into a nested list of numbers involved and the list of operations
# 2. For each column, grab the all the numbers from the same column and the corresponding operation 
# to compute
# 3. Store the results into a list. Return the sum of said list.

from math import prod


#### Helper Functions Goes Here (if any) ####
def read_math_problem(input_file):
    with open(input_file, "r") as f:
        math_problem = [s.strip().split() for s in f.readlines()]
    
    # Operations are always the last row in the file
    return [[int(num) for num in num_lst] for num_lst in math_problem[:-1]], math_problem[-1]


def perform_operation(lst, opr):
    match opr:
        case '+':
            return sum(lst)
        case '*':
            return prod(lst)

def solve(input_file):
    """
    Produce the solution to Day 6: Trash Compactor
    """
    results = []

    nums, ops = read_math_problem(input_file)
    
    column_nums = list(zip(*nums))
    print(column_nums)

    for i in range(len(ops)):
        results.append(perform_operation(column_nums[i], ops[i]))
    
    return sum(results)

#### Helper Functions For Part 2 Goes Here (if any) ####


#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 6: Trash Compactor
    """
    return


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution is {solve(input)}.")