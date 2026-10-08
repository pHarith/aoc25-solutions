# Solution to Advent of Code 2025
# Day 10: Factory

ON = "#"
OFF = "."

from itertools import combinations
from collections import Counter

import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

#### Helper Functions Goes Here (if any) ####
def read_input(input):
    light_diagrams, buttons, joltages = [], [], []

    with open(input, "r") as config:
        for line in config:
            line_lst = line.strip().split()

            ld, bt, jt = line_lst[0], line_lst[1:-1], line_lst[-1]
            light_diagrams.append(ld[1:-1])
            buttons.append([num[1:-1] for num in bt])
            joltages.append(jt[1:-1])

    return light_diagrams, buttons, joltages

def solve(input_file):
    """
    Produce the solution to Day 10: Factory
    """
    lowest_btn_presses = []
    light_diagrams, buttons, _ = read_input(input_file)
    for i in range(len(light_diagrams)):
        # Flag if lowest button pressed has been found
        found_lowest = False

        # Initialize a map to represent the end state of the indicator lights
        switch_map = {i:(int(k==ON)) for i, k in enumerate(light_diagrams[i])}

        # Iterate through the number of button pressed
        for j in range(len(buttons[i])):
            for config in list(combinations(buttons[i], j)):

                # Count the number of times each light is switched
                count = Counter(int(num) for button in config for num in button.split(','))

                # Find the end state of the combination of button pressed
                test_map = {k:count[k] % 2 for k in range(len(light_diagrams[i]))}

                # Check if endstate matches with desired endstate
                if switch_map == test_map:
                    lowest_btn_presses.append(j)
                    found_lowest = True
                    break

            if found_lowest:
                break
                    
    # Return the sum of lowest number of button pressed across all lights
    return sum(lowest_btn_presses)

#### Helper Functions For Part 2 Goes Here (if any) ####


#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 10: Factory
    """

    lowest_btn_presses = []

    _, buttons, joltages = read_input(input_file)

    for i in range(len(buttons)):
        btns, jolts = [[int(b) for b in btn.split(',')] for btn in buttons[i]], [int(jolt) for jolt in joltages[i].split(',')]

        # Initialize empty matrix for all the linear equations
        A = [[0] * len(btns) for _ in range(len(jolts))] 

        # Iterate through each button, check which button 
        # affects which light and update the equation
        for j in range(len(btns)):
            for char in btns[j]:
                A[char][j] = 1

        cost = np.array([1] * len(btns)) 
        A = np.array(A)
        target = np.array(jolts)

        # Solve for lowest using mixed-integer linear programming
        lowest = milp(
            cost,
            constraints=LinearConstraint(A, target, target),  
            integrality=np.ones(len(btns)),                           
            bounds=Bounds(0, np.inf),                         
        )

        # extract the total number of button pressed for the lowest presses
        lowest_btn_presses.append(lowest.fun)

    # Return the sum of lowest number of button pressed across all lights
    return sum(lowest_btn_presses)


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'

    print(f"The solution to part 1 is {solve(input)}.")
    print(f"The solution to part 2 is {solve_part2(input)}.")