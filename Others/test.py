"""Lambda function
е анонимна функция и по дефиницеия връща резултат, не се иска ретърн
Често се изполват във функцията sorted(), тъй като са удобен начин за задаване на
условие по което да се сортира. Използва се за конкретен случай и после няма да се прилага в кода
"""
# мапа вади секи елемент и прилага лбдата върху всеки от елементите
# трите варианта правят едно и също и са еквивалентни като резултат
my_ints = ["1", "2", "3"]
der_my_list = [int(el) for el in my_ints] # --> list_of_the_day comprehension
list_as_ints = list(map(lambda i: int(i), my_ints)) # --> map в мапа има втора функция (lamda, int..)
der_my_list3 = list(map(int, my_ints))
print(type(my_ints))
print("as ints ->", der_my_list)
print("as ints ->", list_as_ints)
print("as ints ->", der_my_list3)
# разгледам map функцията
res = [i for i in list_as_ints if i % 2 == 0]
res_one = list(filter(lambda num: num % 2 == 0, der_my_list)) # --> както map, така и филтър трябва да са в лист за да върне стойност лист
print(res)
print(res_one)
# map and filter ще се разглеждат в следващото ниво
# имат своето място не са просто алтернатива на лист компрехеншън