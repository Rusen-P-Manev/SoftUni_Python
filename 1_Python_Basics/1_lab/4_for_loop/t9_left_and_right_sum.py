n = int(input())

sum_one = 0
sum_two = 0

for i in range(1, n + 1):
    sum_one += int(input())
for i in range(1, n + 1):
    sum_two += int(input())
if sum_one == sum_two:
    print(f"Yes, sum = {sum_one}")
elif sum_one != sum_two:
    differece = abs(sum_one - sum_two)
    print(f"No, diff = {differece}")

