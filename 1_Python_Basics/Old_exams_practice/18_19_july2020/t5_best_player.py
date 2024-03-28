best_player_name = ""
best_result = - 100000
current_player_name = ""
while True:
    current_player_name = input()
    if current_player_name == "END":
        break
    current_goals = int(input())

    if current_goals > best_result:
        best_result = current_goals
        best_player_name = current_player_name
    if current_goals >= 10:
        break

if best_result >= 3:
    print(f"{best_player_name} is the best player!")
    print(f"He has scored {best_result} goals and made a hat-trick !!!")
else:
    print(f"{best_player_name} is the best player!")
    print(f"He has scored {best_result} goals.")
