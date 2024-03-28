# Тази задача като логика е много интересна да си я прегледам...
from sys import maxsize

n = int(input())

biggest = -maxsize
smallest = maxsize

for i in range(n):
    current_number = int(input())

    if current_number > biggest:
      biggest = current_number

    if current_number < smallest:
      smallest = current_number

print(f"Max number: {biggest}\nMin number: {smallest}")
