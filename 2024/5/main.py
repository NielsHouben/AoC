# FILENAME = "2024/5/input-simple.txt"
FILENAME = "2024/5/input.txt"

predecessors = {}  # should be object with values as lists
updates = []

with open(FILENAME, "r") as input_file:
    fill_predecessors = True
    for line in input_file.read().split('\n')[:-1]:
        if fill_predecessors:
            if line == "":
                fill_predecessors = False
            else:
                value, key = (int(x) for x in line.split("|"))
                if key in predecessors:
                    predecessors[key].append(value)
                else:
                    predecessors[key] = [value]

        else:
            updates.append([int(x) for x in line.split(",")])


def is_update_valid(update, predecessors):
    seen = set()
    for n in update:
        seen.add(n)
        relevant_predecessors = [p for p in predecessors.get(n, []) if p in update]
        if not all(p in seen for p in relevant_predecessors):
            return False
    return True

    return True


def get_valid_updates(predecessors, updates):
    return [update for update in updates if is_update_valid(update, predecessors)]


def sum_middle_elements(predecessors, updates):
    valid_updates = get_valid_updates(predecessors, updates)
    res = 0
    for update in valid_updates:
        res += update[len(update) // 2]
    return res


for p in predecessors:
    print(p, predecessors[p])
print()
print(sum_middle_elements(predecessors, updates))
