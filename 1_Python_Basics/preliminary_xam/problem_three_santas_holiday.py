days_to_stay = int(input())
type_of_room = input()
rating = input()

number_of_nights = days_to_stay - 1
room_per_ine_price_per_night = 18.00
apartment_price_per_night = 25.00
president_apartment_per_night = 35.00

costs_of_stay = 0
final_price = 0

if type_of_room == "apartment":
    if number_of_nights < 10:
        costs_of_stay = number_of_nights * apartment_price_per_night * 0.7
    elif number_of_nights > 15:
        costs_of_stay = number_of_nights * apartment_price_per_night * 0.5
    else:
        costs_of_stay = number_of_nights * apartment_price_per_night * 0.65

if type_of_room == "president apartment":
    if number_of_nights < 10:
        costs_of_stay = number_of_nights * president_apartment_per_night * 0.9
    elif number_of_nights > 15:
        costs_of_stay = number_of_nights * president_apartment_per_night * 0.8
    else:
        costs_of_stay = number_of_nights * president_apartment_per_night * 0.85

if type_of_room == "room for one person":
    costs_of_stay = number_of_nights * room_per_ine_price_per_night

if rating == "positive":
    costs_of_stay = costs_of_stay * 1.25
elif rating == "negative":
    costs_of_stay = costs_of_stay * 0.9

print(f"{costs_of_stay:.2f}")
