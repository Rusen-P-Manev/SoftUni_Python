# items = {'shards' : 0, 'fragments' : 0, 'motes' : 0}
#
# obtained = False
#
# while not obtained:
#     collected_items = input().split()
#     for index in range(0, len(collected_items), 2):
#
#         material_val = int(collected_items[index])
#         material_type = collected_items[index + 1].lower()
#
#         if material_type not in items:
#             items[material_type] = 0
#         items[material_type] += material_val
#
#         if items['shards'] >= 250:
#             print(f'Shadowmourne obtained!')
#             items['shards'] -= 250
#             obtained = True
#         elif items['fragments'] >= 250:
#             print(f'Valanyr obtained!')
#             items['fragments'] -= 250
#             obtained = True
#         elif items['motes'] >= 250:
#             print(f'Dragonwrath obtained!')
#             items['motes'] -= 250
#             obtained = True
#
#         if obtained:
#             break
#
# for key, val in items.items():
#     print(f'{key}: {val}')




items = {'shards' : 0, 'fragments' : 0, 'motes' : 0}

obtained = False

while not obtained:
    collected_items = input().split()
    for index in range(0, len(collected_items), 2):

        material_val = int(collected_items[index])
        material_type = collected_items[index + 1].lower()

        if material_type not in items:
            items[material_type] = material_val
        else:
            items[material_type] += material_val

        if items['shards'] >= 250:
            print(f'Shadowmourne obtained!')
            items['shards'] -= 250
            obtained = True
        elif items['fragments'] >= 250:
            print(f'Valanyr obtained!')
            items['fragments'] -= 250
            obtained = True
        elif items['motes'] >= 250:
            print(f'Dragonwrath obtained!')
            items['motes'] -= 250
            obtained = True

        if obtained:
            break

for key, val in items.items():
    print(f'{key}: {val}')

