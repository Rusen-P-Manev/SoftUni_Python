luggage_price_over_twety_kilograms = float(input())
weight_of_luggage = float(input())
days_until_flight = int(input())
number_of_luggage = int(input())

current_luggage_ptice = 0

if weight_of_luggage < 10:
    current_luggage_ptice = luggage_price_over_twety_kilograms * 0.20
elif 10 <= weight_of_luggage <= 20:
    current_luggage_ptice = luggage_price_over_twety_kilograms * 0.50
elif weight_of_luggage > 20:
    current_luggage_ptice = luggage_price_over_twety_kilograms

if days_until_flight > 30:
    current_luggage_ptice *= 1.10
elif 7 <= days_until_flight <= 30:
    current_luggage_ptice *= 1.15
elif days_until_flight < 7:
    current_luggage_ptice *= 1.40

total_luggage_price = current_luggage_ptice * number_of_luggage

print(f" The total price of bags is: {total_luggage_price:.2f} lv. ")