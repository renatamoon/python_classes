# SLICE LISTS

friends = ["Rolf", "Charlie", "Anna", "Bob", "Jen"]

# if I want to get the 2 values then I put the index I wanna get
# and the : then the other index

print(friends[2:4]) # ['Anna', 'Bob']
# -----------------------------------

# if want to get the everything except and exact index:
print(friends[1:]) # ['Charlie', 'Anna', 'Bob', 'Jen'] - without Rolf
print(friends[:4]) # ['Rolf', 'Charlie', 'Anna', 'Bob'] - without Bob

# -----------------------------------
# if you want a new list with all the elements you can do:

print(friends[:]) # ['Rolf', 'Charlie', 'Anna', 'Bob', 'Jen']

# -----------------------------------
# you also can use negative numbers

print(friends[-3:]) # ['Anna', 'Bob', 'Jen'] - you will get the 3rd element till the end of the list
print(friends[-3:4]) # ['Anna', 'Bob'] -  getting the 3rd element (from the end of list till the start) and the next one

# -----------------------------------
# from the start of the list till the end

print(friends[:-2]) # ['Rolf', 'Charlie', 'Anna'] - getting all the elements except the last two

print(friends[-3:-1]) # ['Anna', 'Bob'] - getting the third element from the end of the list till the start
# then exclude the last element.