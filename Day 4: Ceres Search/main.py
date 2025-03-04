def read_input(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]

def search_word(grid, word, x, y, dx, dy):
    for i in range(len(word)):
        nx, ny = x + i * dx, y + i * dy
        if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != word[i]:
            return False
    return True

def count_xmas(grid):
    # word = "XMAS"
    count = 0
    rows, cols = len(grid), len(grid[0])

    # directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]

    for y in range(rows):
        for x in range(cols):
            if grid[y][x] == 'M' or grid[y][x] == 'S':
                if x + 2 >= cols or y + 2 >= rows:
                    continue
                exam = [grid[y][x], grid[y+1][x+1], grid[y+2][x+2]]
                if exam == ['M', 'A', 'S'] or exam == ['S', 'A', 'M']:
                    if x + 2 >= cols and y + 2 >= rows:
                        continue
                    exam = [grid[y][x+2], grid[y+1][x+1], grid[y+2][x]]
                    if exam == ['M', 'A', 'S'] or exam == ['S', 'A', 'M']:
                        count += 1
            #for dx, dy in directions:
            #    if search_word(grid, word, i, j, dx, dy):
            #        count += 1

    return count

def main():
    grid = read_input('input.txt')
    result = count_xmas(grid)
    print(f"XMAS appears {result} times.")

if __name__ == "__main__":
    main()