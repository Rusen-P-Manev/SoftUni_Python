number_easter_bread = int(input())
number_of_peels_with_eggs = int(input())
kilograms_cookies = int(input())

price_for_easter_bread = number_easter_bread * 3.2
price_for_eggs = number_of_peels_with_eggs * 4.35
price_for_cookies = kilograms_cookies * 5.40
price_for_eggs_paint = number_of_peels_with_eggs * 12 * 0.15

total_cost_price = price_for_easter_bread + price_for_eggs\
                   + price_for_cookies + price_for_eggs_paint

print(f"{total_cost_price:.2f}")
