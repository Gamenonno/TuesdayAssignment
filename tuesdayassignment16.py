class Series:
    def __init__(self, title: str, seasons: int, genres: list):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.ratings = []

    def __str__(self):
        genre_string = ", ".join(self.genres)
        if self.ratings:
            average_rating = sum(self.ratings) / len(self.ratings)
            return (f"{self.title} ({self.seasons} seasons)\n"
                    f"genres: {genre_string}\n"
                    f"{len(self.ratings)} ratings, average {average_rating:.1f} points")
        else:
            return (f"{self.title} ({self.seasons} seasons)\n"
                    f"genres: {genre_string}\n"
                    "no ratings")

    def rate(self, rating: int):
        if 0 <= rating <= 5:
            self.ratings.append(rating)

# Searching for series functions
def minimum_grade(rating: float, series_list: list) -> list:
    return [series for series in series_list if series.ratings and sum(series.ratings) / len(series.ratings) >= rating]

def includes_genre(genre: str, series_list: list) -> list:
    return [series for series in series_list if genre in series.genres]

# Example of usage
dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
dexter.rate(4)
dexter.rate(5)
dexter.rate(5)
dexter.rate(3)
dexter.rate(0)
print(dexter)

s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
s1.rate(5)

s2 = Series("South Park", 24, ["Animation", "Comedy"])
s2.rate(3)

s3 = Series("Friends", 10, ["Romance", "Comedy"])
s3.rate(2)

series_list = [s1, s2, s3]

print("\na minimum grade of 4.5:")
for series in minimum_grade(4.5, series_list):
    print(series.title)

print("\ngenre Comedy:")
for series in includes_genre("Comedy", series_list):
    print(series.title)
