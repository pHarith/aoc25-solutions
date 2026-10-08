# Solution to Advent of Code 2025
# Day 9: Movie Theate

#### SUMMARY OF TASKS ####
# 1. Read the list of (x, y) coordinates of the theatre
# 2. Calculate the area of rectangle between any 2 coordinates
# 3. Return max(list_of_rectangle_areas)


directions = [(0,1), (0, -1), (1, 0), (-1, 0)]

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
def grab_notable_coordinates(red_tiles):
    all_xs, all_ys = set(), set()

    # Append the x, y of red tiles
    for x, y in red_tiles:
        all_xs.add(x)
        all_ys.add(y)

    # Pad out coordinates for grid fill
    x_pad_left, x_pad_right = min(all_xs) - 1, max(all_xs) + 1
    all_xs.add(x_pad_left)
    all_xs.add(x_pad_right)

    y_pad_left, y_pad_right = min(all_ys) - 1, max(all_ys) + 1
    all_ys.add(y_pad_left)
    all_ys.add(y_pad_right)

    return sorted(list(all_xs)), sorted(list(all_ys))


def coordinate_compression(all_xs, all_ys):

    # Inner function to assist in coordinate compression
    def fill_gaps(coordinates):
        """
        Return a copy of coordinates, with large gaps in between values being filled with
        a dummy number.
        e.g. [2, 7, 10] -> [2, 3, 7, 8, 10] where 3 and 8 are dummies
        """
        # Initialize an empty list
        expanded = []

        list_len = len(coordinates)

        # Iterate over the original list and the indices
        for i, coord in enumerate(coordinates):
            expanded.append(coord)

            # Check if out of bounds
            if i + 1 < list_len:

                # Check for gaps (adjacent coord differs by > 1)
                if coordinates[i + 1] > coord + 1:
                    expanded.append(coord + 1)  # Add a dummy number as a gap

        return expanded
    
    
    # Expand the xs and ys with dummies to account for gaps
    expanded_xs = fill_gaps(all_xs)
    expanded_ys = fill_gaps(all_ys)


    # Build a mapping dictionary
    xs_map, ys_map = {}, {}

    for i, x in enumerate(expanded_xs):
        xs_map[x] = i

    for i, y in enumerate(expanded_ys):
        ys_map[y] = i

    return xs_map, ys_map

def build_boolean_grid(xs_map, ys_map):
    """
    Initialize a boolean grid that represents compressed areas.
    True = the coordinate represents a valid tile.
    False = the coordinate represents an unvalid tile.
    """
    return [[False] * (len(xs_map)) for _ in range(len(ys_map))]

def compress_red_tiles(red_tiles, xs_map, ys_map, grid):
    compressed_red_tiles = []
    for x, y in red_tiles:
        compressed_x, compressed_y = xs_map[x], ys_map[y]
        compressed_red_tiles.append((compressed_x, compressed_y))
        grid[compressed_y][compressed_x] = True

    return compressed_red_tiles

def compress_green_tiles(compressed_red_tiles, grid):
    compressed_green_tiles = []

    red_tiles_len = len(compressed_red_tiles)

    for i in range(len(compressed_red_tiles)):
        next = i + 1 if i + 1 != red_tiles_len else 0
        curr_x, curr_y = compressed_red_tiles[i]
        next_x, next_y = compressed_red_tiles[next]

        section = []
        if curr_x - next_x == 0: # Vertical

            start, end = min(curr_y, next_y), max(curr_y, next_y)
            for y in range(start, end):
                grid[y][curr_x] = True
                section.append((curr_x, y))
            
        if curr_y - next_y == 0:  # Horizontal
            start, end = min(curr_x, next_x), max(curr_x, next_x)
            for x in range(start, end):
                grid[curr_y][x] = True
                section.append((x, curr_y))

        compressed_green_tiles.append(section)
            
    return compressed_green_tiles

def flood_fill_exterior(grid):
    start = (0, 0)
    visited = set()

    queue = [start]

    while queue:
        curr = queue.pop()

        # Check for out of bounds
        if not (0 <= curr[0] < len(grid[0]) and 0 <= curr[1] < len(grid)):
            continue

        # If tile already visited or is inside of the grid
        if curr in visited or grid[curr[1]][curr[0]]:
            continue

        for dir in directions:
            # Add in the 4 neighbors into the queue
            queue.append((curr[0] + dir[0], curr[1] + dir[1]))

        # Add tile to visited (this counts outside tiles)
        visited.add(curr)

    return visited

def fill_interior(grid, exterior):
    rows, cols = len(grid), len(grid[0])

    for y in range(rows):
        for x in range(cols):
            # Check if grid[y][x] is False which means either unlabeled or outside the polygon
            if not grid[y][x]: 
                # Check if the tile is not within the flood-filled exterior
                if (x, y) not in exterior:
                    # Set grid to True - valid tile inside polygon
                    grid[y][x] = True

    return

def is_valid_rectangle(grid, corner1, corner2, compressed_xs, compressed_ys):
    """
    Test if a rectangle generated by <corner1, corner2> is contained in valid <grid>
    tiles (green and red).
    """
    # Map corner1 and corner2 to the compressed coordinates
    compressed1 = (compressed_xs[corner1[0]], compressed_ys[corner1[1]])
    compressed2 = (compressed_xs[corner2[0]], compressed_ys[corner2[1]])


    # Find the leftmost, rightmost x values and uppermost and lowermost y values 
    # making the rectangle
    left = min(compressed1[0], compressed2[0])
    right = max(compressed1[0], compressed2[0])
    upper = min(compressed1[1], compressed2[1])
    lower = max(compressed1[1], compressed2[1])

    for x in range(left, right + 1):
        for y in range(upper, lower + 1):
            if grid[y][x] == False:
                #print(f"{corner1} and {corner2} produced one wrong spot {(x, y)}")
                return False

    return True
    

#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 9: Movie Theate
    """
    # Create a list of red tiles
    red_tiles = read_red_theatre_tiles(input_file)

    all_xs, all_ys = grab_notable_coordinates(red_tiles)

    compressed_xs, compressed_ys = coordinate_compression(all_xs, all_ys)

    grid = build_boolean_grid(compressed_xs, compressed_ys)

    compressed_red_tiles = compress_red_tiles(red_tiles, compressed_xs, compressed_ys, grid)
    compress_green_tiles(compressed_red_tiles, grid)

    exterior_region = flood_fill_exterior(grid)
    fill_interior(grid, exterior_region)

    max_rect_area = 0

    for i, coord1 in enumerate(red_tiles):
            for coord2 in red_tiles[i+1:]:
                if is_valid_rectangle(grid, coord1, coord2, compressed_xs, compressed_ys):
                    rect_area = compute_rect_area(coord1, coord2)
                    if rect_area > max_rect_area:
                        max_rect_area = rect_area

    return max_rect_area


if __name__ == "__main__":
    input = 'input.txt'
    #input = 'test.txt'
    print(f"The solution to part 1 is {solve(input)}.")
    print(f"The solution to part 2 is {solve_part2(input)}.")