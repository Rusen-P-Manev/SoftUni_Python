movie_name = input()
total_tickets_sold = 0
student_tickts_counter = 0
standard_tickts_counter = 0
kids_tickts_counter = 0
break_condition = False

while movie_name != "Finish":
    seats = int(input())
    current_tickets_sold = 0
    while seats > current_tickets_sold:
        ticket_type = input()
        if ticket_type == "student":
            student_tickts_counter += 1
        elif ticket_type == "standard":
            standard_tickts_counter += 1
        elif ticket_type == "kid":
            kids_tickts_counter += 1
        elif ticket_type == "End":
            break
        current_tickets_sold += 1
        total_tickets_sold += 1

    percentage_hall_occupied = (current_tickets_sold / seats) * 100
    print(f"{movie_name} - {percentage_hall_occupied:.2f}% full.")

    movie_name = input()

student_tickts_sold = (student_tickts_counter / total_tickets_sold) * 100
standard_tickts_sold = (standard_tickts_counter / total_tickets_sold) * 100
kids_tickts_sold = (kids_tickts_counter / total_tickets_sold) * 100
print(f"Total tickets: {total_tickets_sold}")
print(f"{student_tickts_sold:.2f}% student tickets.")
print(f"{standard_tickts_sold:.2f}% standard tickets.")
print(f"{kids_tickts_sold:.2f}% kids tickets.")