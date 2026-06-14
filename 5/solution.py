# Solution to Advent of Code 2025
# Day 5: CafeteriaDay 5: Cafeteria

#### SUMMARY OF TASKS ####
# 1. Read the ranges into a list of tuples and the available items' ids into a list
# 2. Iterate through items' ids list - see if an id is in range(range_start, range_end)
# 3. Return a list of items whose id fall into any ranges


#### Helper Functions Goes Here (if any) ####
def read_file(input_file):
    """
    Return a list of tuples and a list of integers.
    """
    with open(input_file, "r") as file:
        ranges, items = file.read().split('\n\n')

    return [tuple(int(i) for i in id.split('-')) for id in ranges.split('\n')], [int(item) for item in items.split('\n')]

def solve(input_file):
    """
    Produce the solution to Day 5: Cafeteria
    """
    fresh = []

    ranges, items = read_file(input_file)

    for id in items:
        for start, end in ranges:
            if id in range(start, end + 1) and id not in fresh:
                fresh.append(id)
    return len(fresh)

#### SUMMARY OF TASKS (Part 2) ####
# 1. Sort the id ranges from smallest start to largest start
# 2. Construct a new list to keep merged ranges, append new ranges
# 3. For each subsequent range, check if the start of the current 
# range is less than the end of the previous range to detect overlap
# 4. Update the range by changing the end of the max of (current_end, previous_end)
# 5. If not, we have moved out of overlap territory - append the new range and repeat
# 3. Return the sum of the numbers of ids in each range 
# NOTE: num_of_ids_in_range = end + 1 - start

#### Helper Functions For Part 2 Goes Here (if any) ####

#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 5: Cafeteria
    """
    # Omit list of available ids
    ranges, _ = read_file(input_file)

    merged_ranges = []

    # Sort the ranges
    ranges.sort()

    # Construct a new list of merged ranges
    for start, end in ranges:
        if merged_ranges == []:
            merged_ranges.append((start, end))
            continue
        
        # Grab the previous range in merged list
        last_start, last_end = merged_ranges[-1]

        if start <= last_end + 1:   # Overlap is found
            # Update the end of the range
            last_end = max(last_end, end)   
            merged_ranges[-1] = (last_start, last_end)
        else:
            # No overlap, append the new range
            merged_ranges.append((start, end))
    
    # Return the sum of number of ids in each range
    return sum([end + 1 - start for start, end in merged_ranges])


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution to part 1 is {solve(input)}.")
    print(f"The solution to part 2 is {solve_part2(input)}.")