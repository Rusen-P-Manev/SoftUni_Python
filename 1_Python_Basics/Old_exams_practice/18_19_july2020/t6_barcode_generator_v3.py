number_one = int(input())
number_two = int(input())
for number_to_check in range(number_one, number_two + 1):
    print_condition = True
    current_number_as_string = str(number_to_check)
    current_symbol = 0
    for current_letter in current_number_as_string:
        current_symbol = int(current_letter)
        if current_symbol % 2 == 0:
            print_condition = False
    if print_condition:
        print(number_to_check, end=' ')