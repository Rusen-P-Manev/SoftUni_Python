word_to_ban = input().split(', ')
text_to_ban = input()

for word in word_to_ban:
    while word in text_to_ban:
        text_to_ban = text_to_ban.replace(word, '*' * len(word))

print(text_to_ban)

