vacation_days = int(input())
buddget = float(input())
number_of_people = int(input())
fuel_price_per_kilometer = float(input())
food_expenses_per_person_daily = float(input())
room_price_per_person = float(input())

total_food_costs = (vacation_days
                    * number_of_people
                    * food_expenses_per_person_daily)
hotel_total_costs = (vacation_days
                     * number_of_people
                     * room_price_per_person)

if number_of_people > 10:
    hotel_total_costs *= 0.75

total_price = total_food_costs + hotel_total_costs

for day in range(1, vacation_days + 1):
    kilometers_per_day = float(input())
    dayly_travel_cost = kilometers_per_day * fuel_price_per_kilometer
    total_price += dayly_travel_cost

    if day % 3 == 0 or day % 5 == 0:
        total_price *= 1.4
    if day % 7 == 0:
        total_price -= (total_price / number_of_people)
    if total_price > buddget:
        print(f"Not enough money to continue the trip. "
              f"You need {abs(total_price - buddget):.2f}$ more.")
        break

if buddget >= total_price:
    print(f"You have reached the destination. "
          f"You have {(buddget - total_price):.2f}$ budget left.")

