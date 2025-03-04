import sys
import z3

s = [0, 0]

def get_text_from_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def parse_input(data):
    machines = []
    for line in data.split("\n\n"):
        lines = line.strip().split("\n")
        ax, ay = map(int, lines[0].split("X+")[1].split(", Y+"))
        bx, by = map(int, lines[1].split("X+")[1].split(", Y+"))
        px, py = map(int, lines[2].split("X=")[1].split(", Y="))
        machines.append(((ax, ay), (bx, by), (px, py)))
    return machines


def solve_machine(machine):
    (ax, ay), (bx, by), (px, py) = machine

    for i, add in enumerate([0, 10000000000000]):
        a, b = z3.Int('a'), z3.Int('b')

        solver = z3.Optimize()
        solver.add(px + add == a * ax + b * bx)
        solver.add(py + add == a * ay + b * by)
        solver.minimize(a * 3 + b)

        if solver.check() == z3.sat:
            model = solver.model()
            s[i] += model.eval(a).as_long() * 3 + model.eval(b).as_long()

    print(*s, sep="\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage : python script.py <chemin_du_fichier>")
    else:
        file_path = sys.argv[1]
        text = get_text_from_file(file_path)
        machines = parse_input(text)
        print(machines)

        for machine in machines:
            solve_machine(machine)