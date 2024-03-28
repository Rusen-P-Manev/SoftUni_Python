number_of_adults = 0
number_of_kids = 0

while True:
    command = input()
    total_money_toys = number_of_kids * 5
    total_money_sweaters = number_of_adults * 15
    if command == "Christmas":
        print(f"Number of adults: {number_of_adults}\nNumber of kids: {number_of_kids}")
        print(f"Money for toys: {total_money_toys}\nMoney for sweaters: {total_money_sweaters}")
        break
    age = int(command)
    if age <= 16:
        number_of_kids += 1
    else:
        number_of_adults += 1