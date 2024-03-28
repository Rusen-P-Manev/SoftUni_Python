number_of_joinery = int(input())
type_of_joinery = input()
shipment_method  = input()

ninety_by_hundred_and_thirty_price = 110
hundred_by_hundred_and_fifty_price = 140
hundred_and_thirty_by_hundred_and_eighty_price = 190
two_hundred_by_three_hundred_price = 250
delivery_price = 60

order_total_value = 0

if type_of_joinery == "90X130" and number_of_joinery > 10:
    order_total_value = number_of_joinery * ninety_by_hundred_and_thirty_price
    if number_of_joinery > 60:
        order_total_value *= 0.92
    elif 30 < number_of_joinery <= 60:
        order_total_value *= 0.95

elif type_of_joinery == "100X150" and number_of_joinery > 10:
    order_total_value = number_of_joinery * hundred_by_hundred_and_fifty_price
    if number_of_joinery > 80:
        order_total_value *= 0.90
    elif 40 < number_of_joinery <= 80:
        order_total_value *= 0.94

elif type_of_joinery == "130X180" and number_of_joinery > 10:
    order_total_value = number_of_joinery * hundred_and_thirty_by_hundred_and_eighty_price
    if number_of_joinery > 50:
        order_total_value *= 0.88
    elif 20 < number_of_joinery <= 50:
        order_total_value *= 0.93

elif type_of_joinery == "200X300" and number_of_joinery > 10:
    order_total_value = number_of_joinery * two_hundred_by_three_hundred_price
    if number_of_joinery > 50:
        order_total_value *= 0.86
    elif 25 < number_of_joinery <= 50:
        order_total_value *= 0.91

if number_of_joinery <= 10:
    print("Invalid order")
elif shipment_method == "With delivery":
    order_total_value += 60
    if number_of_joinery >= 100:
        order_total_value *= 0.96
    elif number_of_joinery < 100:
        order_total_value = order_total_value
    print(f"{order_total_value:.2f} BGN")
elif shipment_method == "Without delivery":
    order_total_value = order_total_value
    print(f"{order_total_value:.2f} BGN")
