from collections import deque

total_amount_of_food = int(input())
hungry_people = deque(int(ele) for ele in input().split())

print(max(hungry_people))

for portion in hungry_people.copy():
    if total_amount_of_food >= portion:
        hungry_people.popleft()
        total_amount_of_food -= portion
    else:
        print(f'Orders left:', *hungry_people)
        break
else:
    print('Orders complete')


# solution 2
#
# while orders:
#     order = orders.popleft()
#
#     if food >= order:
#         food -= order
#     else:
#         print(f"Orders left:", order, *orders)  # " ".join([str(x) for x in orders])
#         break
# else:
#     print("Orders complete")