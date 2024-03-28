buddget = float(input())
season = input()

destination = ""
rest_type = ""
spendet_sum = 0

if buddget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        spendet_sum = buddget * 0.3
    else:
        spendet_sum = buddget * 0.7

elif buddget <= 1000:
    destination = "Balkans"
    if season == "summer":
        spendet_sum = buddget * 0.4
    else:
        spendet_sum = buddget * 0.8
else:
    destination = "Europe"
    spendet_sum = buddget * 0.9

if season == "summer" and destination != "Europe":
    rest_type = "Camp"
else:
    rest_type = "Hotel"

print(f"Somewhere in {destination} \n"
      f"{rest_type} - {spendet_sum:.2f}")