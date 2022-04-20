# ITERATING OVER DICTIONARIES

# dicts has keys and values
friends = {
        "Rolf": 25, 
        "Anne": 37,
        "Charlie": 31,
        "Bob": 22
}

# if you want to take all the keys and values
# to be printed out: 
for name in friends:
    print(f"this the name: {name}")

print("=-"*20)

# now if you only want the value:

for age in friends.values():
    print(f"this is the ages: {age}")

print("=-"*20)

# tis you will get the name and the age using the .items
for name, age in friends.items():
    print(f"{name} is {age} years old")
