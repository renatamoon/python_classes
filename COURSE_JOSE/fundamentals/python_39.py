# COMPREHENSIONS WITH CONDITIONALS

ages = [23, 35, 27, 21, 20]

odds = [age for age in ages if age % 2 == 1]

print("THE ODDS: ", odds) # [23, 35, 27, 21]

# -------------------------------------------

friends = ["Rolf", "Ruth", "Charlie", "Jen"]

guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = [f.lower() for f in friends]

# getting all the friends list in lower cause
print("FRIENDS: ", friends_lower) # ['rolf', 'ruth', 'charlie', 'jen']

guests_lower = [g.lower() for g in guests]
print("GUESTS: ", guests_lower) # ['jose', 'bob', 'rolf', 'charlie', 'michael']

# -------------------------------------------

# if I want to see the intersection persons between the friends and guests, then I put all the data on
# a set and then check which data are in both of the lists

friends_lower_set = set([f.lower() for f in friends])
guests_lower_set = set([g.lower() for g in guests])

print("FRIENDS INTERSECTION: ", friends_lower_set.intersection(guests_lower_set)) # {'rolf', 'charlie'}

# -------------------------------------------

# USING LIST COMPREHENSION

present_list = [
    name.title() 
    for name in guests
    if name.lower() in friends_lower
]
print("PRESENT LIST: ", present_list) # ['Rolf', 'Charlie']
