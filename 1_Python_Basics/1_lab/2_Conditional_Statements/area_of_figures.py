from math import pi
figure = input()
area = 0 # Това е глобална променлива. и спестява принтирането на area за вска фигура.
# Презаписва се за всяка фигура автоматично. Живот на променливата.

if figure == "square":
    a = float(input())
    area = a * a

elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b

elif figure == "circle":
    r = float(input())
    area = (r ** 2) * pi

elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = (a/2) * h

print(f"{area:.3f}")


