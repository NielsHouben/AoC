
# with open("input.txt", "r") as input_file:
with open("small_input.txt", "r") as input_file:
    lines = input_file.read().split('\n')


sections = []
builder = []
for line in lines[3:]:
    if ':' in line:
        sections.append(builder)
        builder = []
        continue
    builder.append(line)
sections = [filter(lambda x: len(x) > 0, section) for section in sections]
sections = [[list(map(int, line.split(' '))) for line in section] for section in sections]
print(sections)
for section in sections:
    print("----------")
    for line in section:
        print(line)


def get_num_from_section(num, section):
    # first check if num is within a section
    for line in section:

        ...

    # else return num
    return num


print("##########")
location_numbers = []
# for seed_num in lines[0][7:].split(' '):
for seed_num in map(int, ["79"]):
    current_num = seed_num
    for section in sections:
        current_num = get_num_from_section(current_num, section)

    print(seed_num, current_num)
