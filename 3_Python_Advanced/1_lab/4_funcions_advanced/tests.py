# def sum_nums(a, b, *nums):
#     total_sum = a + b
#     for ele in nums:
#         total_sum += ele
#     return total_sum
#
#
# print(sum_nums(2, 4, 5, 55))


# def some_func(**kwargs):
#   for key, value in kwargs.items():
#       print(f'{value}, {key}')
#
#
# some_func(Peter='Hello', Putio='Bye')

# def print_nums(a, b, c):
#     print(a, b, c)
#
#
# nums = [1, 2, 3]
# a, b, c = nums
#
# print_nums(a, b, c)
# print_nums(nums[0], nums[1], nums[2])
# print_nums(*nums)


# def some_func(name, age, town):
#     print(f"{name} is {age} years old from {town}")
#
#
# person = {'age': 20, 'name': "Peter", 'town': 'Plovdiv'}
# some_func(**person)

# listatmi = [3, -4, 1, 0, -54,7]
# print(sorted(listatmi, reverse=True))


# data = {'Peter': 21, 'George': 18, 'John': 45}
# print(sorted(data))
# print(sorted(data.items()))
# print(sorted(data.items(), key=lambda kvp: kvp[0]))  # сортира по ключ  на речника
# print(sorted(data.items(), key=lambda kvp: kvp[1]))  # сортира по стойност на речника
# print(sorted(data.items(), key=lambda kvp: kvp[0], reverse=True))  # сортира по ключ на речника наобратно
# # print(sorted(data.items(), key=lambda kvp: -kvp[0]))  # не работи за стрингове!!!! винаги горния вариант
# print(sorted(data.items(), key=lambda kvp: kvp[1], reverse=True))  # сортира по стйност на речника
# print(sorted(data.items(), key=lambda kvp: -kvp[1]))  # сортира по стойност на речника