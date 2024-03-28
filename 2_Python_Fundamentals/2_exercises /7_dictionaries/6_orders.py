products_list = {}

while True:
    command = input()

    if command == 'buy':
        for key, val in products_list.items():
            print(f'{key} -> {(val[0] * val[1]):.2f}')
        break

    product_name, price, quantity = command.split(' ')
    product_price = float(price)
    product_quuantity = int(quantity)

    if product_name not in products_list.keys():
        products_list[product_name] = [product_price, product_quuantity]
    elif product_name in products_list.keys():
        products_list[product_name][1] += product_quuantity
        if products_list[product_name][0] != product_price:
            products_list[product_name][0] = product_price
