gives_string = input()
n_times = int(input())

repeat_str = lambda a, b: a * b

result = repeat_str(gives_string, n_times)
print(result)
