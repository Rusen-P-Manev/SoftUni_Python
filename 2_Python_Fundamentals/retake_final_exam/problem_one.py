strig_container = []
indexes_container = []

while True:
    commands_and_data = input()
    if commands_and_data == 'End':
        break

    command = commands_and_data.split()[0]

    if command == 'Add':
        substring = commands_and_data.split()[1]
        strig_container += [char for char in substring]

    elif command == 'Upgrade':
        character = commands_and_data.split()[1]
        next_char = chr(ord(character) + 1)
        for index in range(len(strig_container)):
            if strig_container[index] == character:
                strig_container[index] = next_char

    elif command == 'Print':
        print(''.join(strig_container))

    elif command == 'Index':
        character_to_convert = commands_and_data.split()[1]
        if character_to_convert in ''.join(strig_container):
            for index in range(len(strig_container)):
                if strig_container[index] == character_to_convert:
                    indexes_container.append(index)
            print(' '.join([str(ch) for ch in indexes_container]))
        else:
            print('None')

    elif command == 'Remove':
        sub_string = commands_and_data.split()[1]
        string_to_clean = ''.join(strig_container)
        if sub_string in string_to_clean:
            while sub_string in string_to_clean:
                string_to_clean = string_to_clean.replace(sub_string, '')
            strig_container.clear()
            strig_container += [char for char in string_to_clean]

