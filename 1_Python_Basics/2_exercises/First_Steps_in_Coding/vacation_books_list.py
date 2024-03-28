from math import floor

number_of_pages = int(input())
pages_per_hour = int(input())
days_to_finisj = int(input())
# Да се отпечата на конзолата броят часове, които Жоро трябва да отделя за четене всеки ден.
time_to_finish_the_book = number_of_pages / pages_per_hour
houers_per_day = time_to_finish_the_book / days_to_finisj

print(int(houers_per_day))
print(floor(houers_per_day))
# Може и по двата начина да закръглим до петица