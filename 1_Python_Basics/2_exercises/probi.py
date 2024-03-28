destination = input()
budget = 0
savings = 0

while destination != "End":
    budget = float(input())
    if budget > 0:
        while budget > savings:
            money_to_save = float(input())
            if money_to_save > 0:
                savings += money_to_save
                if savings >= budget:
                    print(f"Going to {destination}!")
                    savings = 0
            if savings == 0:
                break
    destination = input()
