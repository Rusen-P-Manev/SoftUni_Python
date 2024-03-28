values_to_modify = [int(val) for val in input().split(' ')]

while True:
    command_and_data = input()
    if command_and_data == 'end':
        print(', '.join([str(ele) for ele in values_to_modify]))
        break
    commands = command_and_data.split(' ')
    command = commands[0]

    if command == 'swap':
        first_index = int(commands[1])
        second_index = int(commands[2])
        values_to_modify[first_index], values_to_modify[second_index] = values_to_modify[second_index], values_to_modify[first_index]
    elif command == 'multiply':
        first_number = int(commands[1])
        second_number = int(commands[2])
        result = values_to_modify[first_number] * values_to_modify[second_number]
        values_to_modify.pop(first_number)
        values_to_modify.insert(first_number, result)
    elif command == 'decrease':
        decreaseed_values = []
        for element in values_to_modify:
            new_element = element - 1
            decreaseed_values.append(new_element)
            values_to_modify = decreaseed_values