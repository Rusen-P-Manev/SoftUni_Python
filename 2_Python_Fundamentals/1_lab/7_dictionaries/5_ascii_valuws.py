# characters = input().split(', ')
#
# char_dict = {char: ord(char) for char in characters}
#
# print(char_dict)


char_list = input().split(', ')

pair_values = {}

for element in char_list:
    code_name = ord(element)
    pair_values[element] = code_name

print(pair_values)