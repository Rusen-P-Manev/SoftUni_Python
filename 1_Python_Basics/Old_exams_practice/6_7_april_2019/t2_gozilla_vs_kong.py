budget = float(input())
number_of_extras = int(input())
outfit_of_an_extra = float(input())

decor = budget * 0.10
outfit_discount = 0.90
total_costs = 0

if number_of_extras > 150:
    total_costs = decor + (number_of_extras * outfit_of_an_extra * outfit_discount)
else:
    total_costs = decor + number_of_extras * outfit_of_an_extra

difference = abs(total_costs - budget)

if total_costs <= budget:
    print(f"Action!\nWingard starts filming with {difference:.2f} leva left.")
else:
    print(f"Not enough money!\nWingard needs {difference:.2f} leva more.")
