#  Тази задача мина да разбера защо мояра весия
#  не работи и да разуча тази като синтаксис

exam_hours = int(input())
exam_minutes = int(input())
arriving_hours = int(input())
arriving_minutes = int(input())

late = "late"
on_time = "On time"
early = "Early"

exam_start_time = (exam_hours * 60) + exam_minutes
arrival_time = (arriving_hours * 60) + arriving_minutes
total_minutes_difference = arrival_time - exam_start_time

student_arrival = late
if total_minutes_difference < -30:
    student_arrival = early
elif total_minutes_difference <= 0:
    student_arrival = on_time

result = ""
if total_minutes_difference != 0:
    hours_difference = abs(total_minutes_difference) // 60
    minutes_difference = abs(total_minutes_difference) % 60

    if hours_difference > 0:
        result = \
            f"{hours_difference}:{minutes_difference:02d} hours"
    else:
        result = f"{minutes_difference} minutes"

    if total_minutes_difference < 0:
        result += " before the start"
    else:
        result += " after the start"
print(student_arrival)
if result:
    print(result)
