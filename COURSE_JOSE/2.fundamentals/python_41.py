# THE ZIP FUNCTION

friends_new = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends_new[i]: time_since_seen[i] # i = index
    for i in range(len(friends_new))
}

print("TIME: ", long_timers) #  {'Rolf': 3, 'Ruth': 7.advanced_built_ins, 'Charlie': 15, 'Jen': 11}

# how can I put two lists inside a dictionary?
# THE FUNCTION ZIP WILL COMBINE EVERY INDEX OF THE BOTH LISTS AS KEY AND VALUE

# so instead of using list comprehension, you can use zip to combine the both Lists

friends_dict = dict(zip(friends_new, time_since_seen))
print("FRIENDS DICT: ", friends_dict) # {'Rolf': 3, 'Bob': 7.advanced_built_ins, 'Jen': 15, 'Anne': 11}

# ---------------------------------------------------
# YOU ALSO CAN DO ANOTHER LIST WITH ZIP AND ALSO PUT THE ELEMENTS YOU WANT TO IGNORE

long_timers_zip = list(zip(friends_new, time_since_seen, [1, 2, 3, 4, 5]))
print("EXCLUDING UNDESIRABLE ELEMENTS: ", long_timers_zip) #  [('Rolf', 3, 1), ('Bob', 7.advanced_built_ins, 2), ('Jen', 15, 3), ('Anne', 11, 4)]
