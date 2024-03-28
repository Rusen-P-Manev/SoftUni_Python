rows, columns = [int(x) for x in input().split(', ')]

matrix = []

for row in range(rows):
    data = input().split(', ')
    raw_data = [int(x) for x in data]
    matrix.append(raw_data)

final_sum = sum([sum(x) for x in matrix])

print(final_sum)
print(matrix)

# rows, columns = [int(x) for x in input().split(', ')]
#
# total_sum = 0
# matrix = []
#
# for row in range(rows):
#     row_data = [int(x) for x in input().split(', ')]
#     total_sum += sum(row_data)  # избягва се един фор цикъл от моето решение -> оптимизация
#     matrix.append(row_data)
#
# print(total_sum)
# print(matrix)

