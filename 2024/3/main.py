# FILENAME = "2024/3/input-simple.txt"
FILENAME = "2024/3/input.txt"

memory = ""

with open(FILENAME, "r") as input_file:
    for line in input_file.read().split('\n')[:-1]:
        memory += line


def parse_memory(memory):
    do_sum = True
    sum = 0
    idx = 0
    while True:
        next_do = memory.find("do()", idx+1)
        next_do_not = memory.find("don't()", idx+1)
        next_mul = memory.find("mul(", idx+1)

        findings = [x for x in [next_do, next_do_not, next_mul] if x != -1]
        if len(findings) == 0:
            break

        idx = min(findings)

        if idx == next_do:
            do_sum = True
            continue
        if idx == next_do_not:
            do_sum = False
            continue

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
        if do_sum:
            sum += int(n1) * int(n2)

    return sum


print(parse_memory(memory))
