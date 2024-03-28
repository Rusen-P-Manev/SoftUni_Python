from collections import deque

money = [int(x) for x in input().split(' ')]
food_price = deque(int(x) for x in input().split(' '))

taken_meals = 0

while money and food_price:
    current_money = money[-1]
    current_bill = food_price[0]

    if current_money == current_bill:
        taken_meals += 1
        money.pop()
        food_price.popleft()

    elif current_money > current_bill:
        taken_meals += 1
        difference = current_money - current_bill
        money.pop()
        if len(money) > 0:
            money[-1] += difference
        food_price.popleft()

    elif current_money < current_bill:
        money.pop()
        food_price.popleft()

if taken_meals >= 4:
    print(f'Gluttony of the day! Henry ate {taken_meals} foods.')
elif 1 < taken_meals < 4:
    print(f'Henry ate: {taken_meals} foods.')
elif taken_meals == 1:
    print(f'Henry ate: {taken_meals} food.')
else:
    print(f'Henry remained hungry. He will try next weekend again.')
