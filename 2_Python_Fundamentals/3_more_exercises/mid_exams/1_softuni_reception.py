first_employee = int(input())
second_employee = int(input())
third_employee = int(input())

number_of_students = int(input())
needed_time = 0

while number_of_students > 0:
    needed_time += 1
    if needed_time % 4 == 0:
        continue

    number_of_students -= first_employee
    number_of_students -= second_employee
    number_of_students -= third_employee

print(f"Time needed: {needed_time}h.")



