# odd_set = set()
# even_set = set()
#
# for row in range(1, int(input()) + 1):
#     ascii_sum_of_name = sum(ord(l) for l in input()) // row
#
#     if ascii_sum_of_name % 2 == 0:
#         even_set.add(ascii_sum_of_name)
#     else:
#         odd_set.add(ascii_sum_of_name)
#
# sum_odd_set, sum_even_set = sum(odd_set), sum(even_set)
#
# if sum_even_set == sum_odd_set:
#     print(*odd_set.union(even_set), sep=", ")
# elif sum_even_set < sum_odd_set:
#     print(*odd_set.difference(even_set), sep=", ")  # B - A
# else:
#     print(*odd_set.symmetric_difference(even_set), sep=", ")


def transform_and_sum(name: str):
    chars_sum = 0
    for ch in name:
        chars_sum += ord(ch)
    return chars_sum


repetition = int(input())

odd_container = set()
even_container = set()

for row in range(1, repetition + 1):
    current_name = input()

    value_to_check = transform_and_sum(current_name) // row

    if value_to_check % 2 == 0:
        even_container.add(value_to_check)
    else:
        odd_container.add(value_to_check)

if sum(odd_container) == sum(even_container):
    print(*odd_container.union(even_container), sep=', ')

elif sum(odd_container) > sum(even_container):
    print(*odd_container.difference(even_container), sep=', ')

elif sum(odd_container) < sum(even_container):
    print(*odd_container.symmetric_difference(even_container), sep=', ')
