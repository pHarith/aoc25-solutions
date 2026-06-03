# Solution to Advent of Code 2025
# Day 1 : Secret Entrance

#### SUMMARY OF TASKS ####
# 1. Read the dial turns and convert them into a list of negative and positive integers
# 2. Add the integer turn value to the initial dial value, then apply modular 100. If it
# is pointing at 0 after the operation, add 1 to password.

LEFT = 'L'
RIGHT = 'R'
DIAL_SIZE = 100

#### Helper Functions Goes Here (if any) ####
def read_dial_turns(input_file):
    """
    Read text file of dial turns, classifying them as a left turn (negative) or a right turn (positive). Return a list of integers that represent these dial turns.
    """
    dial_turns = []
    with open(input_file, "r") as dial_files:
        for turn in dial_files:
            direction, value = turn[0], int(turn[1:])
            if direction == LEFT:
                # Set left/counterclockwise as negative integers
                dial_turns.append(value * -1)
            elif direction == RIGHT:
                dial_turns.append(value)
            else:
                raise ValueError("Incorrect Content found in File Read.")
    return dial_turns
            


def solve(input_file):
    """
    Produce the solution to Day 1 : Secret Entrance
    """
    password = 0 # Initialize the password to 0
    dial_value = 50 # Initialize the dial to 50
    dial_turns = read_dial_turns(input_file)

    for turn in dial_turns:
        # Compute the new value pointed at the dial
        dial_value += turn
        dial_value %= DIAL_SIZE # Apply modular to prevent overflow
        if dial_value == 0:
            password += 1   # Increase the count of 0 being pointed after a turn
    return password

#### Helper Functions For Part 2 Goes Here (if any) ####


#### SUMMARY OF TASKS (PART 2) ####
# 1. Compute the number of turns to get to 0 (if possible)
# 2. Compute the number of zeroes pointed at by:
# Subtract the number of turns to the first 0 from the total number of turns
# Divide that by the dial size to see how many times it can loop around 0
# Add 1 at the end to account for the first 0 we reached

#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 1 : Secret Entrance
    """
    password = 0 # Initialize the password to 0
    init_dial = 50 # Initialize the dial to 50
    dial_turns = read_dial_turns(input_file)

    for turns in dial_turns:
        # Compute the new dial value
        new_dial = init_dial + turns
        new_dial %= DIAL_SIZE

        if turns > 0:   # Right turns, compute number of right turns to get to 0
            turns_to_zero = DIAL_SIZE - init_dial
        elif turns < 0: 
            # Left turns, turns the same number of times as its initial value 
            # or 100 if it is currently point at 0
            turns_to_zero = init_dial if init_dial != 0 else 100

        # The dial will only point at 0 at some point if the number of turns exceeds
        # the number of turns needed to reach zero from its position
        if abs(turns) >= turns_to_zero:
            # Compute the number of zeroes pointed at while turning the dial
            num_zeros = ((abs(turns) - turns_to_zero) // DIAL_SIZE) + 1
            password += num_zeros
        init_dial = new_dial
    return password


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution to part 1 is {solve(input)}.")
    print(f"The solution to part 2 is {solve_part2(input)}.")
