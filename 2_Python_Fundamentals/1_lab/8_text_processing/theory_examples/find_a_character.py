# Using .find() find the index of certen chracter...
print('_' * 25 + 'Find Character' + '_' * 25)
print(" " * 15 + '_' * 10 + '.find' + '_' * 10)

word = "Hello World"
print("The string is:",word)
character="W"
print("The character is:",character)
position=word.find(character)  # take character as input and returns its index..
print("The position of the character in the string is:",position)  # if serched char not in the strin returns -1

print(" " * 15 + '_' * 10 + '.index' + '_' * 10)
# Using .index find the index of certen chracter...
word = "Hello World"
print("The string is:",word)
character="W"
print("The character is:",character)
position=word.index(character)
print("The index of the character in the string is:",position)

print(" " * 15 + '_' * 10 + '.count' + '_' * 10)

word = "Hello World"
print("The string is:",word)
character="l"
print("The character is:",character)
position=word.count(character)
print("The frequency of the character in the string is:",position)

print('*' * 25)

myStr = "Count, the number of spaces"
print("The string is:",myStr)
character=" "
position=myStr.count(character)
print("The number of spaces in the string is:",position)

print('_' * 25 + 'Changing Upper and Lower Case Strings' + '_' * 25)
print(" " * 15 + '_' * 10 + '.upper' + '_' * 10)

my_string = 'Some texT'
new_text = my_string.upper()
print(new_text)

print(" " * 15 + '_' * 10 + '.lower' + '_' * 10)

new_text = my_string.lower()
print(new_text)

print(" " * 15 + '_' * 10 + '.title' + '_' * 10)

new_text = my_string.title()
print(new_text)

print(" " * 15 + '_' * 10 + '.capitalize' + '_' * 10)

new_text = my_string.capitalize()
print(new_text)

print(" " * 15 + '_' * 10 + '.swapcase' + '_' * 10)

new_text = my_string.swapcase()
print(new_text)





