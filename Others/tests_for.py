for a in range(10):
    print(a, end="")
print( )

for b in range(1, 10):
    print(b, end="")
print()

for c in range(1, 11):
    print(c, end="")
print()

for d in range(20, 0, -1):
    print(d, end="")
print()

for e in range(0, 21, 2):
    print(e, end="")
print()

word = "Hallo"
for i in word:
    print(i, end="")
print()

word = "Hallo"
for i in reversed(word):
    print(i, end="")
print()

word = "Hallo"
for i in range(len(word)):
    print(i, end="")
print()

word = "Hallo"
for i in range(len(word) - 1, -1, -1):
    print(i, end="")
print()

word = "Hallo - world - i - am Rusen"
word_two = word.split("-")
print(word_two)
for ii in word_two:
    print(ii, end="")
print()

number = 11223344  # за числа това не работи по този начин, трябва да се минт през цикъл и да се раздели по индекси
as_string = str(number)  #  и тогава с append да се напълни в списък
number_two = as_string.split(" ")
print(number_two)
for ii in number_two:
    print(ii, end="")
print()