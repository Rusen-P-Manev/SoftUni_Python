first_time = int(input())
second_time = int(input())
third_time = int(input())
total_time = first_time + second_time + third_time
minuters = total_time // 60
seconds = total_time % 60
if seconds <= 9:
    print(f"{minuters}:0{seconds}")
else:
    print(f"{minuters}:{seconds}")
# Има и вариант, да се направи и без if. Целият if модул се заменя с:
# print(f"{minutes}:{seconds:02d}") - 02d е вид форматиране. Да си прегледам
# видовете форматиране с fstring. В материалите е решено по различен начин, който
# е повече затормозяващ от към ресурси, заради въвеждането на
# библиотека/и и не е за предпочитане...
# Библиотеките товарят паметта и прцесора.....!