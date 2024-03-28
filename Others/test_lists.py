# x = 'asdf'
# y = lambda i: i * 3
# print(y(x))

strin_is = 'Hallo World'
as_str = [ch for ch in strin_is]
as_str_two = list(strin_is)
if ' ' in as_str:
    as_str.remove(' ')
print(strin_is)
print(as_str)
print(as_str_two)
print((''.join(as_str)).lower())

# това мога да го използвам за валидацията на паролата
nums = [1, 2, 3, 4, 5, 6]
filtered = [True if x % 2 == 0 else False for x in nums]
print(filtered)

text = 'asdasdlk;jsaf'
vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']
no_vowels = ''.join([x for x in text if x not in vowels])
print(no_vowels)

numbers_list = [6, 2, 1, 4, 3, 5]
sorted_numbers = sorted(numbers_list)

numbers_list = [6, 2, 1, 4, 3, 5]
sorted_numbers = sorted(numbers_list)

strings_list = ["1", "2", "3", "4"]
numbers_list = list(map(int, strings_list))
print(numbers_list)

numbers_list = [1, 2, 3, 4]
doubled_list = list(map(lambda x: x*2, numbers_list))
print('doble: ', doubled_list)

numbers_list = [1, 2, 3, 4, 5, 6]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers_list))
print(even_numbers)

numbers = [1, 2, 2, 3, 1, 4, 5, 4, 'asdf', 'asdf', 'aa']
unique_numbers = list(set(numbers))
print(unique_numbers)

