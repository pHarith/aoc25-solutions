# Solution to Advent of Code 2025
# Day 8: Playground

#### SUMMARY OF TASKS ####
# 1. 
# 2. 

PAIR_LIMIT = 1000
TEST_LIMIT = 10

import numpy as np

from math import sqrt, prod

#### Helper Functions Goes Here (if any) ####
def read_coordinates(input_file):
    with open(input_file, "r") as file:
        return [tuple(int(value) for value in line.strip().split(',')) for line in file]

# Numpy Implementation
def find_euclidean_distance(coord1, coord2):
    a1, a2 = np.array(coord1), np.array(coord2)
    return np.linalg.norm(a2 - a1)

# Math.sqrt implementation
def find_euclidean_distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

# Function to match all possible coordinates
def find_euc_dist_all(coords):
    """
    Return a list of euclidean distances between any two pairs of coordinates.
    """
    euc_dist_lst = []

    for i, coord1 in enumerate(coords):
        for coord2 in coords[i+1:]:
            euc_dist_lst.append((find_euclidean_distance(coord1, coord2), coord1, coord2))
    return euc_dist_lst

def solve(input_file):
    """
    Produce the solution to Day 8: Playground
    """
    coords = read_coordinates(input_file)
    sorted_distances = find_euc_dist_all(coords)
    sorted_distances.sort()

    groups = []
    groups_size = []
    

    for i in range(TEST_LIMIT):
        _, coord1, coord2 = sorted_distances[i]
        
        coord1_group, coord2_group = None, None
        
        for i in range(len(groups)):
            if coord1 in groups[i]:
                coord1_group = i
            
            if coord2 in groups[i]:
                coord2_group = i

        if coord1_group is not None and coord1_group == coord2_group:
            continue
        
        # groups is empty or both coordinates make a new set
        if coord1_group is None and coord2_group is None:
            groups.append({coord1, coord2})

            # Append the most recently added group into the size list
            groups_size.append(2)
            
        # first coordinate is part of an existing set but group 2 is not
        elif coord1_group is not None and coord2_group is None:
            groups[coord1_group].add(coord2)
            groups_size[coord1_group] += 1

        # first coordinate is part of an existing set but group 2 is not
        elif coord1_group is None and coord2_group is not None:
            groups[coord2_group].add(coord1)
            groups_size[coord2_group] += 1
    
    groups_size.sort()
    print(groups)
    print(groups_size)
    return prod(groups_size[:3])

#### Helper Functions For Part 2 Goes Here (if any) ####


#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 8: Playground
    """
    return 


if __name__ == "__main__":
    # input = 'input.txt'
    input = 'test.txt'
    print(f"The solution to part 1 is {solve(input)}.")