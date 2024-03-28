# не работи с 111 и други случаи....
# виж следващата задача
n = int(input())

sum_one = 0
sum_two = 0

for i in range(2, n + 2):
    num_one = int(input())
    num_two = int(input())
    if i % 2 == 0:
        sum_one = num_one + num_two
    else:
        sum_two += num_one + num_two

if sum_one == sum_two:
    print(f"Yes, sum = {sum_one}")
elif sum_one != sum_two:
    differece = abs(sum_one - sum_two)
    print(f"No, diff = {differece}")

