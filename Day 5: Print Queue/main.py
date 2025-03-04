import sys

def get_text_from_file(filePath):
    with open(filePath, "r") as file:
        return file.read()

def parse_data(text):
    lines = text.split("\n")

    X = []
    Y = []
    updates = []

    for line in lines:
        if '|' in line:
            split = line.split("|")
            X.append(int(split[0]))
            Y.append(int(split[1]))
        elif ',' in line:
            line = line.split(",")
            data = []
            for i in line:
                data.append(int(i))
            updates.append(data)

    return X, Y, updates

def check_before(page, index, number):
    while index >= 0:
        if page[index] == number:
            return True
        index -= 1
    return False


def check_after(page, index, number):
    while index < len(page):
        if page[index] == number:
            return True
        index += 1
    return False

def get_middle_number_of_array(array):
    return array[len(array)//2]

def check_is_good_order(X, Y, update):
    needToSwap = []
    for pageIndex in range(len(update)):
        cantBeBefore = []
        cantBeAfter = []

        for i in range(len(X)):
            if X[i] == update[pageIndex]:
                cantBeBefore.append(Y[i])
            if Y[i] == update[pageIndex]:
                cantBeAfter.append(X[i])

        delete = False

        for before in cantBeBefore:
            if check_before(update, pageIndex-1, before):
                delete = True
                needToSwap = [update[pageIndex], before]
                break

        if delete:
            return False, needToSwap

        for after in cantBeAfter:
            if check_after(update, pageIndex+1, after):
                delete = True
                needToSwap = [after, update[pageIndex]]
                break

        if delete:
            return False, needToSwap

    return True, needToSwap

def swap_two_number_in_a_list(list, number1, number2):
    index1 = list.index(number1)
    index2 = list.index(number2)

    list[index1] = number2
    list[index2] = number1

    return list

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        text = get_text_from_file(file_path)
        X, Y, updates = parse_data(text)

        badUpdates = []

        result = 0
        for update in updates:
            good = True
            res, needToSwap = check_is_good_order(X, Y, update)
            if res:
                result += get_middle_number_of_array(update)
            else:
                badUpdates.append(update)

        print(result)
        result = 0

        for badUpdate in badUpdates:
            res = False
            while True:
                res, needToSwap = check_is_good_order(X, Y, badUpdate)
                if res:
                    break
                badUpdate = swap_two_number_in_a_list(badUpdate, needToSwap[0], needToSwap[1])
            result += get_middle_number_of_array(badUpdate)

        print(result)