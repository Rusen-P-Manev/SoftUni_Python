words_collection = input().split(' ')
trasformed_elements = {}

for element in words_collection:
    new_element = element.lower()
    if new_element not in trasformed_elements:
        trasformed_elements[new_element] = 0
    trasformed_elements[new_element] += 1

for key, val in trasformed_elements.items():
    if val % 2 != 0:
        print(key, end = ' ')
