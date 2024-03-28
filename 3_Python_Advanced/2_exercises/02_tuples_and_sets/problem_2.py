# n, m = [int(x) for x in input().split()]  # "4 3" -> ["4", "3"] -> [4, 3]
#
# first_set = {input() for _ in range(n)}   # 1, 3, 5, 7
# second_set = {input() for _ in range(m)}  # 3, 4, 5
#
# print(*first_set.intersection(second_set), sep="\n")  # 3, 5


n_rep, m_rep = [int(n) for n in input().split()]

nst = set()
mst = set()

for _ in range(n_rep):
    nst.add(input())

for _ in range(m_rep):
    mst.add(input())

for ele in nst.intersection(mst):
    print(ele)


# print(first_set & second_set)  # and, intersection
# print(first_set | second_set)  # or, union
# print(first_set - second_set)  # subtract, difference
# print(first_set ^ second_set)  # symmetric difference