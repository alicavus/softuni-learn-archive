def movie_organizer(*args):
    movies = {}
    for movie_data in args:
        movie_name, movie_genre = movie_data
        if movie_genre not in movies:
            movies[movie_genre] = []
        movies[movie_genre].append(movie_name)
    result = []

    for movie_data in sorted(movies.items(), key=lambda item: (-len(item[1]), item[0])):
        result += [f"{movie_data[0]} - {len(movie_data[1])}"]
        for movie_name in sorted(movie_data[1], key=lambda item: item):
            result += [f"* {movie_name}"]

    return "\n".join(result)

print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
