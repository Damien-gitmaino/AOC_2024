import sys
import re

X = 101
Y = 103

def get_text_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()


def parse_robot(data):
    res = []
    for i in data.split(" "):
        split = i.split("=")[1].split(",")
        res.append((int(split[0]), int(split[1])))
    return res[0][0], res[0][1], res[1][0], res[1][1]


def est_dans_carre(carre, point):
    x, y, x1, y1 = carre
    px, py = point

    return x <= px <= x1 and y <= py <= y1


def inverser_signe(nombre):
    return -nombre


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        text = get_text_from_file(file_path)

        quadrants = [0, 0, 0, 0]
        nums = [list(map(int, re.findall(r"-?\d+", line))) for line in text.split("\n")]

        for i in range(X * Y):
            quadrant = [0, 0, 0, 0]
            picture = [" "] * (X * Y)
            for x, y, vx, vy in nums:
                nx = (x + vx * i) % X
                ny = (y + vy * i) % Y
                picture[ny * X + nx] = "#"
                if nx != X // 2 and ny != Y // 2:
                    quadrant[(nx > X // 2) + (ny > Y // 2) * 2] += 1

            if i == 100:
                print(quadrant[0] * quadrant[1] * quadrant[2] * quadrant[3])

            if ("#" * 20) in ''.join(picture):
                print(i)
                break
