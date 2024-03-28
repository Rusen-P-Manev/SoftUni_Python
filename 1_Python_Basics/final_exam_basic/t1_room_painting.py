from math import ceil, floor
number_paint_cans = int(input())
number_wallpapers_rolls = int(input())
price_gloves_per_pair = float(input())
price_per_brush = float(input())

paint_can_price = 21.50
wallpaper_roll_price = 5.20
needed_gloves = ceil(number_wallpapers_rolls * 0.35)
needed_brushes = floor(number_paint_cans * 0.48)

total_price = number_paint_cans * paint_can_price\
              + number_wallpapers_rolls * wallpaper_roll_price\
              + needed_gloves * price_gloves_per_pair\
              + needed_brushes * price_per_brush
delivery = total_price / 15

print(f"This delivery will cost {delivery:.2f} lv.")