# Solution to Advent of Code 2025
# Day 9: Movie Theate

#### SUMMARY OF TASKS ####
# 1. Read the list of (x, y) coordinates of the theatre
# 2. Calculate the area of rectangle between any 2 coordinates
# 3. Return max(list_of_rectangle_areas)

#### Helper Functions Goes Here (if any) ####
def compute_rect_area(coord1, coord2):
    # Add 1 to length and width as the end points are included
    return (abs(coord1[0] - coord2[0]) + 1) * (abs(coord1[1] - coord2[1]) + 1)

def find_rect_area_all(coords):
    """
    Return a list of euclidean distances between any two pairs of coordinates.
    """
    rect_area_lst = []

    for i, coord1 in enumerate(coords):
        for coord2 in coords[i+1:]:
            rect_area_lst.append((compute_rect_area(coord1, coord2), coord1, coord2))
    return rect_area_lst


def read_red_theatre_tiles(input_file):
    """
    
    """
    with open(input_file, "r") as theatre_coordinates:
        return [tuple([int(i) for i in coord.strip().split(',')]) for coord in theatre_coordinates.read().split('\n')]

def solve(input_file):
    """
    Produce the solution to Day 9: Movie Theate
    """
    red_tiles = read_red_theatre_tiles(input_file)

    rectangle_areas = find_rect_area_all(red_tiles)

    return max(rectangle_areas)[0]

#### SUMMARY OF TASKS (Part 2) ####
# 1. Use the red tiles to form green tiles (at least the borders)
# 2. Fill in the inner tiles as green and a build a grid of valid/invalid tiles
# 3. 

#### Helper Functions For Part 2 Goes Here (if any) ####
def find_green_boundary(red_tiles):
    """
    Returns a list of coordinates representing green tiles in the theatre board
    that forms a bridge between adjacent red tiles.
    """
    green_tiles = []
    for i in range(len(red_tiles)):
        next = i + 1 if i + 1 != len(red_tiles) else 0
        curr_x, curr_y = red_tiles[i]
        next_x, next_y = red_tiles[next]
        
        # Fill in green tiles boundary
        if curr_x - next_x == 0:
            # NOTE: Add + 1 to start to exclude red tiles
            for y in range(min(curr_y, next_y) + 1, max(curr_y, next_y)):
                green_tiles.append((curr_x, y))
        if curr_y - next_y == 0:
            for x in range(min(curr_x, next_x) + 1, max(curr_x, next_x)):
                green_tiles.append((x, curr_y)) 
            
    return green_tiles




    return green_tiles

def find_interior_green(boundary):
    # Find the smallest rectangular search zone on that board 
    # that contains the red-green boundary
    max_x = max(x for x, _ in boundary)
    min_x = min(x for x, _ in boundary)

    max_y = max(y for _, y in boundary)
    min_y = min(y for _, y in boundary)

    # These four forms the corners of the search zone

    def inside_search_zone(tile):
        '''
        Returns if a tile is within the rectangular search zone.
        '''
        return min_x - 1 <= tile[0] < max_x + 1 and min_y - 1 <= tile[1] < max_y + 1

    # Inner function to root out tiles outside the red-green boundary
    def bfs():
        visited = set()
        exterior = set()

        # start from outside the bound, top-left first
        start = (min_x - 1, min_y - 1)
        queue = [start]
        visited.add(start)

        while queue:
            curr = queue.pop(0)

            if inside_search_zone(curr):
                if curr not in boundary:
                    exterior.add(curr)
            else: # Stop the search
                continue

            for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
                next_tile = (curr[0] + dx, curr[1] + dy)
                # check bounds: next_tile within [min_x-1, max_x+1] and [min_y-1, max_y+1]
                if inside_search_zone(next_tile):
                    if next_tile not in visited and next_tile not in boundary:
                        visited.add(next_tile)
                        queue.append(next_tile)
        
        return exterior

    green_tiles = []
    exterior = bfs()

    for x in range(min_x, max_x+1):
        for y in range(min_y, max_y+1):
            # (x, y) can only be an interior green tile if (x, y) is:
            # 1. not on the boundary 
            # 2. not part of the exterior
            if (x, y) not in boundary and (x, y) not in exterior:
                green_tiles.append((x, y))
    return green_tiles

def find_largest_rectangle(red_tiles, valid_tiles):
    max_area = 0

    return max_area

#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 9: Movie Theate
    """
    red_tiles = read_red_theatre_tiles(input_file)
    green_boundary = find_green_boundary(red_tiles)

    internal_green_tiles = find_interior_green(red_tiles + green_boundary)
    valid_tiles = red_tiles + green_boundary + internal_green_tiles 

    print(len(red_tiles), len(green_boundary), len(internal_green_tiles), len(valid_tiles))
    return find_largest_rectangle(red_tiles, valid_tiles)


if __name__ == "__main__":
    # input = 'input.txt'
    input = 'test.txt'
    print(f"The solution to part 1 is {solve(input)}.")
    print(f"The solution to part 2 is {solve_part2(input)}.")