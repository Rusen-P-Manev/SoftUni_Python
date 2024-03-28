matrix_data = input().split(', ')
rows, columns = [int(data) for data in matrix_data]

matrix = []

for _ in range(rows):
    row_data = input().split(' ')
    data = [int(ele) for ele in row_data]
    matrix.append(data)

for col_index in range(columns):
    col_total = 0
    for row_index in range(rows):
        col_total += matrix[row_index][col_index]
    print(col_total)

