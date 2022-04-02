# DESTRUCTING SINTAX

currencies = 0.8, 1.2 # this is a tuple

usd, eur = currencies
print(usd) # 0.8
print(eur) # 1.2

print("=-"*20)

friends = [
    ("Rolf": 25), 
    ("Anne": 37),
    ("Charlie": 31),
    ("Bob": 22)
    ]

for name, age in friends:
    print(f"{name} is {age} years old")

# the output
"""
Rolf is 25 years old
Anne is 37 years old
Charlie is 31 years old
Bob is 22 years old """