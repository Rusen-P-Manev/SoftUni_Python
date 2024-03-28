chicken_meals = int(input()) * 10.35
fish_meals = int(input()) * 12.40
vegan_meals = int(input()) * 8.15

total_meal_price = chicken_meals + fish_meals + vegan_meals
total_price = total_meal_price + 2.5 + (total_meal_price * 0.2)

print(total_price)
