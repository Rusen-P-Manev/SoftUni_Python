# Trygna, da pomislq kak moje da se napishe po - dobre.
# Ще е по - добре да се напише по месеци а не по брой нощувки
# Да помисля дали могат да се съкратят изчисленията ако въведа променлива за итстъпка
month = input()
number_of_nights = int(input())

final_price_studio = 0
final_price_apartment = 0
ERR_DATA = False

if number_of_nights > 14:
    if month == "May" or month == "October":
        final_price_studio = (number_of_nights * 50) * 0.70
        final_price_apartment = (number_of_nights * 65) * 0.90
    elif month == "June" or month == "September":
        final_price_studio = (number_of_nights * 75.20) * 0.80
        final_price_apartment = (number_of_nights * 68.70) * 0.90
    elif month == "July" or month == "August":
        final_price_studio = (number_of_nights * 76)
        final_price_apartment = (number_of_nights * 77) * 0.90
    else:
        ERR_DATA = True
elif number_of_nights > 7 and (month == "May" or month == "October"):
        final_price_studio = (number_of_nights * 50) * 0.95
        final_price_apartment = number_of_nights * 65
elif month == "May" or month == "October":
        final_price_studio = (number_of_nights * 50)
        final_price_apartment = number_of_nights * 65
elif month == "June" or month == "September":
        final_price_studio = number_of_nights * 75.20
        final_price_apartment = number_of_nights * 68.70
elif month == "July" or month == "August":
        final_price_studio = number_of_nights * 76
        final_price_apartment = number_of_nights * 77
else:
    ERR_DATA = True

if not ERR_DATA:
    print(f"Apartment: {final_price_apartment:.2f} lv.\n"
          f"Studio: {final_price_studio:.2f} lv.")
else:
    pass

