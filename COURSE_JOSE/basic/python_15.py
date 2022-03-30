# and & or python
# Booleans - TRUE or FALSE

# age = int(input("ENTER YOUR AGE: "))

# can_learn_programming = age >= 18 and age <= 65

# print(f"At the age of {age}, you can learning programing: {can_learn_programming}")

# --------- BOOLEANS
print("=-"*20)

print(bool(30))
print(bool("Renata"))

print("=-"*20)

x = 35 or 4
y = 34 and 5
print(f"the value of X is {x}")
print(f"the value of Y is {y}")

print("=-"*20)

name = input("Enter your name: ")
surname = input("Enter your surname: ")

greeting = name or f"Mrs. {surname}"

print("HERE'S THE OUTPUT: ", greeting)

"""So, if here you can see that if you don't enter the name you enter your surname, your name
won't be added at the greeting sheet. The same occurs to the opposite act"""

print("=-"*20)
"""NOT - also we're using the booleans - TRUE or FALSE"""