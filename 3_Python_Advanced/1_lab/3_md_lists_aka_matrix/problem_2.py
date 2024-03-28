numbers_of_rows = int(input())
matrix = []

for row in range(numbers_of_rows):
    matrix_data = input().split(', ')
    data = [int(ele) for ele in matrix_data if int(ele) % 2 == 0]
    matrix.append(data)

print(matrix)
