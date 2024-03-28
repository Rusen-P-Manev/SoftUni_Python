sq_meters = float(input())
sq_price_total = sq_meters * 7.61
discount = sq_price_total * 0.18
final_price = sq_price_total - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")


