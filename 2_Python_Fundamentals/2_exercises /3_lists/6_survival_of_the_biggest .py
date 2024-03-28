my_list = input().split(" ")
numbers_to_remove = int(input())
my_list_int = []

for element in my_list:
    as_integer = int(element)
    my_list_int.append(as_integer)
for _ in range(numbers_to_remove):
    my_list_int.remove(min(my_list_int))

print(", ".join(str(x) for x in my_list_int))
""" from Mario
nums = input().split(" ")
count = int(input())
copy_nums = list_of_the_day(map(int, nums))

for _ in range(count):
    current_min_element = min(copy_nums)
    nums.remove(current_min_element)
    copy_nums.remove(current_min_element)
print(nums)
"""
"""
Някои интересни записи, на колеги, които да обърна внимание:

№1
a = input()
number = int(input())
ll = [int(i) for i in a.split(' ')]

for _ in range(number):
    x = min(ll)
    ll.remove(x)

result = ', '.join(map(str, ll))
print(result)
------
№2
numbers_str = input().split()
numbers = []

for num in numbers_str:
    numbers.append(int(num))

remover = int(input())

for _ in range(remover):
    numbers.remove(min(numbers))

print(*numbers, sep=", ")
--------
№3
numbers = list_of_the_day(map(int, input().split()))
remover = [numbers.remove(min(numbers)) for _ in range(int(input()))]
--------
№4
numbers_str = input().split()

numbers = []

for num in numbers_str:
    numbers.append(int(num))

remover = int(input())

for _ in range(remover):
    numbers.remove(min(numbers))

print(numbers)
"""