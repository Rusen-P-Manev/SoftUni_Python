def calculations(a, b, operator):
    if operator == 'multiply':
        return a * b
    elif operator == 'divide':
        if b != 0:
            return int(a / b)
    elif operator == 'add':
        return a + b
    elif operator == 'subtract':
        return a - b


operator = input()
num_one = int(input())
num_two = int(input())

print(calculations(num_one, num_two, operator))
