age = float(input())
gender = input()

if gender == "m" and age >= 16:
    print("Mr.")
elif gender == "m" and age < 16:
    print("Master")
# Проверката за М може да бъде направена, акто проверката за жена.
# Горнияят пример е с логически оператори, а долният с вложени цикли.
# Вложените цикли е хубаво да се избягват, когато е възможно, и да не са повече от 3....
elif gender == "f":
    if age >= 16:
        print("Ms.")
    else:
        print("Miss")
