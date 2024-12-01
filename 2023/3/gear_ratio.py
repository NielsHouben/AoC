

with open("input.txt", "r") as input_file:
    # with open("small_input.txt", "r") as input_file:
    board = input_file.read().split('\n')


width = len(board[0])
height = len(board)

number_start_positions = set()  # the starting positions of numbers

symbol_positions = []  # coordinates of symbols


def show_board():
    print("\n".join(board))


def get_pos(x, y):
    return board[y][x]


def filter_neightobur(neighbnour):
    x = neighbnour[0]
    y = neighbnour[1]
    if not 0 <= x < width:
        return False
    if not 0 <= y < height:
        return False
    return True


def positions_of_neightbours(x, y):
    neighbnours = [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                   (x - 1, y), (x, y), (x + 1, y),
                   (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]
    return list(filter(filter_neightobur, neighbnours))


def get_number_position(x, y):
    """ takes in position of integer and gives number start position"""
    # number_start_positions.add((x, y))
    # if position to left is number, return, else call self with number to left
    if x >= 0:
        left = get_pos(x - 1, y)
    else:
        return x, y
    if left.isdigit():  # we need to check to left of left
        return get_number_position(x - 1, y)
    else:
        return x, y


show_board()

# get all symbol positions
for y in range(height):
    for x in range(width):
        res = get_pos(x, y)
        if res == '*':
            symbol_positions.append((x, y))

number_position_pairs = []
# get number positions of neighbouring numbers to symbols
for x, y in symbol_positions:
    new_positions = set()
    for neighbnour in positions_of_neightbours(x, y):
        if not get_pos(*neighbnour).isdigit():
            continue
        new_positions.add(get_number_position(*neighbnour))
    if len(new_positions) == 2:
        number_position_pairs.append(new_positions)
    # number_start_positions.add(get_number_position(*neighbnour))
    # check neighbnours for integer
    # do process to find the integers wholenumbers start position


def get_rightmost_integer(x, y):
    if x < width - 1:
        right = get_pos(x + 1, y)
    else:
        return x, y
    if right.isdigit():  # we need to check to left of left
        return get_rightmost_integer(x + 1, y)
    else:
        return x, y


def get_number_from_start_position(x, y):
    end_x, end_y = get_rightmost_integer(x, y)
    # print(x, y, end_x, end_y, board[y][x:end_x + 1])
    num = int(board[y][x:end_x + 1])
    return num


numbers = []
for num_pos1, num_pos2 in number_position_pairs:
    num1 = get_number_from_start_position(*num_pos1)
    print(num_pos1, num1)
    num2 = get_number_from_start_position(*num_pos2)
    print(num_pos2, num2)
    numbers.append(num1 * num2)

# print(get_number_position(1, 0))
# print(number_start_positions)
# for start_position in number_start_positions:
#     numbers.append(get_number_from_start_position(*start_position))

# print(numbers)
print(sum(numbers))
