"""PROJECT MILESTONE TO CREATE FUNCTIONS"""


MENU_PROMPT = "Enter 'a' to add a movie, 'l' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

# dict with all the movies. Also can get more items
movies_database = []


# function to get the details of a movie
def print_movie(movie):
    print("-="*20)
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}")
    print("-="*20)


# function to list all movies on the database
def list_all_movies_on_the_database():
    for movie in movies_database:
        print_movie(movie)


# function to add a movie on the database
def add_movie_on_database():    

    title = input("Enter the movie TITLE: ").capitalize()
    director = input("Enter the movie DIRECTOR: ").capitalize()
    year = input("Enter the movie RELEASE YEAR: ").capitalize()    

    movies_database.append({
        "title": title,
        "director": director,
        "year": year
    })      


# function to find the movies on the database
def find_a_movie_on_the_database():
    title_searched = input("Enter the movie name to find on our database: ").capitalize()

    for movie in movies_database:
        if movie["title"] == title_searched:
            print_movie(movie)
            print("-="*20)
        else:
            message = "This movie does not exist on our database"
            print(message)


# function to select on the menu prompt and return the expected
def menu():
    
    selection = input(MENU_PROMPT).lower()

    print("-="*20)

    while selection != 'q':
        if selection == 'a':
            add_movie_on_database()            
        elif selection == 'l':
            list_all_movies_on_the_database()
        elif selection == 'f':
            find_a_movie_on_the_database()
        else:
            print("UNKNOWN COMMAND: PLEASE TRY AGAIN!")
        
        selection = input(MENU_PROMPT)


if __name__ == "__main__":
    menu()
