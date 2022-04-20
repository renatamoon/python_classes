"""PROJECT MILESTONE TO CREATE FUNCTIONS"""

# dict with all the movies. Also can get more items
movies_database = [
    {
        "title": "James Bond",
        "director": "Sam Mendes",
        "year": 2021
    },
    {
        "title": "The Lord Of The Rings",
        "director": "Peter Jackson",
        "year": 2001
    },
    {
        "title": "The Devil Wears Prada",
        "director": "William Lane",
        "year": 2006
    }
]

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
    title = input("Enter the movie name to find on our database: ").capitalize()

    for movie in movies_database:
        if title == movie["title"]:
            print("-="*20)
            print("THE MOVIE YOU'RE LOOKING FOR IS:", movie)
        else:
            message = {"error": "This movie does not exist on our database"}
            return message


# function to list all movies on the database
def list_all_movies_on_the_database():
    for movies in movies_database:
        print("-="*20)
        return movies


# function to select on the menu prompt and return the expected
def function_selection_on_the_menu():
    print("-="*20)
    MENU_PROMPT = "Enter 'a' to add a movie, '1' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

    selection = input(MENU_PROMPT).lower()

    print("-="*20)

    while selection != 'q':
        if selection == 'a':
            add_movie_on_database()
        elif selection == 'l':
            list_all_movies_on_the_database()
        elif selection == 'f':
            find_a_movie_on_the_database
        else:
            print("UNKNOWN COMMAND: PLEASE TRY AGAIN!")


if __name__ == "__main__":
    function_selection_on_the_menu()
