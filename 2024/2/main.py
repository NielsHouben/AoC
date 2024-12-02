# FILENAME = "2024/2/input-simple.txt"
FILENAME = "2024/2/input.txt"

reports = []

with open(FILENAME, "r") as input_file:
    for line in input_file.read().split('\n')[:-1]:
        reports.append(list(map(int, line.split())))


def is_delta_in_range(increasing, delta):
    if increasing and delta not in [1, 2, 3]:
        return False
    if not increasing and delta not in [-1, -2, -3]:
        return False
    return True


def is_report_safe(r):
    increasing = r[1] - r[0] > 0

    prev = r[0]
    for i in range(1, len(r)):
        delta = r[i] - prev
        if not is_delta_in_range(increasing, delta):
            return False
        prev = r[i]
    return True


def safe_reports(reports):
    sum = 0
    for r in reports:
        for i in range(len(r)):
            if is_report_safe(r[:i] + r[i+1:]):
                sum += 1
                break
    return sum


print(safe_reports(reports))

# b: 352 is too low...
# b: 354 is too low...
# b: 369 is too low...
# b: 373 is too low...
