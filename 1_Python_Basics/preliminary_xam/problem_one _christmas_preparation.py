number_of_rolls_of_wrapping_paper = int(input())
number_of_fabric_rolls = int(input())
liters_of_glue = float(input())
percentage_discount = int(input())


wrapping_paper_price_per_roll = 5.80
fabric_price_per_roll = 7.20
glue_price_per_liter = 1.20

discount = percentage_discount / 100

costs = (number_of_rolls_of_wrapping_paper * wrapping_paper_price_per_roll\
              + number_of_fabric_rolls * fabric_price_per_roll\
              + liters_of_glue * glue_price_per_liter)
total_costs = costs - costs * discount

print(f"{total_costs:.3f}")
