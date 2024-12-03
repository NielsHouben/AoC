# FILENAME = "2024/3/input-simple.txt"
FILENAME = "2024/3/input.txt"

memory = ""

with open(FILENAME, "r") as input_file:
    for line in input_file.read().split('\n')[:-1]:
        memory += line


def parse_memory(memory):
    sum = 0
    idx = 0
    while True:
        idx = memory.find("mul(", idx+1)
        if idx == -1 or idx + 4 > len(memory):
            break

        start = idx+4
        end = memory.find(")", start)
        args = memory[idx+4: end].split(",")
        if len(args) != 2:
            continue
        n1, n2 = args
        if len(n1) > 3 or len(n2) > 3:
            continue
        sum += int(n1) * int(n2)

    return sum


print(parse_memory(memory))
