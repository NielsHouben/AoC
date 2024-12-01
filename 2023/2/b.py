
with open("input.txt", "r") as input_file:
    # with open("small_input.txt", "r") as input_file:
    games = input_file.read().split('\n')


def cubes_to_amounts(cube_set):
    cube_lists = cube_set.split(', ')
    table = {}
    for cube_list in cube_lists:
        amount_colour = cube_list.split(' ')
        table[amount_colour[1]] = amount_colour[0]
    # print(table)
    return map(int, (table.get('red', 0), table.get('green', 0), table.get('blue', 0)))


def valid_cube_set(cube_set):
    r, g, b = cubes_to_amounts(cube_set)

    # if r > 12 or g > 13 or b > 14:
    #     return False

    return True


def eval_cube_sets(cube_sets):
    mr = 1
    mg = 1
    mb = 1

    for cube_set in cube_sets:
        r, g, b = cubes_to_amounts(cube_set)
        print(r, g, b)
        mr = max(mr, r)
        mg = max(mg, g)
        mb = max(mb, b)
    print(mr, mg, mb)
    power = mr * mg * mb
    return power


sum = 0
for game in games:
    if game[6] == ':':
        game_id = game[5]
        cube_sets = game[8:].split('; ')
    else:
        game_id = game[5:7]
        cube_sets = game[9:].split('; ')

    # print(game_id)
    print(cube_sets)
    p = eval_cube_sets(cube_sets)
    sum += p
    # if valid_cube_sets(cube_sets):
    #     sum += int(game_id)
print(sum)


# 77949 is too low