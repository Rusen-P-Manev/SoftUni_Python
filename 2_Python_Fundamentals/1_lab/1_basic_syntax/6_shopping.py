buddget = int(input())

items_total_costs = 0
condition = False

while True:
    command = input()
    if command == "End":
        break
    item_price = int(command)
    condition = False
    items_total_costs += item_price

    if buddget < items_total_costs:
        print("You went in overdraft!")
        break
    else:
        condition = True

if condition:
    print("You bought everything needed.")
