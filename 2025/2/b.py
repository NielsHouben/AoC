# FILENAME = "example-input.txt"
FILENAME = "puzzle-input.txt"


def handle_faulty(id):
    id_str = str(id)
    middle = len(id_str) // 2
    for i in range(1, middle + 1):
        sub = id_str[:i]
        if len(id_str) % len(sub) != 0:
            continue
        if all([id_str[start*i:start*i + i] == sub for start in range(len(id_str) // i)]):
            return id
    return 0


with open(FILENAME, "r") as input_file:
    line = input_file.read().split('\n')[0]

faulty_range_ids_sum = 0

for r in line.split(","):
    first_id, last_id = r.split("-")
    for id in range(int(first_id), int(last_id) + 1):
        faulty_range_ids_sum += handle_faulty(id)

print(faulty_range_ids_sum)
