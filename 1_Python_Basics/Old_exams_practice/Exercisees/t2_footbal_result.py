scores_from_firs_match = input()
scores_from_second_match = input()
scores_from_third_match = input()

home_goals1, away_goals1 = scores_from_firs_match[0], scores_from_firs_match[2]
home_goals2, away_goals2 = scores_from_second_match[0], scores_from_second_match[2]
home_goals3, away_goals3 = scores_from_third_match[0], scores_from_third_match[2]

wins = int(home_goals1 > away_goals1)\
       + int(home_goals2 > away_goals2)\
       + int(home_goals3 > away_goals3)

losses = int(home_goals1 < away_goals1)\
       + int(home_goals2 < away_goals2)\
       + int(home_goals3 < away_goals3)

draws = int(home_goals1 = away_goals1)\
       + int(home_goals2 = away_goals2)\
       + int(home_goals3 = away_goals3)

print(fTeam won 1 games.)
print(lost 1 games).
print(Drawn games: 1)
#  да оправя изхода и да
#  разгледа решението, тъй като е интересно