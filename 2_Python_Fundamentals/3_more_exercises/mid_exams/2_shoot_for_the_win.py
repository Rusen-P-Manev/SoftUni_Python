targets = list(map(int, input().split()))
shot_targets = 0

while True:
    command = input()
    if command == 'End':
        print(f"Shot targets: {shot_targets} -> {' '.join(map(str, targets))}")
        break

    index = int(command)
    if index in range(len(targets)):
        current_number = targets[index]
        for i in range(len(targets)):
            if targets[i] != -1:
                if targets[i] > current_number:
                    targets[i] -= current_number
                else:
                    targets[i] += current_number
        targets[index] = -1
        shot_targets += 1

# targets = [int(num) for num in input().split(' ')]
# passed_targets = []
# shots_counter = 0
#
# while True:
#     shoot_index = input()
#     if shoot_index == 'End':
#         print(f"Shot targets:")
#         break
#
#     if shoot_index in passed_targets:
#         continue
#     if shoot_index not in len(targets):
#         continue
#
#     passed_targets.append(shoot_index)
#     shots_counter += 1
#     current_target_vlaue = targets[shoot_index]
#
#     for current_target in len(targets):
#         if current_target != -1 and current_target > current_target_vlaue:
