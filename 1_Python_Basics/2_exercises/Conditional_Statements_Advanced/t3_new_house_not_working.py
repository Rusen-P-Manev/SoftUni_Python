# Не работи като хората, да я прегледам! Грешката е цила в пропуснат знак в проверката >=
type_of_flowers = input()
count_of_flowers = int(input())
buddget = int(input())

rose = 5
dahlias = 3.80
tulip = 2.80
narciss = 3
gladiol = 2.5

# Не е лоша идея намаленията и увеличенията
# да са дадени в променливи, ако се налага
# да се сменят, ще е по-лесно. По аналог на цените.

total_costs_for_flowers = 0

if type_of_flowers == "Roses":
    if count_of_flowers > 80:
        total_costs_for_flowers = (count_of_flowers * rose) * 0.9
    else:
        total_costs_for_flowers = count_of_flowers * rose
elif type_of_flowers == "Dahlias":
    if count_of_flowers > 90:
        total_costs_for_flowers = (count_of_flowers * dahlias) * 0.85
    else:
        total_costs_for_flowers = count_of_flowers * dahlias
elif type_of_flowers == "Tulips":
    if count_of_flowers > 80:
        total_costs_for_flowers = (count_of_flowers * tulip) * 0.85
    else:
        total_costs_for_flowers = count_of_flowers * tulip
elif type_of_flowers == "Narcissus":
    if count_of_flowers < 120:
        total_costs_for_flowers = (count_of_flowers * narciss) * 1.15
    else:
        total_costs_for_flowers = count_of_flowers * narciss
elif type_of_flowers == "Gladiolus":
    if count_of_flowers < 80:
        total_costs_for_flowers = (count_of_flowers * gladiol) * 1.2
    else:
        total_costs_for_flowers = count_of_flowers * gladiol

differance = abs(total_costs_for_flowers - buddget)

if buddget >= total_costs_for_flowers:
    print(f"Hey, you have a great garden with {count_of_flowers} {type_of_flowers} "
          f"and {differance:.2f} leva left.")
else:
    print(f"Not enough money, you need {differance:.2f} leva more.")
