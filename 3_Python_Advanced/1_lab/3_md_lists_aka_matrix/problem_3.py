rows_number = int(input())
matrix = []

for row in range(rows_number):
    input_data = input().split(', ')
    data = [int(element) for element in input_data]
    matrix.append(data)

flattened_matrix = []

for row in matrix:
    for element in row:
        flattened_matrix.append(element)

print(flattened_matrix)

# rows = int(input())
# flat_mat = []
# for row in range(rows):
#     raw_data = input().split(', ')
#     data = [int(element) for element in raw_data]
#     flat_mat.extend(data)
# print(flat_mat)

