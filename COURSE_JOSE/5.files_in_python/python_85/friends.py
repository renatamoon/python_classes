# ask the user for a list of 3 friends
# for each friend, we'll tell the user whether they are nearby
# for each nearby friend, we'll save their name to 'nearby_friends.txt'

# hint: readlines()

friends = input('Enter 3 names of your friends, separated by comas (no spaces, please)').split(',')

people = open('people.txt', 'r') # mode of reading the file
people_nearby = [line.strip() for line in people.readlines()]

people.close()

friends_set = set(friends)
people_nearby_set = set(people_nearby)

friends_nearby = friends_set.intersection(people_nearby_set)

nearby_friends_file = open('nearby_friends.txt', 'w')

for friend in people_nearby_set:
    print(f'{friend} is nearby! Meet up with me!')
    nearby_friends_file.write(f'{friend}')

nearby_friends_file.close()
