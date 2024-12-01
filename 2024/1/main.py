

l1 = []
l2 = []

# FILENAME = "2024/1/input-simple.txt"
FILENAME = "2024/1/input.txt"

with open(FILENAME, "r") as input_file:
    # with open("small_input.txt", "r") as input_file:
    # with open("small_input2.txt", "r") as input_file:
    for line in input_file.read().split('\n')[:-1]:
        l, r = line.split()
        l1.append(int(l))
        l2.append(int(r))


def diff_lists(l1, l2):
    diff = 0
    l1.sort()
    l2.sort()
    for n1, n2 in zip(l1, l2):
        diff += abs(n1 - n2)

    return diff


def occurances(lst):
    occ = {}
    for n in lst:
        if n in occ:
            occ[n] += 1
        else:
            occ[n] = 1
    return occ


def similarity_score(l1, l2):
    score = 0
    occ = occurances(l2)
    print(occ)

    for n in l1:
        score += n * occ.get(n, 0)
    return score


print(similarity_score(l1, l2))
