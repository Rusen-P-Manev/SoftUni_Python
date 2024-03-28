dungeons_rooms = input().split('|')
current_roorm = 0
bitcoins = 0
health = 100

for room in dungeons_rooms:
    current_roorm += 1
    game_actions = room.split()
    command = game_actions[0]
    value = int(game_actions[1])

    if command == 'potion':
        health_points = value
        if health + value > 100:
            health_points = 100 - health
            health = 100
        else:
            health += health_points
        print(f"You healed for {health_points} hp.")
        print(f"Current health: {health} hp.")
    elif command == 'chest':
        bitcoins += value
        print(f"You found {value} bitcoins.")
    else:
        health -= value
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {current_roorm}")
            break
if health > 0:
    print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
