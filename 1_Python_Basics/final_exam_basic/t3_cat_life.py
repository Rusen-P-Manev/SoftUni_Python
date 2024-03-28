cat_breed = input()
gender = input()
year_to_live = 0

if cat_breed == "British Shorthair":
    if gender == "m":
        year_to_live = 13
    else:
        year_to_live = 14

elif cat_breed == "Siamese":
    if gender == "m":
        year_to_live = 15
    else:
        year_to_live = 16

elif cat_breed == "Persian":
    if gender == "m":
        year_to_live = 14
    else:
        year_to_live = 15

elif cat_breed == "Ragdoll":
    if gender == "m":
        year_to_live = 16
    else:
        year_to_live = 17

elif cat_breed == "American Shorthair":
    if gender == "m":
        year_to_live = 12
    else:
        year_to_live = 13

elif cat_breed == "Siberian":
    if gender == "m":
        year_to_live = 11
    else:
        year_to_live = 12

in_cat_monts = int((year_to_live * 12) / 6)

if cat_breed == "British Shorthair" or cat_breed == "Siamese" or cat_breed == "Persian"\
        or cat_breed == "Ragdoll" or cat_breed == "American Shorthair" or cat_breed == "Siberian":
    print(f"{in_cat_monts} cat months")
else:
    print(f"{cat_breed} is invalid cat!")