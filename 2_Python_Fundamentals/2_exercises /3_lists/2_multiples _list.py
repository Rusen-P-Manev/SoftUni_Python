factor = int(input())
count = int(input())

final_list = []
next_number = 0
for _ in range(count):
    next_number += factor
    final_list.append(next_number)

print(final_list)
