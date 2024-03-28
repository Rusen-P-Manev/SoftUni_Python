# table = set()
#
# for _ in range(int(input())):
#     for el in input().split():  # input().split() -> ["Ce", "O", "H"]
#         table.add(el)
#
# print(*table, sep="\n")
#
#
# # print(*{el for _ in range(int(input())) for el in input().split()}, sep="\n")
# # not a good idea

repetition = int(input())
container = set()

for _ in range(repetition):
    data = input().split()
    for ele in data:
        container.add(ele)

print(*container, sep='\n')
