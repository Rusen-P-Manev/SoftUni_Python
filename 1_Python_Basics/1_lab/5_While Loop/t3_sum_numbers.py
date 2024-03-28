first_number = int(input())
sum_total = 0

while True:
    current_number = int(input())
    sum_total += current_number

    if sum_total >= first_number:
        print(sum_total)
        break
