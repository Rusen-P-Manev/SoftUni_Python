budget = float(input())
number_of_statist = int(input())
one_suit_price = float(input())
decor_price = budget * 0.10
suits_price = one_suit_price * number_of_statist
if number_of_statist > 150:
    suits_price *= 0.9
neaded_money = suits_price + decor_price
diference = abs(neaded_money - budget)
if neaded_money > budget:
    print(f"Not enough money!")
    print(f"Wingard needs {diference:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {diference:.2f} leva left.")