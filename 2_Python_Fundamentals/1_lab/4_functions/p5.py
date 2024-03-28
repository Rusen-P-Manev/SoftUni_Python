def sum_bill(product, quantity):

    result = 0

    if product == 'coffee':
        result = 1.50 * quantity
    elif product == 'water':
        result = 1 * quantity
    elif product == 'coke':
        result = 1.40 * quantity
    elif product == 'snacks':
        result = 2 * quantity

    return result


product_input = input()
quantity = int(input())

final = sum_bill(product_input, quantity)
print(f'{final:.2f}')
