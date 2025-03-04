import sys
from copy import deepcopy

player_symbole = ["^", ">", "v", "<"]

def get_text_from_file(filePath):
    with open(filePath, "r") as file:
        return file.read()

def format_map(text):
    map = text.split("\n")
    for i in range(len(map)):
        map[i] = list(map[i])
    return map

def get_coords_player(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] in player_symbole:
                return y, x, map[y][x]

def get_next_position(y, x, symbol):
    if symbol == '^':
        return y - 1, x
    elif symbol == '>':
        return y, x + 1
    elif symbol == 'v':
        return y + 1, x
    elif symbol == '<':
        return y, x - 1
    return y, x

def simulate_guard_path(map, y, x, symbol):
    visited = set()
    while True:
        state = (y, x, symbol)
        if state in visited:
            return True  # Cycle detected
        visited.add(state)

        nextY, nextX = get_next_position(y, x, symbol)
        if nextY < 0 or nextY >= len(map) or nextX < 0 or nextX >= len(map[0]):
            return False  # Guard exits the map
        if map[nextY][nextX] == '#':
            symbol = player_symbole[(player_symbole.index(symbol) + 1) % 4]
        else:
            y, x = nextY, nextX

def find_positions_to_block(map, start_y, start_x, start_symbol):
    valid_positions = []
    for y in range(len(map)):
        for x in range(len(map[y])):
            if map[y][x] == '.' and (y != start_y or x != start_x):
                temp_map = deepcopy(map)
                temp_map[y][x] = '#'
                if simulate_guard_path(temp_map, start_y, start_x, start_symbol):
                    valid_positions.append((y, x))
    return valid_positions

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        text = get_text_from_file(file_path)
        map = format_map(text)
        y, x, symbol = get_coords_player(map)

        positions_to_block = find_positions_to_block(map, y, x, symbol)
        print(f"Nombre de positions valides pour ajouter un obstacle : {len(positions_to_block)}")
        #print("Positions :", positions_to_block)