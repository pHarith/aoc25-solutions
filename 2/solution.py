# Solution to Advent of Code 2025
# Day 2: Gift Shop

#### SUMMARY OF TASKS ####
# 1. Read ID ranges into a list of tuples
# 2. Iterate through each and find "invalid IDs" and store them in a list:
# - Check if they are of even length 
# - Check if the first half = 2nd half via list slicing
# 3. Return the sum of those invalid IDs


#### Helper Functions Goes Here (if any) ####

def read_id_range(input_file):
    """
    Return a list of tuples (first_id, last_id) from input text file.
    """
    id_range = []

    with open(input_file, "r") as id_file:
        ids = id_file.read().strip().split(',')

        for id in ids:
            first_id, last_id = id.strip().split('-')
            try:
                id_range.append((int(first_id), int(last_id)))
            except ValueError:
                raise ValueError("Incorrect value found in input_file. Expected int-int, int-int,....,int-int.")
    return id_range


def find_invalid_ids(first_id, last_id):
    invalids = []

    for id in range(first_id, last_id + 1):
        id_str = str(id)
        id_len = len(id_str)

        if id_len % 2 == 0:

            if id_str[:id_len // 2] == id_str[id_len // 2:]:
                invalids.append(id)
    return invalids

def solve(input_file):
    """
    Produce the solution to Day 2: Gift Shop
    """
    invalid_ids = []

    id_range = read_id_range(input_file)
    
    for first_id, last_id in id_range:
        invalid_ids.extend(find_invalid_ids(first_id, last_id))

    return sum(invalid_ids)

#### Helper Functions For Part 2 Goes Here (if any) ####


#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 2: Gift Shop
    """
    return


if __name__ == "__main__":
    input = 'input.txt'
    #input = 'test.txt'
    print(f"The solution to part 1 is {solve(input)}.")