print('_' * 25 + 'Replace Substring' + '_' * 25)
# You can replace a substring with another substring using the replace()
# method in Python. The replace() method, when invoked on a string, takes
# the substring to replaced as its first input argument and the replacement
# string as its second input argument. After execution, it replaces the
# specified substring with the replacement string and returns a modified string.
print(" " * 15 + '_' * 10 + '.replace' + '_' * 10)

text = 'Hello World'

new_text = text.replace('Hello', 'Hi')

print(new_text)
