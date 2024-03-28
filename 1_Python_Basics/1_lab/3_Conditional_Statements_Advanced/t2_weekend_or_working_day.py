day_of_weak = input()
if day_of_weak == "Monday" or day_of_weak == "Tuesday" or day_of_weak == "Wednesday" \
        or day_of_weak == "Thursday"  or day_of_weak == "Friday":
    print("Working day")
elif day_of_weak == "Saturday" or day_of_weak == "Sunday":
    print("Weekend")
else:
    print("Error")