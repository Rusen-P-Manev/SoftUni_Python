# longest_intersection = set()
#
# for _ in range(int(input())):
#     first_data, second_data = [el.split(",") for el in input().split("-")]  # "0,3-1,2" -> ["0,3", "1,2"] -> [["0", "3"], ["1", "2"]]
#
#     first_set = set(range(int(first_data[0]), int(first_data[1]) + 1))  # {0, 1, 2, 3}
#     second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))  # {1, 2}
#
#     intersection = first_set.intersection(second_set)  # first_set & second_set
#
#     if len(intersection) > len(longest_intersection):
#         longest_intersection = intersection
#
# print(
#     f"Longest intersection is "
#     f"[{', '.join(str(x) for x in longest_intersection)}] "
#     f"with length {len(longest_intersection)}"
# )


def create_sequence(start_index, end_index):
    seq_set = set()
    for i in range(start_index, end_index + 1):
        seq_set.add(i)
    return seq_set


repetition = int(input())
container = {}

for _ in range(repetition):
    data = input().split('-')

    first_range = [int(x) for x in data[0].split(',')]
    second_range = [int(x) for x in data[1].split(',')]

    result = (create_sequence(first_range[0], first_range[1])
              .intersection
              (create_sequence(second_range[0], second_range[1])))

    container[len(result)] = result

print(f'Longest intersection is {list(container[max(container)])}'
      f' with length {max(container)}')