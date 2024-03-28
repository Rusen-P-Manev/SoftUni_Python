weapon_name = input().split('|')
element_check_even = []
element_check_odd = []

while True:
    command_and_data = input()
    if command_and_data == 'Done':
        print(f"You crafted {''.join(weapon_name)}!")
        break

    command = command_and_data.split()[0]

    if command == 'Add':
        index = int(command_and_data.split()[2])
        particle = command_and_data.split()[1]
        if index in range(len(weapon_name)):
            weapon_name.insert(index,particle)

    elif command == 'Remove':
        index = int(command_and_data.split()[1])
        if index in range(len(weapon_name)):
            weapon_name.pop(index)

    if command_and_data == 'Check Even':
        for element in range(len(weapon_name)):
            if element % 2 == 0:
                element_check_even.append(weapon_name[element])
        print(' '.join(element_check_even))

    elif command_and_data == 'Check Odd':
        for element in range(len(weapon_name)):
            if element % 2 != 0:
                element_check_odd.append(weapon_name[element])
        print(' '.join(element_check_odd))
