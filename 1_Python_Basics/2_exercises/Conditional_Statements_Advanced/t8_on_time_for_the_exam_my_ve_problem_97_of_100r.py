hour_of_exam_start = int(input())
minutes_of_exam_start = int(input())
hour_of_arriving = int(input())
minutes_of_arriving = int(input())

starting_time = hour_of_exam_start * 60 + minutes_of_exam_start
arriving_time = hour_of_arriving * 60 + minutes_of_arriving
difference = abs(starting_time - arriving_time)
hours = difference // 60
minutes = difference % 60

if (starting_time - 30 <= arriving_time <= starting_time):
    print(f"On time")
    if difference < 60:
        print(f"{minutes} minutes before the start")

elif arriving_time > starting_time:
    print(f"Late")
    if difference < 60:
        print(f"{minutes} minutes after the start")
    elif difference > 60:
        print(f"{hours}:{minutes:02d} hours after the start")
else:
    print(f"Early")
    if difference < 60:
        print(f"{minutes} minutes before the start")
    elif difference >= 60:
        print(f"{hours}:{minutes:02d} hours before the start")
