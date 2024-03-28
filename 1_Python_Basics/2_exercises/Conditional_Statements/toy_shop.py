price_tour = float(input())
number_of_puzzls = int(input())
number_of_dolls = int(input())
number_of_bears = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())
puzzle = 2.6
doll = 3
bear = 4.1
minion = 8.2
truck = 2
total_sum = number_of_puzzls * puzzle\
            + number_of_dolls * doll\
            + number_of_bears * bear\
            + number_of_minions * minion\
            + number_of_trucks * truck
total_number_of_tous = number_of_puzzls\
             + number_of_dolls\
             + number_of_bears\
             + number_of_minions\
             + number_of_trucks
if total_number_of_tous >= 50:
    total_sum = total_sum * 0.75 # total_sum +== 0.75
total_sum = total_sum * 0.9 # total_sum *= 0.9
diference = abs(total_sum - price_tour) # abs връща абсолютна стойност
if total_sum >= price_tour:
    print(f"Yes! {diference:.2f} lv left.")
else:
    print(f"Not enough money! {diference:.2f} lv needed.")

