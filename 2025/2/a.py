# FILENAME = "example-input.txt"
FILENAME = "puzzle-input.txt"


with open(FILENAME, "r") as input_file:
    line = input_file.read().split('\n')[0]

faulty_range_ids_sum = 0


def handle_faulty(id):
    s = str(id)
    middle = len(s) // 2
    first_half = s[:middle]
    second_half = s[middle:]

    if (first_half == second_half):
        return id
    return 0


for r in line.split(","):
    first_id, last_id = r.split("-")
    for id in range(int(first_id), int(last_id) + 1):
        faulty_range_ids_sum += handle_faulty(id)

print(faulty_range_ids_sum)
