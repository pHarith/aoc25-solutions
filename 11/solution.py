# Solution to Advent of Code 2025
# Day 11: Reactor

#### Helper Functions Goes Here (if any) ####

def read_file(input_file):

    config_map = {}

    with open(input_file) as file:
        for line in file:
            input_device, output_devices = line.strip().split(':')
            config_map[input_device] = output_devices.strip().split()

    return config_map


def find_all_paths(start, end, graph):

    all_paths = []
    path = [start]
    visited = {start}


    def dfs(node):

        if node == end:
            all_paths.append(path.copy())
            return

        for child in graph.get(node, []):
            if child not in visited:
                visited.add(child)
                path.append(child)

                # Recursive call on child (until reaching end)
                dfs(child)

                # Reset path and visited when moving onto a different child
                path.pop()
                visited.remove(child)

    dfs(start)
    return all_paths

            


def solve(input_file):
    """
    Produce the solution to Day 11: Reactor
    """

    start, end = "you", "out"
    device_map = read_file(input_file)

    print(device_map)
    print(device_map.get("you", []))

    return len(find_all_paths(start, end, device_map))

#### Helper Functions For Part 2 Goes Here (if any) ####


#### Part 2 Goes Here ####
def solve_part2(input_file):
    """
    Produce the solution to part 2 of Day 11: Reactor 
    """
    return


if __name__ == "__main__":
    input = 'input.txt'
    # input = 'test.txt'
    print(f"The solution to part 1 is {solve(input)}.")
    print(f"The solution to part 2 is {solve_part2(input)}.")