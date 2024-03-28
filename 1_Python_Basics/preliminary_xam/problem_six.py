number = int(input())
counter = 0
exit_condition = False
for a in range(1,10):
    for b in range(9,a,-1):
        for c in range(10):
            for d in range(9,c,-1):
                if (a + b + c + d) == (a * b * c * d) and number % 10 == 5:
                    counter += 1
                    print(f"{a}{b}{c}{d}")
                    exit_condition = True
                    break
                elif (a * b * c * d) // (a + b + c + d) == 3 and number % 3 == 0:
                    counter += 1
                    print(f"{d}{c}{b}{a}")
                    exit_condition = True
                    break
            if exit_condition:
                break
        if exit_condition:
            break
    if exit_condition:
        break
if counter == 0:
    print(f"Nothing found")




