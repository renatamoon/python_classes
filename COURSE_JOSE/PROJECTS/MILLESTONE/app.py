MENU_PROMPT = "Enter 'a' to add a movie, '1' to see your movies, 'f' to find a movie by title, or 'q' to quit: "

movies = []

title = input("Enter the movie TITLE: ")
director = input("Enter the movie DIRECTOR: ")
year = input(int("Enter the movie RELEASE YEAR: "))


movies.append({
    "title": title,
    "director": director,
    "year": year
})

# create other functions for:
# listening movies
# finding movies


# and another function here for the user menu
selection = input(MENU_PROMPT)

while selection != 'q':
    if selection == 'a':
        pass
    elif selection == 'l':
        pass
    elif selection == 'f':
        pass
    else:
        print("UNKNOWN COMMAND: PLEASE TRY AGAIN!")

    selection = input(MENU_PROMPT)

    