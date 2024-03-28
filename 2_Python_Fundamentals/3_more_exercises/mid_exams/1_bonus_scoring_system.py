# import math
# count_of_the_students = int(input())
# count_of_the_lectures = int(input())
# initial_bonus = int(input())
# high_bonus = 0
# high_attendances = 0
#
# for i in range(count_of_the_students):
#     attendances_for_each = int(input())
#     total_bonus = attendances_for_each / count_of_the_lectures * (5 + initial_bonus)
#     if high_bonus < total_bonus:
#         high_bonus = total_bonus
#         high_attendances = attendances_for_each
#
# print(f"Max Bonus: {math.ceil(high_bonus)}.")
# print(f"The student has attended {high_attendances} lectures.")


from math import ceil
number_of_students = int(input())
number_lectures = int(input())
additional_bonus = int(input())
# Списъците не трябва да са празни заради max() --> гърми()
# Не може да има празен лист в max()
max_attindance = [0]
max_bonus_points = [0]

for _ in range(number_of_students):
    student_attendances = int(input())
    max_attindance.append(student_attendances)

    bonus_points = ((student_attendances / number_lectures)
                    * (5 + additional_bonus))
    max_bonus_points.append(bonus_points)

print(f"Max Bonus: {ceil(max(max_bonus_points))}.")
print(f"The student has attended {max(max_attindance)} lectures.")
