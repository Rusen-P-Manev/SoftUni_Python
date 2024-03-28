training_tax = int(input())

basketball_shues = training_tax - (training_tax * 0.4)
basketball_clothes = basketball_shues - (basketball_shues *0.2)
basketball_ball = basketball_clothes / 4
basketball_accessories = basketball_ball / 5

total_expences = training_tax + basketball_shues \
                 + basketball_clothes + basketball_ball \
                 + basketball_accessories
print(total_expences)