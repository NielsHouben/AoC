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
    prev_error = False
    increasing = r[1] - r[0] > 0

    prev = r[0]
    for i in range(1, len(r)):
        delta = r[i] - prev
        if not is_delta_in_range(increasing, delta):
            if prev_error:
                print(r, "is unsafe")
                return False
            prev_error = True
        else:
            prev = r[i]
    return True


def safe_reports(reports):
    return len([r for r in reports if is_report_safe(r)])


print(safe_reports(reports))

# b: 352 is too low...
