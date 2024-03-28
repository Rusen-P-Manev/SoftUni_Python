# words = input().split(", ")
#
# sorted_names = sorted(names, key=len, reverse=True)
#
# print(sorted_names)

def sort_names():
    names_list = [name for name in input()].splir()", "
    return sorted(names_list, key=lambda  x: (-len(x), x))

print(sort_names())