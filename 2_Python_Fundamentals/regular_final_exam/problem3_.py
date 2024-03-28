heroes_data = {}

while True:
    current_hero_data = input()

    if current_hero_data == 'End':
        break

    hero_state = current_hero_data.split(' ')
    command = hero_state[0]
    hero_name = hero_state[1]
    spell_name = ''

    if command == 'Enroll':

        if hero_name not in heroes_data:
            heroes_data[hero_name] = []
        else:
            print(f'{hero_name} is already enrolled.')

    elif command == 'Learn':
        spell_name = hero_state[2]

        if (hero_name in heroes_data) and (spell_name not in heroes_data[hero_name]):
            heroes_data[hero_name].append(spell_name)
        elif (hero_name in heroes_data) and (spell_name in heroes_data[hero_name]):
            print(f'{hero_name} has already learnt {spell_name}.')
        else:
            print(f"{hero_name} doesn't exist.")

    elif command == 'Unlearn':
        spell_name = hero_state[2]

        if hero_name not in heroes_data:
            print(f"{hero_name} doesn't exist.")
        elif spell_name not in heroes_data[hero_name]:
            print(f"{hero_name} doesn't know {spell_name}.")
        else:
            heroes_data[hero_name].remove(spell_name)


print('Heroes:')
for key, val in heroes_data.items():
    print(f"== {key}: {', '.join(val)}")
