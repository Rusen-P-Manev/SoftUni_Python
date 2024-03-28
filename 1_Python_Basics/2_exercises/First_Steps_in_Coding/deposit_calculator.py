amount_deposited = float(input())
period = int(input())
annual_interest_rate = float(input())
the_accrued_interest = amount_deposited * (annual_interest_rate / 100)
divident_per_month = the_accrued_interest / 12
total = amount_deposited + (period * divident_per_month)
print(total)
