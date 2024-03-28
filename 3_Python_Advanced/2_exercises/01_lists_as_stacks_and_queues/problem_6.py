def balance_sequence_check(seq_to_check):

    char_container = []
    open_ch = ('(', '[', '{')

    for ch in seq_to_check:

        if ch in open_ch:
            char_container.append(ch)

        elif len(char_container) == 0:
            return False

        elif ch == ')' and char_container.pop() != '(':
            return False

        elif ch == ']' and char_container.pop() != '[':
            return False

        elif ch == '}' and char_container.pop() != '{':
            return False
    if len(char_container) == 0:
        return True
    return False


sequence = input()

if len(sequence) % 2 != 0:
    print('NO')
else:
    if balance_sequence_check(sequence):
        print('YES')
    else:
        print('NO')


# another logic to implement
# def is_balanced(parens: str) -> bool:
#     # Link: https://stackoverflow.com/a/73341167/
#     parens_map ={'(':')','{':'}','[':']'}
#     stack = []
#     for paren in parens:
#         if paren in parens_map:  # is open
#             stack.append(paren)
#         elif paren in parens_map.values():  # is close
#             if (not stack) or (paren != parens_map[stack.pop()]):
#                 return False
#     return not stack
