value_of_the_voucher = int(input())

number_of_tickets = 0
number_of_purchases = 0
vaucher_value_left = value_of_the_voucher

command = ""

while command != "End":
    command = input()

    firs_char = ord(command[0])
    second_char = ord(command[1])

    if len(command) > 8 and command != "End":
        ticket_price = firs_char + second_char
        if ticket_price <= vaucher_value_left:
            number_of_tickets += 1
            vaucher_value_left = vaucher_value_left - ticket_price
        else:
            command = "End"
    elif len(command) <= 8 and command != "End":
        purchase_price = firs_char
        if purchase_price <= vaucher_value_left:
            number_of_purchases += 1
            vaucher_value_left = vaucher_value_left - purchase_price
        else:
            command = "End"
print(f"{number_of_tickets}\n{number_of_purchases}")

