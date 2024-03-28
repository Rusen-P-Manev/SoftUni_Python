tank_length = int(input())
tank_width = int(input())
tank_height = int(input())
percentage_full = float(input())

tank_volume = tank_length * tank_width * tank_height \
              * 0.001 * (1 - percentage_full / 100)
print(tank_volume)