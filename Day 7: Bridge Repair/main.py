import sys


def get_text_from_file(filePath):
    with open(filePath, "r") as file:
        return file.read()


def can_reach_target(nums, target, index=1, current_result=None):
    if current_result is None:
        current_result = nums[0]
    if index == len(nums):
        return current_result == target

    if can_reach_target(nums, target, index + 1, current_result + nums[index]):
        return True

    if can_reach_target(nums, target, index + 1, current_result * nums[index]):
        return True

    concatenated_result = int(str(current_result) + str(nums[index]))
    if can_reach_target(nums, target, index + 1, concatenated_result):
        return True

    return False


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        text = get_text_from_file(file_path)
        lines = text.split("\n")

        answer = 0

        for line in lines:
            if line.strip() == "":
                continue
            calc = line.split(":")
            result = int(calc[0])
            split = calc[1].split(' ')
            calc = []
            for s in split:
                if s != "":
                    calc.append(int(s))
            if can_reach_target(calc, result):
                answer += result

        print(answer)