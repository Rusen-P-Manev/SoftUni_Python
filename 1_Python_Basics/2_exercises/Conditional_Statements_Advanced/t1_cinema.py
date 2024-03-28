projection_type = input()
number_of_rows = int(input())
number_of_columns = int(input())

total_places = number_of_rows * number_of_columns
ticket_price = 0

if projection_type == "Premiere":
    ticket_price = 12
elif projection_type == "Normal":
    ticket_price = 7.50
elif projection_type == "Discount":
    ticket_price = 5

total_income = total_places * ticket_price

print(f"{total_income:.2f} leva")
