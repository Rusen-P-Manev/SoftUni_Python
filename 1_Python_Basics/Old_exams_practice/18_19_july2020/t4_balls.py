from math import floor
number_of_balls = int(input())

total_points = 0
red_balls_counter = 0
orange_balls_counter = 0
yellow_balls_counter = 0
white_balls_counter = 0
other_colors_picked_counter = 0
divides_from_black_balls = 0

for _ in range(number_of_balls):
    current_colir = input()
    if current_colir == "red":
        total_points += 5
        red_balls_counter += 1
    elif current_colir == "orange":
        total_points += 10
        orange_balls_counter += 1
    elif current_colir == "yellow":
        total_points += 15
        yellow_balls_counter += 1
    elif current_colir == "white":
        total_points += 20
        white_balls_counter += 1
    elif current_colir == "black":
        total_points = floor(total_points / 2)
        divides_from_black_balls += 1
    else:
        other_colors_picked_counter += 1

print(f"Total points: {total_points}")
print(f"Red balls: {red_balls_counter}")
print(f"Orange balls: {orange_balls_counter}")
print(f"Yellow balls: {yellow_balls_counter}")
print(f"White balls: {white_balls_counter}")
print(f"Other colors picked: {other_colors_picked_counter}")
print(f"Divides from black balls: {divides_from_black_balls}")
