import re

user_pass = input()
pass_as_list = list(user_pass)

while True:
    commands_and_data = input()
    if commands_and_data == 'Complete':
        break

    command = commands_and_data.split(' ')

    if commands_and_data[:-2] == 'Make Upper':
        index = int(command[2])
        if index in range(len(pass_as_list)):
            pass_as_list[index] = pass_as_list[index].upper()
            print(''.join(pass_as_list))

    elif commands_and_data[:-2] == 'Make Lower':
        index = int(command[2])
        if index in range(len(pass_as_list)):
            pass_as_list[index] = pass_as_list[index].lower()
            print(''.join(pass_as_list))

    if command[0] == 'Insert':
        index = int(command[1])
        char_to_insert = command[2]
        if index in range(len(pass_as_list)):
            pass_as_list.insert(index, char_to_insert)
            print(''.join(pass_as_list))

    if command[0] == 'Replace':
        character = command[1]
        value = int(command[2])
        new_char = chr(ord(character) + value)
        if character in pass_as_list:
            for index in range(len(pass_as_list)):
                if pass_as_list[index] == character:
                    pass_as_list[index] = new_char
            print(''.join(pass_as_list))

    if command[0] == 'Validation':

        if len(pass_as_list) < 8:
            print("Password must be at least 8 characters long!")

        if not any(char.isdigit() for char in pass_as_list):
            print("Password must consist at least one digit!")

        if not any(char.isupper() for char in pass_as_list):
            print("Password must consist at least one uppercase letter!")

        if not any(char.islower() for char in pass_as_list):
            print("Password must consist at least one lowercase letter!")

        if not re.search(r'^[\w-]*$', ''.join(pass_as_list)):
            print("Password must consist only of letters, digits and _!")
