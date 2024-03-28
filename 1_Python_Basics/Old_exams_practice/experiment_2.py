family_buddget = float(input())
number_of_nights = int(input())
price_per_night = float(input())
additional_costs = int(input())

amount_per_nights_needed = number_of_nights * price_per_night
discount_residence = amount_per_nights_needed * 0.05
additional_costs_total = family_buddget * (additional_costs / 100)
total_costs = 0

if number_of_nights > 7:
    total_costs = (amount_per_nights_needed - discount_residence) + additional_costs_total
else:
    total_costs = amount_per_nights_needed + additional_costs_total

if family_buddget >= total_costs:
    monry_left = abs(family_buddget - total_costs)
    print(f"Ivanovi will be left with {monry_left:.2f} "
          f"leva after vacation.")
else:
    money_left = abs(family_buddget - total_costs)
    print(f"{money_left:.2f} leva needed.")
