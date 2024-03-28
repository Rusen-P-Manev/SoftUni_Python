data = input().split()

stack = {}

for i in range(0, len(data), 2):
    food = data[i]
    quantity = int(data[i + 1])
    stack[food] = quantity

print(stack)
