with open("input.txt", "r") as input_file:
    # with open("small_input.txt", "r") as input_file:
    cards = input_file.read().split('\n')


def card_matches(winning_nums, my_nums):
    sum = 0
    for num in my_nums:
        if num in winning_nums:
            sum += 1
    return sum


cards_points = 0
copies = [1] * 1000
for idx, card in enumerate(cards):

    spl = (card[8:].split(' | '))
    winning_nums = list(filter(lambda x: len(x) > 0, spl[0].split(' ')))
    my_nums = list(filter(lambda x: len(x) > 0, spl[1].split(' ')))

    matches = card_matches(winning_nums, my_nums)
    # if matches > 0:
    #     cards_points += 2 ** (matches - 1)
    for match_idx in range(1, matches + 1):
        copies[idx + match_idx] += 1 * copies[idx]
    print(winning_nums, my_nums, cards_points)

print(sum(copies[:len(cards)]))
print(copies)
