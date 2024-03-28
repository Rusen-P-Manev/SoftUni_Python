number = int(input())

for i in range(1, number + 1):
    first = i % 10
    second = i // 10
    sum_digits = first + second

    if (sum_digits == 5
            or sum_digits == 7
            or sum_digits == 11):
        print(f"{i} -> True")
    else:
        print(f"{i} -> False")
