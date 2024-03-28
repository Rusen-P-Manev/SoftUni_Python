from math import ceil # ceil закръгля до най-близкото цяло число нагоре

name_of_tv_series = str(input())
episode_duration = int(input())
break_duration = int(input())
lunch_duration = break_duration / 8
relaxation_duration = break_duration / 4
time_left = break_duration \
            - lunch_duration \
            - relaxation_duration
difference = abs(time_left - episode_duration)
difference = ceil(difference)
if time_left >= episode_duration:
    print(f"You have enough time to watch {name_of_tv_series} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_tv_series}, you need {difference} more minutes.")