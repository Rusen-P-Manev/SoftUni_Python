hall_rent = int(input())

statuettes = hall_rent * 0.70
kettering = statuettes * 0.85
sounding = kettering * 0.50

total_costs = hall_rent + statuettes\
              + kettering + sounding

print(f"{total_costs:.2f}")
