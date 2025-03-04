import sys


def split_columns(file_path):
    left_column = []
    right_column = []

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():  # Ignorer les lignes vides
                    numbers = line.split()
                    if len(numbers) == 2:
                        left_column.append(int(numbers[0]))
                        right_column.append(int(numbers[1]))
                    else:
                        print(f"Ligne ignorée : {line.strip()} (ne contient pas exactement deux nombres)")
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{file_path}' est introuvable.")
        return [], []
    except ValueError:
        print("Erreur : Le fichier contient des données non numériques.")
        return [], []

    return left_column, right_column


def get_smallest_number_in_my_list(numbers):
    if not numbers:
        return None

    smallest = numbers[0]
    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest

def count_how_much_time_the_number_appear_in_the_list(numbers, number):
    count = 0
    for n in numbers:
        if n == number:
            count += 1
    return count


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        left, right = split_columns(file_path)
        result = 0

        if len(left) != len(right):
            print("Erreur : Les colonnes n'ont pas la même taille.")
            sys.exit(1)

        for i in left:
            iteration = count_how_much_time_the_number_appear_in_the_list(right, i)
            result += i * iteration

        print("Colonne de gauche :", left)
        print("Colonne de droite :", right)
        print("Résultat final :", result)