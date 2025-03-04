import sys

def get_text_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def parse_input(map_input):
    return [[int(cell) for cell in line] for line in map_input.strip().split("\n")]


def find_trailheads(grid):
    trailheads = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                trailheads.append((r, c))
    return trailheads


def is_valid_step(grid, current, next_step):
    rows, cols = len(grid), len(grid[0])
    r, c = next_step
    if 0 <= r < rows and 0 <= c < cols and grid[next_step[0]][next_step[1]] == grid[current[0]][current[1]] + 1:
        return True
    return False


def calculate_rating(grid, start):
    from collections import defaultdict

    stack = [(start, [])]
    trail_count = defaultdict(set)

    while stack:
        current, path = stack.pop()
        r, c = current

        path = path + [current]

        if grid[r][c] == 9:
            trail_count[current].add(tuple(path))

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_step = (r + dr, c + dc)
            if is_valid_step(grid, current, next_step):
                stack.append((next_step, path))

    return sum(len(paths) for paths in trail_count.values())


def calculate_total_ratings(grid):
    trailheads = find_trailheads(grid)
    total_rating = sum(calculate_rating(grid, trailhead) for trailhead in trailheads)
    return total_rating

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        text = get_text_from_file(file_path)
        grid = parse_input(text)
        result = calculate_total_ratings(grid)
        print(f"La somme des scores de tous les points de départ est : {result}")