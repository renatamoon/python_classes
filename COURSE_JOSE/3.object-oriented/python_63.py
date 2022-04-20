# PARAMETER NAMING

class Movie:
    def __init__(self, title: str, year: int, director: str) -> dict:
        self.title = title # properties of self. That's why title is created inside of self. That can be accessed by the . (dot)
        self.year = year
        self.director = director

print(Movie('The Matrix', 1999, "Brothers Washowsky").title)

print("-="*20)

movie_1 = Movie('Bewitched', 2004, "Miller Grant").title
print(movie_1)