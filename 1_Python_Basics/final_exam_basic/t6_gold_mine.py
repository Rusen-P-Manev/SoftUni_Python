number_of_locations = int(input())
for _ in range(number_of_locations):
    expected_average_yield_daily = float(input())
    digging_days = int(input())
    avarage_gold_dayly = 0
    total_gold_all_days = 0

    for _ in range(digging_days):
        collected_gold_daily = float(input())
        total_gold_all_days += collected_gold_daily

    avarage_gold_dayly = total_gold_all_days / digging_days
    difference = abs(expected_average_yield_daily - avarage_gold_dayly)

    if avarage_gold_dayly >= expected_average_yield_daily:
        print(f"Good job! Average gold per day: {avarage_gold_dayly:.2f}.")
    elif avarage_gold_dayly < expected_average_yield_daily:
        print(f"You need {difference:.2f} gold.")
