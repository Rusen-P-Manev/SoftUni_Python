# stocks = {}
#
# while True:
#     line = input()
#
#     if line == "statistics":
#         break
#
#     product, quantity = line.split(": ")
#     quantity = int(quantity)
#
#     if product in stocks:
#         stocks[product] += quantity
#     else:
#         stocks[product] = quantity
#
# product_count = len(stocks)
# total_quantity = sum(stocks.values())
#
# print("Products in stock:")
#
# for product, quantity in stocks.items():
#     print(f"- {product}: {quantity}")
#
# print(F"Total Products: {product_count}")
# print(f"Total Quantity: {total_quantity}")

stocks = {}

while True:
    command = input()

    if command == 'statistics':
        break

    product, quantity = command.split(': ')
    quantity = int(quantity)

    if product in stocks:
        stocks[product] += quantity
    else:
        stocks[product] = quantity

print('Products in stock:')

for prod, quant in stocks.items():
    print(f'- {prod}: {quant}')

print(f"Total Products: {len(stocks)}"
      f"\nTotal Quantity: {sum(stocks.values())}")
