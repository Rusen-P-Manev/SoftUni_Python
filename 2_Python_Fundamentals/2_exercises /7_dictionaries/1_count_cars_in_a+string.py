# the_string_is = input().split(' ')
#
# catalog = {}
#
# for text in the_string_is:
#     for ch in text:
#         if ch not in catalog:
#             catalog[ch] = 1
#         else:
#             catalog[ch] += 1
#
# for key, val in catalog.items():
#     print(f'{key} -> {val}')

symbols = [character for character in input() if character != " "]
letters = {}
for symbol in symbols:
    if symbol not in letters.keys(): # if symbol not in letters
        letters[symbol] = 0
    letters[symbol] += 1
for symbol, occurrences in letters.items():
    print(f"{symbol} -> {occurrences}")
