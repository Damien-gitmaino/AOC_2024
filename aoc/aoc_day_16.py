import heapq
import sys

# Direction vectors and their rotations
DIRECTIONS = ['E', 'S', 'W', 'N']
DX = {'E': 0, 'W': 0, 'N': -1, 'S': 1}
DY = {'E': 1, 'W': -1, 'N': 0, 'S': 0}

def get_text_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def parse_maze(maze):
    start, end = None, None
    for i, row in enumerate(maze):
        for j, cell in enumerate(row):
            if cell == 'S':
                start = (i, j)
            elif cell == 'E':
                end = (i, j)
    return start, end


def heuristic(pos, end):
    return abs(pos[0] - end[0]) + abs(pos[1] - end[1])


def solve_maze(maze):
    start, end = parse_maze(maze)
    rows, cols = len(maze), len(maze[0])
    pq = []  # Priority queue for A*
    visited = set()

    # Initial state: (cost, x, y, direction)
    for initial_dir in DIRECTIONS:
        heapq.heappush(pq, (0, start[0], start[1], initial_dir))

    while pq:
        cost, x, y, direction = heapq.heappop(pq)

        if (x, y, direction) in visited:
            continue
        visited.add((x, y, direction))

        # Check if we've reached the end
        if (x, y) == end:
            return cost

        # Explore all possible actions
        # 1. Move forward
        nx, ny = x + DX[direction], y + DY[direction]
        if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#':
            heapq.heappush(pq, (cost + 1, nx, ny, direction))

        # 2. Rotate left or right
        current_dir_index = DIRECTIONS.index(direction)
        left_dir = DIRECTIONS[(current_dir_index - 1) % 4]
        right_dir = DIRECTIONS[(current_dir_index + 1) % 4]

        heapq.heappush(pq, (cost + 1000, x, y, left_dir))
        heapq.heappush(pq, (cost + 1000, x, y, right_dir))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        text = get_text_from_file(file_path)
        print(solve_maze(text))