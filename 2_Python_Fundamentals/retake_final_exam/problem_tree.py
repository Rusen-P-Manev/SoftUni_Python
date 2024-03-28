players_database = {}

while True:
    data_and_commands = input().split(':')

    if data_and_commands[0] == 'Results':
        break

    command = data_and_commands[0]

    if command == 'Add':
        persone_name = data_and_commands[1]
        health = int(data_and_commands[2])
        energy = int(data_and_commands[3])

        if persone_name not in players_database:
            players_database[persone_name] = [health, energy]

        else:
            players_database[persone_name][0] += health

    elif command == 'Attack':
        attacher_name = data_and_commands[1]
        defender_name = data_and_commands[2]
        damage = int(data_and_commands[3])

        if attacher_name in players_database and defender_name in players_database:
            players_database[attacher_name][1] -= 1
            players_database[defender_name][0] -= damage

            if players_database[defender_name][0] <= 0:
                del players_database[defender_name]
                print(f"{defender_name} was disqualified!")

            if players_database[attacher_name][1] <= 0:
                del players_database[attacher_name]
                print(f"{attacher_name} was disqualified!")

    elif command == 'Delete':
        dell_command = data_and_commands[1]

        if dell_command == 'All':
            players_database.clear()

        else:
            if dell_command in players_database:
                del players_database[dell_command]

print(f"People count: {len(players_database.keys())}")

if len(players_database.keys()) > 0:
    for key, val in players_database.items():
        print(f'{key} - {val[0]} - {val[1]}')
