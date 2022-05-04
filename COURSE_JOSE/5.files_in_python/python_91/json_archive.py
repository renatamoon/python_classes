import json

# ------------- context manager - automatically close the file at the end

with open('friends_json.txt', 'r') as file:
    file_contents = json.load(file) # read files and turn it into a dictionary

print(file_contents['friends'][0])

# ------------ 

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'VW', 'model': 'Meriva'}
]


with open('cars_json.txt', 'w') as file:
    json.dump(cars, file)