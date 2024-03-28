item = input()
city = input()
quantity = float(input())

price = 0

if city == "Sofia":
    if item == "coffee":
        price = 0.5
    elif item == "water":
        price = 0.80
    elif item == "beer":
        price = 1.20
    elif item == "sweets":
        price = 1.45
    elif item == "peanuts":
        price = 1.60
elif city == "Plovdiv":
    if item == "coffee":
        price = 0.40
    elif item == "water":
        price = 0.70
    elif item == "beer":
        price = 1.15
    elif item == "sweets":
        price = 1.30
    elif item == "peanuts":
        price = 1.50
elif city == "Varna":
    if item == "coffee":
        price = 0.45
    elif item == "water":
        price = 0.70
    elif item == "beer":
        price = 1.10
    elif item == "sweets":
        price = 1.35
    elif item == "peanuts":
        price = 1.55

yours_bill_is = price * quantity
print(yours_bill_is)
