# DICTIONARIES - allows you to store keys and values

friends_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print("OUTPUT", friends_ages["Rolf"])

friends_ages["Bob"] = 20 # adding an element to the dictionary
friends_ages["Rolf"] = 25 # changing the value of the key Rolf

print("OUTPUT: ", friends_ages) # {'Rolf': 25, 'Adam': 30, 'Anne': 27, 'Bob': 20}

print("=-"*20)

"""DOING A TUPLE OF DICTIONARIES"""

friends = (
    {"name": "Rolf Smith", "age": 24},
    {"name": "Renata Monteiro", "age": 27},
    {"name": "Renato Romeo", "age": 26},
)

print("THE NAME IS: ", friends[0]["name"])
print("THE NAME IS: ", friends[1]["name"])
print("THE NAME IS: ", friends[2]["name"])

print("THE AGE IS: ", friends[2]["age"])

print("=-"*20)

friends_dict = [("Rolf", 24), ("Adam", 30), ("Anne", 27)]