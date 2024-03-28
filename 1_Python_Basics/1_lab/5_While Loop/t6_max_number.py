enterance = input()
maximu_value = -10000000000000000
current = 0
while enterance != "Stop":
    current = int(enterance)

    if current > maximu_value:
        maximu_value = current
    enterance = input()
print(maximu_value)
