def check_employee_happines():
    happiness_list = list(map(int, input()))
    happiness_factor = int(input())

    improved_happiness = [happiness * happiness_factor for happiness in happiness_list]
    average_happiness = sum(improved_happiness / len(improved_happiness))
    happy_count = sum(happiness >= average_happiness for happiness in improved_happiness)
    total_count = len(improved_happiness)

    message = "happy" if happy_count >= total_count / 2 else "not happy"
    result = f" {happy_count}/{total_count}. Employee are{message}!"

    return result

print(check_employee_happines())
