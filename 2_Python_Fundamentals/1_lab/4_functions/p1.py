# list_of_strings = input().split()
# list_of_numbers = []
#
# for n in list_of_strings:
#     number = float(n)
#     list_of_numbers.append(number)
# list_of_absolute_numbers = []
#
# for n in list_of_numbers:
#     absolute_number = abs(n)
#     list_of_absolute_numbers.append(absolute_number)
#
# print(list_of_absolute_numbers)

def transform_data(data_list: list):
    return [float(ele) for ele in data_list]


def print_abs_values(numbers_list: list):
    print([abs(ele) for ele in numbers_list])


data = input().split()
print_abs_values(transform_data(data))
