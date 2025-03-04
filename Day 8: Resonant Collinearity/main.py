import sys
from itertools import combinations
from math import gcd

def get_text_from_file(filePath):
    with open(filePath, "r") as file:
        return file.read()


def load_grid_from_text(text):
    return [list(line) for line in text.split("\n")]


def count_antinode_locations(grid):
    antennas = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.': #and cell != '#':
                antennas.append((x, y, cell))

    antinodes = set()

    for i in range(len(antennas)):
        for j in range(i + 1, len(antennas)):
            x1, y1, freq1 = antennas[i]
            x2, y2, freq2 = antennas[j]

            if freq1 == freq2:
                dx, dy = x2 - x1, y2 - y1

                antinode1 = (x1 - dx, y1 - dy)
                antinode2 = (x2 + dx, y2 + dy)

                for ax, ay in [antinode1, antinode2]:
                    if 0 <= ax < len(grid[0]) and 0 <= ay < len(grid):
                        antinodes.add((int(ax), int(ay)))

    for antinode in antinodes:
        grid[antinode[1]][antinode[0]] = "#"

    return len(antinodes), grid

def count_resonant_antinode_locations(grid):
    antennas = []
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell != '.':
                antennas.append((x, y, cell))

    def direction(dx, dy):
        if dx == 0 and dy == 0:
            return (0, 0)
        g = gcd(dx, dy)
        return (dx // g, dy // g)

    antinodes = set()
    antenna_by_freq = {}

    for x, y, freq in antennas:
        if freq not in antenna_by_freq:
            antenna_by_freq[freq] = []
        antenna_by_freq[freq].append((x, y))


    for freq, freq_antennas in antenna_by_freq.items():
        for a1, a2 in combinations(freq_antennas, 2):
            x1, y1 = a1
            x2, y2 = a2
            dx, dy = x2 - x1, y2 - y1
            dir_vector = direction(dx, dy)

            in_line = set()
            for ax, ay in freq_antennas:
                dx, dy = ax - x1, ay - y1
                if direction(dx, dy) == dir_vector:
                    in_line.add((ax, ay))

            antinodes.update(in_line)

            for factor in range(-len(grid) * len(grid[0]), len(grid) * len(grid[0])):
                nx, ny = x1 + factor * dir_vector[0], y1 + factor * dir_vector[1]
                if 0 <= nx < len(grid[0]) and 0 <= ny < len(grid):
                    antinodes.add((nx, ny))

    return len(antinodes)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        text = get_text_from_file(file_path)
        #print(text)
        grid = load_grid_from_text(text)
        # antinodes, grid = count_antinode_locations(grid)
        antinodes = count_resonant_antinode_locations(grid)
        print(f"{antinodes} antinode locations found.")
        #for line in grid:
        #    print("".join(line))
