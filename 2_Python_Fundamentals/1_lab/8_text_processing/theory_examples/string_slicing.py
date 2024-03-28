print('_' * 25 + 'String Slicing' + '_' * 25)
# (print('*' * 25)
# print(" " * 15 + '_' * 10 + '.find' + '_' * 10)

word = "Hello World"
# word[start:end:step]  items start through end-1
# word[start:]  items start through the rest of the list
# word[:end]  items from the beginning through end-1
# word[:]  a copy of the whole list
print(word[0]) #get one char of the word
print(word[0:1]) #get one char of the word (same as above)
print(word[0:3]) #get the first three char
print(word[:3]) #get the first three char
print(word[-3:]) #get the last three char
print(word[3:]) #get all but the three first char
print(word[:-3]) #get all but the three last character
print(word[0:7:2]) #get all char to the seventh with step two
print(word[::5])
print(word[::-1])
print(word[::-5])



