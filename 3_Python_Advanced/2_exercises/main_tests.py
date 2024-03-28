from collections import deque

asdf = deque([1, 2, 3, 4, 5])

while asdf:

    a = asdf.popleft()
    asdf.append(a)

    print(asdf)

    if asdf[0] == 1:
        break
