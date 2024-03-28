number_of_users = int(input())

database = {}

for _ in range(number_of_users):

    user_details = input().split(' ')

    command = user_details[0]
    username = user_details[1]


    if command == 'register':
        license_plate_number = user_details[2]
        if username not in database:
            database[username] = license_plate_number
            print(f'{username} registered {license_plate_number} successfully')
        else:
            print(f'ERROR: already registered with plate number {license_plate_number}')

    elif command == 'unregister':
        if username not in database:
            print(f'ERROR: user {username} not found')
        else:
            database.pop(username)
            print(f'{username} unregistered successfully')

for key, val in database.items():
    print(f'{key} => {val}')