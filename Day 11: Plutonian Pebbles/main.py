import sys
from collections import Counter

def get_text_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read().strip()

def parse_input(map_input):
    # Utiliser une compréhension de liste pour améliorer les performances
    return list(map(int, map_input.split()))

def split_stone(number):
    """Divise le nombre en deux pierres selon la règle des chiffres pairs."""
    num_str = str(number)
    mid = len(num_str) // 2
    left = int(num_str[:mid])
    right = int(num_str[mid:])
    return left, right

def simulate_blinks_optimized(initial_stones, blinks):
    """Simule les clignements de manière optimisée en utilisant un dictionnaire."""
    # Dictionnaire pour compter les occurrences des pierres
    stones = Counter(initial_stones)

    for _ in range(blinks):
        new_stones = Counter()
        for stone, count in stones.items():
            if stone == 0:
                new_stones[1] += count
            elif len(str(stone)) % 2 == 0:
                left, right = split_stone(stone)
                new_stones[left] += count
                new_stones[right] += count
            else:
                new_stones[stone * 2024] += count
        stones = new_stones

    return sum(stones.values())

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        text = get_text_from_file(file_path)
        grid = parse_input(text)
        sum_stones = simulate_blinks_optimized(grid, 75)


        print(sum_stones)