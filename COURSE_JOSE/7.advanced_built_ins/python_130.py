# MUTABILITY IN PYTHON

"""A mutable data is a data that you can change when you created, an immutable you can't change"""

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}

another_variable = friends_last_seen  # here we're only passing the same dict into a variable

# how do you know it's mutable? - the ID is the id of this variable on the system
print(id(friends_last_seen))  # 140670768395392
print(id(another_variable))  # 140670768395392 - this is the same object as the dictionary friends_last_seen

# but now if we copy the same dictionary and take the id, we'll see that this is not the same:

friends_last_seen = {
    'Rolf': 31,
    'Jen': 1,
    'Anne': 7
}
print(id(friends_last_seen))  # 140670768395456

# things that are immutable = floats, strings and tuples
