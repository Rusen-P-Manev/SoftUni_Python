# from collections import deque
#
# numbers = deque(input().split())
#
# for _ in range(len(numbers)):
#     print(numbers.pop(), end=" ")

# solution 2

# numbers = deque(input().split())
#
# numbers.reverse()
#
# print(*numbers)

# my solution

some_str = input().split(' ')
rev_str = []
for ele in some_str.copy():
    rev_str.append(some_str.pop())
print(' '.join(rev_str))