max_bad_grades = int(input())
average_grade = 0
total_sloved_problems = 0
bad_grades_counter = 0
last_problemm_name = ""
is_faild = False

current_problem = input()
while current_problem != "Enough":
    current_grade = int(input())
    if current_grade <= 4:
        bad_grades_counter += 1
        if bad_grades_counter == max_bad_grades:
            is_faild = True
            break
    average_grade += current_grade
    total_sloved_problems += 1
    last_problemm_name = current_problem
    current_problem = input()
if is_faild:
   print(f"You need a break, {max_bad_grades} poor grades.")
else:
    average_grade /= total_sloved_problems
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {total_sloved_problems}")
    print(f"Last problem: {last_problemm_name}")