'''
Ask the user to input a list of movies with ratings like [("Titanic", 8), ("Inception", 9), ...]. Compute
the average rating, find the highest-rated movie, and list all movies with rating above the
average.
'''

a = input("Enter the movies: ").strip()
a = a.split(",")
new_list = []
for item in a:
    if "-" in item:
        new_list.append(item)

a = new_list

final_list = []
for item in a:
    parts = item.split("-")     
    final_list.append(tuple(parts))  
a = final_list


def average(movies):
    ratings = 0
    length = len(movies)
    if(length < 1):
        return 0
    for name, rating in movies:
        ratings += float(rating)
    return ratings/len(movies)

def highest_rated(movies):
    if not movies:
        return ''
    highest = movies[0]
    for title, rating in movies:
        if float(highest[1]) < float(rating):
            highest = (title, float(rating))
    return highest[0]

def avg_movies(movies, avg):
    higher = []
    lower = []
    for title, rating in movies:
        rating = float(rating)
        if rating > avg:
            # higher.append((title, rating))
            higher.append(title)
        if rating < avg:
            # lower.append((title, rating))
            lower.append(title)
    return (higher, lower)

avg = average(a)
highest = highest_rated(a)
higher, lower = avg_movies(a, avg)

print(f"Average: {avg}")
print(f"Highest Rated Movie: {highest}")
print(f"Higher than Average : {higher}")
print(f"Lower than Average : {lower}")