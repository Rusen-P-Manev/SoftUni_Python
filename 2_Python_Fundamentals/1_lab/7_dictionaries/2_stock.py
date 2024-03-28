stock_data = input().split()
searched_product = input().split()

stock_database = {}

for i in range(0, len(stock_data), 2):
    product = stock_data[i]
    quantity = int(stock_data[i + 1])
    stock_database[product] = quantity

for needet_product in searched_product:
    if needet_product in stock_database:
        print(f"We have {stock_database[needet_product]} of {needet_product} left")
    else:
        print(f"Sorry, we don't have {needet_product}")
