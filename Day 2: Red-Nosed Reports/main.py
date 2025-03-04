import sys

def is_safe(report):
    increasing = True
    decreasing = True

    for i in range(len(report) - 1):
        diff = report[i + 1] - report[i]

        if abs(diff) < 1 or abs(diff) > 3:
            return False
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False

    return increasing or decreasing


def can_be_made_safe(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i+1:]
        if is_safe(modified_report):
            return True
    return False

def count_safe_reports(file_path):
    safe_count = 0

    try:
        with open(file_path, 'r') as file:
            for line in file:
                if line.strip():
                    report = list(map(int, line.split()))
                    if is_safe(report) or can_be_made_safe(report):
                        safe_count += 1
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        return 0
    except ValueError:
        print("Error: File contains non-numeric data.")
        return 0

    return safe_count

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <file_path>")
    else:
        file_path = sys.argv[1]
        safe_count = count_safe_reports(file_path)
        print(f"Number of safe reports: {safe_count}")