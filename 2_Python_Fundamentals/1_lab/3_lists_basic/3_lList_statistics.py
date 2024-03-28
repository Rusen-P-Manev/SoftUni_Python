"""
elements_count = int(input())

positive_numbers_list = []
negative_numbers_list = []
count_positives = 0
sum_of_negatives = 0

for n in range(elements_count):
    element = int(input())
    if element >= 0:
        positive_numbers_list.append(element)
        count_positives += 1
    else:
        negative_numbers_list.append(element)
        sum_of_negatives += element
print(positive_numbers_list)
print(negative_numbers_list)
print(f"Count of positives: {count_positives}")
print(f"Sum of negatives: {sum_of_negatives}")
"""
elements_count = int(input())

positive_numbers_list = []
negative_numbers_list = []

for n in range(elements_count):
    element = int(input())
    if element >= 0:
        positive_numbers_list.append(element)
    else:
        negative_numbers_list.append(element)

print(positive_numbers_list)
print(negative_numbers_list)
print(f"Count of positives: {len(positive_numbers_list)}")
print(f"Sum of negatives: {sum(negative_numbers_list)}")
