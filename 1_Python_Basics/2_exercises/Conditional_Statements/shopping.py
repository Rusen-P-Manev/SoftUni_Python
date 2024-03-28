budget = float(input())
number_of_video_cards = int(input())
number_of_processors = int(input())
number_of_ram_memmory = int(input())

video_cards_price = number_of_video_cards * 250
procesor_price = video_cards_price * 0.35
ram_memmory_price = video_cards_price * 0.10

total_parts_price = video_cards_price\
                    + number_of_processors * procesor_price\
                    + number_of_ram_memmory * ram_memmory_price

if number_of_video_cards > number_of_processors:
    total_parts_price *= 0.85
diference = abs(budget - total_parts_price)

if budget >= total_parts_price:
    print(f"You have {diference:.2f} leva left!")
else:
    print(f"Not enough money! You need {diference:.2f} leva more!")
