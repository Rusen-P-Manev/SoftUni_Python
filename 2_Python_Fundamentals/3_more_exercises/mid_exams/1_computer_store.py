all_purchased_parts = []

while True:
    command = input()
    if command != "regular" and command != "special":
        part_price = float(command)

        if part_price >= 0:
            all_purchased_parts.append(part_price)

        elif part_price < 0:
            print("Invalid price!")

    else:
        if sum(all_purchased_parts) == 0:
            print("Invalid order!")
            break
        else:
            final_sum = sum(all_purchased_parts)
            taxes = final_sum * 0.2
            total_price_with_taxes = final_sum + taxes

            if command == "special":
                total_price_with_taxes -= total_price_with_taxes * 0.1

        print(f"Congratulations you've just bought a new computer!\n"
              f"Price without taxes: {final_sum:.2f}$\n"
              f"Taxes: {taxes:.2f}$\n"
              f"-----------\n"
              f"Total price: {total_price_with_taxes:.2f}$")
        break




# total_price = 0
# print_type = ''
# while True:
#     command = input()
#     if command != 'special' and command != 'regular':
#         part_price = float(command)
#
#         if part_price >= 0:
#             total_price += part_price
#         else:
#             print("Invalid price!")
#     else:
#         print_type = command
#         break
#
# if total_price == 0:
#     print('Invalid order!')
# else:
#     taxes = total_price * 0.2
#     vat_price = total_price + taxes
#
#     if print_type == 'special':
#         vat_price -= vat_price * 0.1
#
#     print(f"Congratulations you've just bought a new computer!\n"\
#            f"Price without taxes: {total_price:.2f}$\n"\
#            f"Taxes: {taxes:.2f}$\n"\
#            f"-----------\n"\
#            f"Total price: {vat_price:.2f}$")
