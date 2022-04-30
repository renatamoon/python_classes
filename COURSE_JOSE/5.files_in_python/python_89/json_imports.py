import json

file = open('friends_json.txt', 'r')

file_contents = json.load(file)

file.close

print(file_contents['friends'][0]) # {'name': 'Renata', 'degree': 'Applied Computing'}

cars = [
    {'make': 'Ford', 'model': 'Fiesta'},
    {'make': 'VW', 'model': 'Meriva'}
]

file = open('cars_json.txt', 'w')
json.dump(cars, file)
file.close()


my_json_string = '[{"name": "Alfa Romeo", "released": 1950}]'
incorrect_car = json.loads(my_json_string)
print(incorrect_car[0]['name'])


# ------------- exercicio

json_list = []      # store the converted json data for each line
csv_file = open('csv_file.txt', 'r')
 
for line in csv_file.readlines():
    club, city, country = line.strip().split(',')   # first get rid of the \n and then split with ','
    data = {
        'club': club,
        'city': city,
        'country': country
    }
    json_list.append(data)
 
csv_file.close()
 
json_file = open('json_file.txt', 'w')
json.dump(json_list, json_file)     # write json data to a file
json_file.close()