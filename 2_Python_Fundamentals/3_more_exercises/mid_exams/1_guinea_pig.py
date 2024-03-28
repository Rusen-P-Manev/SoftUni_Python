# ресурси за 30 дни

food_monthly = float(input())
hay_monthly = float(input())
cover_monthly = float(input())
pigs_weight = float(input())

food_in_grams = food_monthly * 1000
hay_in_grams = hay_monthly * 1000
cover_in_grams = cover_monthly * 1000

for day in range(1, 31):
    food_in_grams -= 300

    if day % 2 == 0:
        hay_in_grams -= food_in_grams * 0.05
    if day % 3 == 0:
        cover_in_grams -= ((pigs_weight * 1000) / 3)

    if food_in_grams <= 0 or hay_in_grams <= 0 or cover_in_grams <= 0:
        print("Merry must go to the pet store!")
        break
    elif day == 30:
        print(f"Everything is fine! Puppy is happy! "
              f"Food: {(food_in_grams / 1000):.2f}, "
              f"Hay: {(hay_in_grams / 1000):.2f}, "
              f"Cover: {(cover_in_grams /1000):.2f}.")


