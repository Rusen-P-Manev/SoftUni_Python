# first_string, second_string = input().split()
# total_sum = 0
# if len(first_string) > len(second_string):
#     # Multiplication
#     for index in range(len(second_string)):
#         total_sum += ord(first_string[index]) * ord(second_string[index])
#     for index in range(len(second_string), len(first_string)):
#         total_sum += ord(first_string[index])
# elif len(second_string) > len(first_string):
#     for index in range(len(first_string)):
#         total_sum += ord(first_string[index]) * ord(second_string[index])
#     for index in range(len(first_string), len(second_string)):
#         total_sum += ord(second_string[index])
# elif len(second_string) == len(first_string):  # else
#     for index in range(len(second_string)):
#         total_sum += ord(first_string[index]) * ord(second_string[index])
# print(total_sum)



strings = input()
string_1, string_2 = strings.split()
total_sum = 0

for char1, char2 in zip(string_1, string_2):
    total_sum += ord(char1) * ord(char2)

if len(string_1) > len(string_2):
    total_sum += sum(ord(char) for char in string_1[len(string_2):])
elif len(string_2) > len(string_1):
    total_sum += sum(ord(char) for char in string_2[len(string_1):])

print(total_sum)