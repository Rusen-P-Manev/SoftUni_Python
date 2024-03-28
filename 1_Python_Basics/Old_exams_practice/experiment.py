# a = "asdf"
# b = len(a)
# print(b)
# a = "qwerty"
# b = (ord(a[0]) + ord(a[1]))
# print(b)
# a = (8 / 12) * 100
# print(float(a))
break_condition = False

for h in range(24):
    for m in range(60):
        print(f"{h:02d}:{m:02d}")

        if h == 5:
            break_condition = True
            break

    if break_condition:
        break