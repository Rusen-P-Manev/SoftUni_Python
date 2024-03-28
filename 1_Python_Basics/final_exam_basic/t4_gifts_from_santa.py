n = int(input())
m = int(input())
s = int(input())

for i in reversed(range(n, m + 1)):
    if i % 2 == 0 and i % 3 == 0:
        if i == s:
            break
            print(i, end=" ")
        print("a", end=" ")
    print("b", end=" ")
print("b", end=" ")