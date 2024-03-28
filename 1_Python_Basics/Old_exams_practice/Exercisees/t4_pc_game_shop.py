number_sold_games = int(input())
# counters
hearthstone_counter = 0
fornite_counter = 0
overwatch_counter = 0
Others_counter = 0

for _ in range(number_sold_games):
    game_name = input()
    for