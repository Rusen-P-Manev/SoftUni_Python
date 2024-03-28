enterance = input()
minimum_value = 10000000000000000
current = 0
while enterance != "Stop":
    current = int(enterance)

    if current < minimum_value:
        minimum_value = current
    enterance = input()
print(minimum_value)
