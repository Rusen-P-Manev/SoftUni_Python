# resources = {}
# while True:
#     current_resources = input()
#     if current_resources == "stop":
#         break
#     current_quantity = int(input())
#     if current_resources not in resources.keys(): #if current_resources not in resources
#         resources[current_resources] = 0
#     resources[current_resources] += current_quantity
# for resource, quantity in resources.items():
#     print(f"{resource} -> {quantity}")



all_collected = []
resources_container = {}

while True:
    given_item = input()

    if given_item == "stop":
        break

    all_collected.append(given_item)

for item in range(0, len(all_collected), 2):
    if all_collected[item] not in resources_container:
        resources_container[all_collected[item]] = int(all_collected[item + 1])
    else:
        resources_container[all_collected[item]] += int(all_collected[item + 1])

for key, val in resources_container.items():
    print(f'{key} -> {val}')