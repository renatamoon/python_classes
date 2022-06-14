# ADVANCED BUILT-IN FUNCTIONS
# any() and all()

# any() is an iterable that returns true if any of its elements evaluate True
# all() return True if all the elements evaluates True

friends = [
    {'name': 'Rafael',
     'location': 'São Paulo'},
    {'name': 'Shira',
     'location': 'Tel Aviv'},
    {'name': 'Camila',
     'location': 'New York'},
    {'name': 'Victoria',
     'location': 'Rio de Janeiro'},
]

your_location = input("Where are you right now? ")

# list comprehension
friends_nearby = [friend for friend in friends if friend['location'] == your_location]

if any(friends_nearby):
    print("YOU'RE NOT ALONE! There's a friend nearby")

# Exercises
my_list = []
bool(my_list)  # False

another_list = [None]
bool(another_list)  # True
