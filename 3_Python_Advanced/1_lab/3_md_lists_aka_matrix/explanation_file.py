print('*** example 1 ***')
rows = 3
columns = 3
matrix = []

for row in range(rows):  # броят на вложените списъци
    matrix.append([])
    for col in range(columns):  # боят на елементите от вложеният списък
        matrix[row].append(0)

for ele in matrix:
    print(ele)
print(matrix)


print('*** example 2 ***')
matrix_two = [[0] * columns for _ in range(rows)]  # същото като горното, но с комперхеншън
matrix_comp = [[0 for j in range(columns)]for i in range(rows)]
print(matrix)
print(matrix_comp)

print('*** example 3 ***')
matrix_three = []
for i in range(rows):
    sub_list = []
    for j in range(columns):
        sub_list.append(0)
    matrix_three.append(sub_list)

print(matrix_three)

print('*** example 4 ***')

matrix_four = []
for row in range(3):
    sub_list = []
    for column in range(1, 4):
        sub_list.append(column)
    matrix_four.append(sub_list)
print(matrix_four)

matrix_four2 = []
for row in range(3):
    matrix_four2.append([])
    for column in range(1, 4):
        matrix_four2[row].append(column)
print(matrix_four2)

matrix_comp2 = [[j for j in range(1, 4)] for i in range(3)]
print(matrix_comp2)

print('*** example 5 ***')
matrix = [[1, 2, 3], [4, 5, 6]]
flattened = [num for sublist in matrix for num in sublist]
print(flattened)

flatten = []
for row in matrix:
    for element in row:
        flatten.append(element)
print(flatten)

print('*** example 6 ***')
matrix_t = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row_index in range(len(matrix_t)):
    for col_index in range(len(matrix_t[row_index])):
        print(matrix_t[row_index][col_index], end=" ")
    print()







