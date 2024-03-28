stop_condition = False

while not stop_condition:
    your_added_number = float(input())

    if 1 <= your_added_number <= 100:
        print(f"The number {your_added_number} is between 1 and 100")
        stop_condition = True
