# Фигура - елха
# for i in range(1,20,2):
#     print(('*' * i).center(20))
#
# for leg in range(3):
#     print(('||').center(20))
#
# print(('\====/').center(20))
n = int(input())

for i in range(n):
    print(' ' * (n - (i + 1)), '+' * (2*i+1))
