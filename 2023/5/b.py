from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


with open("input.txt", "r") as input_file:
    # with open("small_input.txt", "r") as input_file:
    lines = input_file.read().split('\n')


sections = []
builder = []
for line in lines[3:]:
    if ':' in line:
        sections.append(builder)
        builder = []
        continue
    builder.append(line)
sections.append(builder)

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
        destination_range_start = line[0]
        source_range_start = line[1]
        range_len = line[2]
        if source_range_start <= num < source_range_start + range_len:
            return destination_range_start + num - source_range_start

    return num


seed_ranges = list(map(int, lines[0][7:].split(' ')))
print("##########")
location_numbers = []
ranges = []
for idx in range(0, len(seed_ranges), 2):
    print(seed_ranges[idx], seed_ranges[idx+1])
    ranges.append((seed_ranges[idx],  seed_ranges[idx+1]))


cached_seed_nums = {}


def cached_seed_num_to_num(seed_num):
    return cached_seed_nums .get(seed_num, seed_num_to_num(seed_num))


def seed_num_to_num(seed_num):
    current_num = seed_num
    for section in sections:
        current_num = get_num_from_section(current_num, section)
    return current_num


@timeit
def get_lowest_from_range(start, length):
    for seed_num in range(start, start + length):
        location_numbers.append(cached_seed_num_to_num(seed_num))

    print(min(location_numbers), location_numbers)


def main():
    print(ranges)

    for start, length in ranges:
        get_lowest_from_range(start, length)


main()
