# Solution to Advent of Code 2025
# Day 3: Lobby

#### SUMMARY OF TASKS ####
# 1. Read the jotage strings into a list
# 2. Knowing they are made up of single digits, find the largest value in string and stores its index. 
# 3. Find the largest value after the largest's index.
# 4. Save each's bank largest joltage into a list, return the sum.



#### Helper Functions Goes Here (if any) ####

def read_batteries_banks(input_file):
    """
    Return a list of strings of integers representing battery banks.
    """
    with open(input_file) as battery_file:
        return battery_file.read().strip().split('\n')
    

def find_max_joltage(battery_bank, num_digits):
    """
    Giving a battery_bank string, return the largest <num_digits>-digits joltage
    that can be produced.

    <num_digits> must be less than the length of battery_bank.
   
    >>> find_max_joltage("811111111111119", 2)
    89
    >>> find_max_joltage("234234234234278", 12)
    434234234278
    """
    battery_len = len(battery_bank)

    if num_digits > battery_len:
        raise ValueError(f"Expected: num_digits < len(battery_bank). Found {num_digits = } > {battery_len}")
    
    largest_batteries = []
    battery_lst = list(battery_bank)

    start, remaining = 0, num_digits

    while remaining > 0:
        # Set an end point for list slicing to ensure there are enough digits left
        end = battery_len - remaining

        # Slice a section of batteries to find max value 
        curr_section = battery_lst[start: end + 1]
        max_battery = max(curr_section)
        max_index = curr_section.index(max_battery)

        # Append to max value battery to the list
        largest_batteries.append(max_battery)

        # Update loop conditions 
        start += (max_index + 1)    # Iterate from the next index after max
        remaining -= 1              # Decrenent the number of digits need to form the max joltage

    return int("".join(largest_batteries))


def solve(input_file, num_digits):
    """
    Produce the solution to Day 3: Lobby
    """
    max_joltages = []

    battery_banks = read_batteries_banks(input_file)

    for battery_bank in battery_banks:
        max_joltages.append(find_max_joltage(battery_bank, num_digits))

    return sum(max_joltages)


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution to part 1 is {solve(input, num_digits = 2)}.")
    print(f"The solution to part 2 is {solve(input, num_digits = 12)}.")