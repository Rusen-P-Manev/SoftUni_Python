number_of_movies = int(input())

highest_rating = 0
highest_rating_movie = ""
lowest_rating = 10
lowest_rating_movie = ""
sum_ratings = 0

for _ in range(number_of_movies):
    name_of_the_movie = input()
    current_rating = float(input())
    sum_ratings += current_rating

    if current_rating > highest_rating:
        highest_rating = current_rating
        highest_rating_movie = name_of_the_movie

    if current_rating < lowest_rating:
        lowest_rating = current_rating
        lowest_rating_movie = name_of_the_movie

avarage_rating = sum_ratings / number_of_movies

print(f"{highest_rating_movie} is with highest rating: {highest_rating:.1f}\n\
{lowest_rating_movie} is with lowest rating: {lowest_rating:.1f}\n\
Average rating: {avarage_rating:.1f}")