price_of_tshirt = float(input())
amount_to_reach = float(input())

short_price = price_of_tshirt * 0.75
socks_price = short_price * 0.20
buttons_price = (price_of_tshirt + short_price) * 2

discount = 0.15
final_costs = (short_price + socks_price + buttons_price + price_of_tshirt) * 0.85
difference = abs(final_costs - amount_to_reach)

if final_costs >= amount_to_reach:
    print(f"Yes, he will earn the world-cup replica ball!\nHis sum is {final_costs:.2f} lv.")
else:
    print(f"No, he will not earn the world-cup replica ball.\nHe needs {difference:.2f} lv. more.")
