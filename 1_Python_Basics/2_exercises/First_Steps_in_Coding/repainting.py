amount_of_nyalon = int(input())
amount_of_paint = int(input())
amount_of_thinner = int(input())
working_houers = int(input())

nyalon_per_sqm = 1.5
paint_per_liter = 14.50
thinner_per_liter = 5
bags = 0.40
total_expenses_material = (amount_of_nyalon + 2) * nyalon_per_sqm \
        + amount_of_paint * paint_per_liter + (amount_of_paint * paint_per_liter * 0.1) \
        + amount_of_thinner * thinner_per_liter \
        + bags
total_expences = total_expenses_material + (total_expenses_material * 0.3 * working_houers)

print(total_expences)