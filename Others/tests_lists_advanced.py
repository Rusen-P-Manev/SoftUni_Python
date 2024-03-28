
# standard way to do this
list_of_the_day = []


for num in range(1, 11):
    list_of_the_day.append(num)

print(list_of_the_day)

# list_of_the_day comperhantion variant
nums_comp = [num for num in range(1, 11)]
print(nums_comp)

# only evens
nums_comp = [num for num in range(1, 11) if num % 2 == 0]
print(nums_comp)

# only evens
nums_comp = [num for num in range(1, 11) if num % 2 != 0]
print(nums_comp)

# squares
list_of_the_day = [1, 2, 3, 4, 5]
squares = [x ** 2 for x in list_of_the_day]
print(squares)


# list_of_the_day methods
# append - добавя елемент късм списъка
list_of_the_day = [1, 2, 3, 4, 5]
squares = []
for i in list_of_the_day:
    sq = i ** 2
    squares.append(sq)
print(squares)
# extend - съединява два списъка, удължава
nims_1 = [1, 2, 3]
nims_2 = [4, 5, 6]
nims_1.extend(nims_2)
print(nims_1)
nims_2.extend(nims_1)
print(nims_2)
nims_2.extend(nims_2)
print(nims_2)

# insert вмъкване на елемент на конкретен индекс
nums_1 = [1, 2, 3]
nums_2 = [4, 5, 6]
nums_1.insert(1,55)
nums_2.insert(0, 88)
print(nums_1, nums_2)
nums_2.clear() # clear - трие всичко от листа
print(nums_1, nums_2)

# pop - изтрива последния елемент от листа ско в скобите остане празно
# pop връша стойност, това е стойността, която е премахната
# ако в скобите е посочен индекс ще махне елемента на конкретен индекс

# remove - премахва елемент, но не по индекс, а по елемент, за разлика от поп
# не връща елемента, който се премахва...

a = input()
if a.isdigit():
    as_int = int(a)
    print(f"is num --> {as_int}")
else:
    print("is not num")
#
# list_words = ["banana", "apple", "rose", "strawberry"]
# # list_rev = list_words[::-1]
# print(list_words[::-1])







