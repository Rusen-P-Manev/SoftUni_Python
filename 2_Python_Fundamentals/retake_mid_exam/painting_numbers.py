number_of_painting = [int(num) for num in input().split(' ')]

while True:
    procese_data = input()
    if procese_data == 'END':
        break

    current_data = procese_data.split(' ')
    command = current_data[0]

    if command == 'Change':
        painting_number = int(current_data[1])
        new_number = int(current_data[2])
        if painting_number in number_of_painting:
            index = number_of_painting.index(painting_number)
            number_of_painting[index] = new_number

    if command == 'Hide':
        painting_number = int(current_data[1])
        if painting_number in number_of_painting:
            number_of_painting.remove(painting_number)

    if command == 'Switch':
        number_one = int(current_data[1])
        number_two = int(current_data[2])
        if (number_one in number_of_painting) and (number_two in number_of_painting):
            number_one_index = number_of_painting.index(number_one)
            number_two_index = number_of_painting.index(number_two)
            number_of_painting[number_one_index], number_of_painting[number_two_index]= number_of_painting[number_two_index], number_of_painting[number_one_index]

    if command == 'Insert':
        index = int(current_data[1]) + 1
        number = int(current_data[2])
        if index in range(len(number_of_painting)):
            number_of_painting.insert(index, number)

    if command == 'Reverse':
        number_of_painting.reverse()

for element in number_of_painting:
    print(str(element), end=(' '))
