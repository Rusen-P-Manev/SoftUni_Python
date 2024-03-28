number_of_pens = int(input()) * 5.80
number_of_markers = int(input()) * 7.20
liters_of_detergent = int(input()) * 1.2
discount = int(input()) / 100

total_costs = (number_of_pens + number_of_markers + liters_of_detergent)
final_sum_to_pay = total_costs - (total_costs * discount)
print(final_sum_to_pay)
# Да видя как сме го рещшили на УПР и да си препища онзи вариант....