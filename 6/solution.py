# Solution to Advent of Code 2025
# Day 6: Trash Compactor

#### SUMMARY OF TASKS ####
# 1. Read the math problems from file into a nested list of numbers involved and the list of operations
# 2. For each column, grab the all the numbers from the same column and the corresponding operation 
# to compute
# 3. Store the results into a list. Return the sum of said list.

from math import prod
from itertools import zip_longest


#### Helper Functions Goes Here (if any) ####
def read_problem(input_file):
    """
    Read the input file and return a nested list of string numbers and a list of
    operators. 
    """
    with open(input_file, "r") as f:
        math_problem = [s.strip().split() for s in f.readlines()]
    
    # Operations are always the last row in the file
    return [[num for num in num_lst] for num_lst in math_problem[:-1]], math_problem[-1]

def nested_str_to_int(nested_lst):
    """
    Return a new list, where the string values in a nested list are converted into a integer values.

    >>> nested_str_to_int([['1', '23', '4'], ['56']])
    [[1, 23, 4], [56]]
    """
    return [[int(str) for str in sub_lst] for sub_lst in nested_lst]

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

    nums, ops = read_problem(input_file)
    
    column_nums = list(zip(*nums))

    column_nums = nested_str_to_int(column_nums)

    for i in range(len(ops)):
        results.append(perform_operation(column_nums[i], ops[i]))
    
    return sum(results)

#### Helper Functions For Part 2 Goes Here (if any) ####
#### SUMMARY OF TASKS (Part 2) ####
# 1. Read each row of numbers as one continuous string and return a list of the strings
# 2. Reconstruct the numbers by iterating through all the strings simultaneously
# - combine numbers in the same col and add them to a sub list
# - if all rows in the column are empty, add the sublist to the larger list 
# then move onto a new sublist

#### Part 2 Goes Here ####

def read_problem_part2(input_file):
    # NOTE: this can also be used for part 1, with a different converter function.
    with open(input_file, "r") as f:
        # Separte them into lines
        math_problem = [s for s in f.readlines()]

        # Separate the numbers and operators
        nums, ops = [[c for c in num.strip('\n')] for num in math_problem[:-1]], math_problem[-1].split()
    
    # Return the numbers as a list of strings (to be reconstructed later)
    return nums, ops

def convert_to_celaphod(lst):
    """
    Convert a math problem to celaphod system, reading from left to right 
    and top to bottom.
    """

    cel_lst = []

    num_cols = len(lst[0])

    i = num_cols - 1

    # Temporary sublist that stores a section of numbers matching an operator
    temp_lst = []

    # Iterate through all rows simulataneously
    while i >= 0: 
        # Reconstruct the number in the i-th column by combining all elements
        num = "".join(c[i] for c in lst).strip()
        if num == "":   # Empty string, move onto the next set of problem
            cel_lst.append(temp_lst)    # Add the sublist (a problem) to the larger list (of problems)
            temp_lst = []               # Empty the temp sublist
        else:   # Convert the number into integer and store it in the sublist
            temp_lst.append(int(num))
        i -= 1
    cel_lst.append(temp_lst)
    return cel_lst


def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 6: Trash Compactor
    """
    results = []

    nums, ops = read_problem_part2(input_file)
    
    column_nums = convert_to_celaphod(nums)

    # Flip the operators as we are reading from right to left
    ops = ops[::-1]

    for i in range(len(ops)):
        results.append(perform_operation(column_nums[i], ops[i]))
    
    return sum(results)


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution to part 1 is {solve(input)}.")
    print(f"The solution to part 2 is {solve_part2(input)}.")