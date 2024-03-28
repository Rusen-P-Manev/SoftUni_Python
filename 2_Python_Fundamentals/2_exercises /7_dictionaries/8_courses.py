database = {}

while True:
    data = input()

    if data == 'end':
        for course, students in database.items():
            print(f'{course}: {len(students)}')
            for student in students:
                print(f'-- {student}')
        break

    if ':' in data:
        course_name, student_name = data.split(' : ')

        if course_name not in database:
            database[course_name] = [student_name]
        else:
            database[course_name].append(student_name)


