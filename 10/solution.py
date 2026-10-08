# Solution to Advent of Code 2025
# Day 10: Factory


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

            print(light_diagrams, buttons, joltages)

    return light_diagrams, buttons, joltages

def solve(input_file):
    """
    Produce the solution to Day 10: Factory
    """
    input = read_input(input_file)
    return

#### Helper Functions For Part 2 Goes Here (if any) ####


#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 10: Factory
    """
    return


if __name__ == "__main__":
    #input = 'input.txt'
    input = 'test.txt'


    print(f"The solution to part 1 is {solve(input)}.")
    print(f"The solution to part 2 is {solve_part2(input)}.")