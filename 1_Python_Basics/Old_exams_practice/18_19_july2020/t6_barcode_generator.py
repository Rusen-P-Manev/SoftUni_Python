first_number = input()
second_number = input()

for num_one in range(int(first_number[0]), int(second_number[0]) + 1):
    for num_two in range(int(first_number[1]), int(second_number[1]) + 1):
        for num_tree in range(int(first_number[2]), int(second_number[2]) + 1):
            for num_four in range(int(first_number[3]), int(second_number[3]) + 1):
                if num_one % 2 != 0 and num_two % 2 != 0 and num_tree % 2 != 0 and num_four % 2 != 0:
                    print(f"{num_one}{num_two}{num_tree}{num_four}", end = " ")
