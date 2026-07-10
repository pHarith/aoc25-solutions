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

def solve(input_file, limit):
    """
    Produce the solution to Day 8: Playground
    """
    # Grab coordinates and compute distances between pairs
    coords = read_coordinates(input_file)
    sorted_distances = find_euc_dist_all(coords)

    # Sort the distances in ascending order
    sorted_distances.sort()

    # List to store circuits
    circuits = []

    # List to store size of each circuit of the same index
    circuits_size = []
    
    for i in range(limit):
        _, coord1, coord2 = sorted_distances[i]

        # Initialize the circuit they are a part of
        coord1_circuit, coord2_circuit = None, None
        
        # Update their circuits (if already in a circuit)
        for j in range(len(circuits)):
            if coord1 in circuits[j]:
                coord1_circuit = j
            
            if coord2 in circuits[j]:
                coord2_circuit = j

        # Both coordinates exists in the same circuit
        if coord1_circuit is not None and coord1_circuit == coord2_circuit:
            continue
        
        # circuits is empty or both coordinates make a new set
        if coord1_circuit is None and coord2_circuit is None:
            circuits.append({coord1, coord2})

            # Append the most recently added circuit into the size list
            circuits_size.append(2)

        # first coordinate is not part of an existing circuit set but 
        # second coordinate is
        elif coord1_circuit is None and coord2_circuit is not None:
            circuits[coord2_circuit].add(coord1)
            circuits_size[coord2_circuit] += 1

        # first coordinate is part of an existing circuit set but 
        # second coordinate is not
        elif coord1_circuit is not None and coord2_circuit is None:
            circuits[coord1_circuit].add(coord2)
            circuits_size[coord1_circuit] += 1

        # Both coordinates exist in different circuits
        elif coord1_circuit != coord2_circuit:
            # Merge curcuits into a single circuit
            circuits[coord1_circuit] = circuits[coord1_circuit].union(circuits[coord2_circuit])

            # Change the size of the newly merged circuit and remove the other circuit
            circuits_size[coord1_circuit] += circuits_size[coord2_circuit]
            circuits.pop(coord2_circuit)
            circuits_size.pop(coord2_circuit)
    
    circuits_size.sort(reverse=True)
    return prod(circuits_size[:3])

#### Helper Functions For Part 2 Goes Here (if any) ####


#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 8: Playground
    """
    # Grab coordinates and compute distances between pairs
    coords = read_coordinates(input_file)
    sorted_distances = find_euc_dist_all(coords)

    # Sort the distances in ascending order
    sorted_distances.sort()

    # List to store circuits
    circuits = []

    # List to store size of each circuit of the same index
    circuits_size = []

    i = 0
    while i < len(sorted_distances):
        _, coord1, coord2 = sorted_distances[i]

        i += 1

        # Initialize the circuit they are a part of
        coord1_circuit, coord2_circuit = None, None
        
        # Update their circuits (if already in a circuit)
        for j in range(len(circuits)):
            if coord1 in circuits[j]:
                coord1_circuit = j
            
            if coord2 in circuits[j]:
                coord2_circuit = j

        # Both coordinates exists in the same circuit
        if coord1_circuit is not None and coord1_circuit == coord2_circuit:
            continue
        
        # circuits is empty or both coordinates make a new set
        if coord1_circuit is None and coord2_circuit is None:
            circuits.append({coord1, coord2})

            # Append the most recently added circuit into the size list
            circuits_size.append(2)

        # first coordinate is not part of an existing circuit set but 
        # second coordinate is
        elif coord1_circuit is None and coord2_circuit is not None:
            circuits[coord2_circuit].add(coord1)
            circuits_size[coord2_circuit] += 1

        # first coordinate is part of an existing circuit set but 
        # second coordinate is not
        elif coord1_circuit is not None and coord2_circuit is None:
            circuits[coord1_circuit].add(coord2)
            circuits_size[coord1_circuit] += 1

        # Both coordinates exist in different circuits
        elif coord1_circuit != coord2_circuit:
            # Merge curcuits into a single circuit
            circuits[coord1_circuit] = circuits[coord1_circuit].union(circuits[coord2_circuit])

            # Change the size of the newly merged circuit and remove the other circuit
            circuits_size[coord1_circuit] += circuits_size[coord2_circuit]
            circuits.pop(coord2_circuit)
            circuits_size.pop(coord2_circuit)

        # Check if all every junction boxes go into a single circuit
        if len(circuits) == 1 and len(circuits[0]) == len(coords):
            # Return the product of x-coord of the two latest junction boxes
            return coord1[0] * coord2[0]
        
    # Connected all pairs and has not found a pair that causes all junction boxes to form a single larger circuit, return -1 to signal error
    return -1

if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution to part 1 is {solve(input, PAIR_LIMIT)}.")
    print(f"The solution to part 2 is {solve_part2(input)}.")