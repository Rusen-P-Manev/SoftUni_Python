aviocompany_name = input()
number_adults_tickets = int(input())
number_chaild_tickets = int(input())
adults_price = float(input())
service_fee = float(input())

chaild_ticket_price = adults_price * 0.30
adult_price_inc_service_fee = adults_price + service_fee
child_price_inc_service_fee = chaild_ticket_price + service_fee

total_incom = (number_adults_tickets * adult_price_inc_service_fee)\
              + (number_chaild_tickets * child_price_inc_service_fee)
profit = total_incom * 0.20
print(f"The profit of your agency from {aviocompany_name} tickets is {profit:.2f} lv.")

