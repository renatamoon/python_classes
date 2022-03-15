# Python string format

age = 34
name = "Jose"
age_as_str = str(age)

print("You are" + age)

print("xxxxxxx")

name_presentation = f"My name is {name}"
print(name_presentation)

# ------------

name = "Renata"
final_greeting = "How are you, {}"
renata_greeting = final_greeting.format(name)
print(renata_greeting)

# ----------- f strings

another_greeting = f'How are you, {name}?'
print(another_greeting)

description = "{} is {age} years old."
print(description.format("Bob", age=30))