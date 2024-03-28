words_cont = int(input())

words_catalog = {}

for _ in range(words_cont):
    key_word = input()
    synonym = input()

    if key_word not in words_catalog:
        words_catalog[key_word] = []
    words_catalog[key_word].append(synonym)

for word in words_catalog:
    print(f'{word} - {", ".join(words_catalog[word])}')
