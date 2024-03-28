some_text = 'Hi, Neo, tis is loco. The matrix has you!'
another_text = '%the&Matrix1234'

# aslist = list(some_text)
# print(aslist)
# aslist = list(another_text)
# print(aslist)

some_text = some_text.replace(',','').replace('.', '').casefold()
#print(some_text)

text = some_text.isupper()
print(some_text)
print(text)
text = some_text.rpartition('o')
print(some_text)
print(text)
