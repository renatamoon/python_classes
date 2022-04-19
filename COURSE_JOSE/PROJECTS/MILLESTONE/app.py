"""PROJECT MILESTONE TO CREATE FUNCTIONS"""

# function to add a movie on the database

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

# def adding_movies_to_library():    

#     title = input("Enter the movie TITLE: ").capitalize()
#     director = input("Enter the movie DIRECTOR: ").capitalize()
#     year = input("Enter the movie RELEASE YEAR: ").capitalize()

#     movies_database.append({
#         "title": title,
#         "director": director,
#         "year": year
#     })

# adding_movies_to_library()
print(movies_database)

# create other functions for:
# listening movies
# finding movies

# def find_movies_on_the_database():

title = input("Enter the movie name to find on our database: ").capitalize()

for m in movies_database:
    if movies_database["title"] == title:
        print(m)
    else:
        print("We don't have this movie on our database!")



# def function_selection_on_the_menu():
#     MENU_PROMPT = "Enter 'a' to add a movie, '1' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

# # and another function here for the user menu
#     selection = input(MENU_PROMPT)

#     while selection != 'q':
#         if selection == 'a':
#             pass
#         elif selection == 'l':
#             pass
#         elif selection == 'f':
#             pass
#         else:
#             print("UNKNOWN COMMAND: PLEASE TRY AGAIN!")

#         selection = input(MENU_PROMPT)
