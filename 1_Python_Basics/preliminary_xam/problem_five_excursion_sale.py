number_of_sea_packages = int(input())
number_of_mountain_packages = int(input())

total_sales_sea = number_of_sea_packages * 680
total_sales_mountain = number_of_mountain_packages * 499

sea_sales_made = 0
mountain_sales_made = 0

command = ""
while command != "Stop":
    command = input()

    if command =="sea":
        if total_sales_sea > 0:
            sea_sales_made = sea_sales_made + 680
            total_sales_sea = total_sales_sea - 680
        else:
            sea_sales_made = sea_sales_made

    elif command == "mountain":
        if total_sales_mountain > 0:
            mountain_sales_made = mountain_sales_made + 499
            total_sales_mountain = total_sales_mountain - 499
        else:
            mountain_sales_made = mountain_sales_made

    if total_sales_sea + total_sales_mountain == 0:
        break

total_profit = sea_sales_made + mountain_sales_made

if total_sales_mountain == 0 and total_sales_sea == 0:
    print(f"Good job! Everything is sold.\nProfit: {total_profit} leva.")
else:
    print(f"Profit: {total_profit} leva.")
