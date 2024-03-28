type_of_plant = input()

if type_of_plant == "banana"\
        or type_of_plant == "apple"\
        or type_of_plant == "kiwi"\
        or type_of_plant == "cherry"\
        or type_of_plant == "lemon"\
        or type_of_plant == "grapes":
    print("fruit")
elif type_of_plant == "tomato"\
        or type_of_plant == "cucumber"\
        or type_of_plant == "pepper"\
        or type_of_plant == "carrot":
    print("vegetable")
else:
    print("unknown")