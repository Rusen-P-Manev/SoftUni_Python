city = input()
sales_volume = float(input())
commision = 0

# Променливата е булева и е константна величина е с главни букви.
# Ако в някакъв момент от задачата се въведе грешен град или отрицателно
# число(т.е. изън зададените диапазини за обем на продажбите т.е. отрицтелни продажби)
# тогава тази променлива ще се задейства и от false ще стане true.
# Ще се включи при въвеждане на невалиден град или обем на продажбите.
ERR_DATA = False

if city == "Sofia":
    if 0 <= sales_volume <= 500:
        commision = sales_volume * 0.05
    elif 500 < sales_volume <= 1000:
        commision = sales_volume * 0.07
    elif 1000 < sales_volume <= 10000:
        commision = sales_volume * 0.08
    elif sales_volume > 10000:
        commision = sales_volume * 0.12
    else:
        ERR_DATA = True

elif city == "Varna":
    if 0 <= sales_volume <= 500:
        commision = sales_volume * 0.045
    elif 500 < sales_volume <= 1000:
        commision = sales_volume * 0.075
    elif 1000 < sales_volume <= 10000:
        commision = sales_volume * 0.1
    elif sales_volume > 10000:
        commision = sales_volume * 0.13
    else:
        ERR_DATA = True

elif city =="Plovdiv":
    if 0 <= sales_volume <= 500:
        commision = sales_volume * 0.055
    elif 500 < sales_volume <= 1000:
        commision = sales_volume * 0.08
    elif 1000 < sales_volume <= 10000:
        commision = sales_volume * 0.12
    elif sales_volume > 10000:
        commision = sales_volume * 0.145
    else:
        ERR_DATA = True
else:
    ERR_DATA = True
    # Презаписва ERR_DATA с True, ако никое от условията по - горе не е изпълнено
    # - т.е. има въведени грешен град и/или обем на продажбите.

if not ERR_DATA:
    print(f"{commision:.2f}")
else:
    print("error")