number_of_computer_models = int(input())
avarage_rating = 0
sales_made = 0
total_sales_made = 0
for _ in range(number_of_computer_models):
    computer_model = int(input())
    rating = computer_model % 10
    possible_sales = computer_model // 10
    if rating == 2:
       sales_made = possible_sales * 0
    elif rating ==3:
        sales_made = possible_sales * 0.5
    elif rating ==4:
        sales_made = possible_sales * 0.7
    elif rating ==5:
        sales_made = possible_sales * 0.85
    elif rating ==6:
        sales_made = possible_sales
    avarage_rating = (avarage_rating + rating)
    total_sales_made = total_sales_made + sales_made
final_avarage_rating = avarage_rating / number_of_computer_models
print(f"{total_sales_made:.2f}\n{final_avarage_rating:.2f}")

