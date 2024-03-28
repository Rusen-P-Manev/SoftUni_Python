# text = list(input())
#
#
# def some_func(a,b):
#     return None
#
# while text:
#     print(text.pop(), end="")
#
#

# string_data = input()
# final_str =[]
# for ele in reversed(string_data):
#     final_str.append(ele)
#
# print(''.join(final_str))

text = list(input())
stack = []
for i in range(len(text)):
    stack.append(text.pop())
print("".join(stack))
