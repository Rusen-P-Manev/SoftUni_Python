days_of_plunder = int(input())
daly_plunder = int(input())
expected_plunder = float(input())

total_plunder = 0

for day in range(1, days_of_plunder +1):
    total_plunder += daly_plunder
# свата ифа са мужни защото денят може както да се дели на три така и на 5...
    if day % 3 == 0:
        total_plunder += daly_plunder * 0.5
    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected_plunder:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
elif total_plunder < expected_plunder:
    percentige_colledted = (total_plunder / expected_plunder) * 100
    print(f'Collected only {percentige_colledted:.2f}% of the plunder.')
