word_to_remove = input()
strin_to_remove_from = input()

while word_to_remove in strin_to_remove_from:
    strin_to_remove_from = strin_to_remove_from.replace(word_to_remove, '')

print(strin_to_remove_from)
