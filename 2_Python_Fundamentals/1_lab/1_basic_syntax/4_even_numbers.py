n = int(input())

for _ in range(n):
    added_number = int(input())

    if not added_number % 2 == 0:
        print(f"{added_number} is odd!")
        break
else:
    print("All numbers are even.")
