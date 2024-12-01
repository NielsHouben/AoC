
with open("input.txt", "r") as input_file:
    # with open("small_input.txt", "r") as input_file:
    # with open("small_input2.txt", "r") as input_file:
    board = input_file.read().split('\n')


table = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}


def first_digit(line):
    for idx, c in enumerate(line):
        if c.isdigit():
            return c
        if idx + 2 < len(line) and c + line[idx + 1] + line[idx + 2] in ['one', 'two', 'six']:
            return table[c + line[idx + 1] + line[idx + 2]]
        if idx + 3 < len(line) and c + line[idx + 1] + line[idx + 2] + line[idx + 3] in ['four', 'five', 'nine']:
            return table[c + line[idx + 1] + line[idx + 2] + line[idx + 3]]
        if idx + 4 < len(line) and c + line[idx + 1] + line[idx + 2] + line[idx + 3] + line[idx + 4] in ['three', 'seven', 'eight']:
            return table[c + line[idx + 1] + line[idx + 2] + line[idx + 3] + line[idx + 4]]


def last_digit(line):
    line = line[::-1]
    for idx, c in enumerate(line):
        if c.isdigit():
            return c
        if idx + 2 < len(line) and c + line[idx + 1] + line[idx + 2] in ['eno', 'owt', 'xis']:
            return table[(c + line[idx + 1] + line[idx + 2])[::-1]]
        if idx + 3 < len(line) and c + line[idx + 1] + line[idx + 2] + line[idx + 3] in ['ruof', 'evif', 'enin']:
            return table[(c + line[idx + 1] + line[idx + 2] + line[idx + 3])[::-1]]
        if idx + 4 < len(line) and c + line[idx + 1] + line[idx + 2] + line[idx + 3] + line[idx + 4] in ['eerht', 'neves', 'thgie']:
            return table[(c + line[idx + 1] + line[idx + 2] + line[idx + 3] + line[idx + 4])[::-1]]


sum = 0
for line in board:
    try:
        sum += int(first_digit(line) + last_digit(line))
    except:
        print(line)
        print(line[::-1])
        print('eerht' in ['eerht', 'neves', 'thgie'])
        # for idx, c in enumerate(line[::-1]):
        # print(c + line[idx + 1] + line[idx + 2] + line[idx + 3] + line[idx + 4])
        print(first_digit(line), last_digit(line))

print(sum)
