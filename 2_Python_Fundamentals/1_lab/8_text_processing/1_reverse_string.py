# text = input()
# while text != 'end':
#     rev = reversed(text)
#     reversed_text = ''.join(rev)
#     print(f'{text} = {reversed_text}')
#     text = input()

while True:
    word = input()

    if word == 'end':
        break

    rev_word = word[::-1]
    print(f'{word} = {rev_word}')