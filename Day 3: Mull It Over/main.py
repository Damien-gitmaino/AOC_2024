import sys
import re
from itertools import count

motif = r"mul\(\d{1,3},\d{1,3}\)"
control_motif = r"(do\(\)|don't\(\))"


def get_text_from_file(filePath):
    with open(filePath, "r") as file:
        return file.read()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        text = get_text_from_file(file_path)
        instructions = re.findall(f"{motif}|{control_motif}", text)
        instructionsMul = re.findall(f"{motif}", text)

        result = 0

        indexInMulList = 0

        for index in range(0, len(instructions)):
            if instructions[index] == '':
                instructions[index] = instructionsMul.pop(0)
                indexInMulList += 1

        execute = True

        for i in instructions:
            if i == "do()":
                execute = True
            elif i == "don't()":
                execute = False
            else:
                if execute:
                    i = i.replace("mul(", "")
                    i = i.replace(")", "")
                    i = i.split(",")
                    result += int(i[0]) * int(i[1])

        print(result)
