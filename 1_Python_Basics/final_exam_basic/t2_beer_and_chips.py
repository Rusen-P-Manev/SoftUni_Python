from math import ceil

fan_name = input()
buddget = float(input())
number_bottel_beer = int((input()))
number_chips_packs = int(input())

price_per_beer = 1.20
price_per_pack_chips = (price_per_beer * number_bottel_beer) * 0.45
chip_total = ceil(price_per_pack_chips * number_chips_packs)
total_costs = number_bottel_beer * price_per_beer + chip_total

difference = abs(buddget - total_costs)

if buddget >= total_costs:
    print(f"{fan_name} bought a snack and has {difference:.2f} leva left.")
else:
    print(f"{fan_name} needs {difference:.2f} more leva!")