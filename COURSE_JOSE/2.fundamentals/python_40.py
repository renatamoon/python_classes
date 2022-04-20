# SET AND DICTIONARY COMPREHENSION

friends = ["Rolf", "Ruth", "Charlie", "Jen"]
guests = ["jose", "Bob", "Rolf", "Charlie", "michael"]

friends_lower = {n.lower() for n in friends}
guests_lower = {n.lower() for n in guests}

present_friends = {name.title() for name in friends_lower.intersection(guests_lower)}
print("PRESENT FRIENDS: ", present_friends) # {'Charlie', 'Rolf'}

# OR WE ALSO COULD LIKE THIS - A BETTER CODE:

present_friendss = friends_lower.intersection(guests_lower)
present_friendss = {name.title() for name in present_friends}

print("PRESENT FRIENDS: ", present_friendss) # {'Charlie', 'Rolf'}

# -----------------------------------------

friends_new = ["Rolf", "Bob", "Jen", "Anne"]
time_since_seen = [3, 7, 15, 11]

long_timers = {
    friends_new[i]: time_since_seen[i] # i = index
    for i in range(len(friends_new))
}

print("TIME: ", long_timers) #  {'Rolf': 3, 'Ruth': 7, 'Charlie': 15, 'Jen': 11}

# with conditional included

long_timers_since = {
    friends_new[i]: time_since_seen[i] # i = index
    for i in range(len(friends_new))
    if time_since_seen[i] > 5
}
print("USING CONDITIONAL: ", long_timers_since) # {'Ruth': 7, 'Charlie': 15, 'Jen': 11}
