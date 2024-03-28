wins_counter = 0
loses_counter = 0
total_matches_counter = 0
while True:
    name_of_tournament = input()
    if name_of_tournament == "End of tournaments":
        break
    number_of_maches = int(input())
    total_matches_counter += number_of_maches

    for match_number in range(1, number_of_maches + 1):
        team_desi = int(input())
        other_team = int(input())

        if team_desi > other_team:
            difference = team_desi - other_team
            wins_counter += 1
            print(f"Game {match_number} of tournament {name_of_tournament}: win with {difference} points.")

        elif team_desi < other_team:
            difference = abs(team_desi - other_team)
            loses_counter += 1
            print(f"Game {match_number} of tournament {name_of_tournament}: lost with {difference} points.")

win_statistics = (wins_counter / total_matches_counter) * 100
loses_statistics = (loses_counter / total_matches_counter) * 100
print(f"{win_statistics:.2f}% matches win\n{loses_statistics:.2f}% matches lost")


