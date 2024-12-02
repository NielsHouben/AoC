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
    delta = r[1] - r[0]
    increasing = delta > 0

    if not is_delta_in_range(increasing, delta):
        return False
    for i in range(1, len(r) - 1):
        delta = r[i+1] - r[i]
        if not is_delta_in_range(increasing, delta):
            return False
    return True


def safe_reports(reports):
    return len([r for r in reports if is_report_safe(r)])


print(safe_reports(reports))
