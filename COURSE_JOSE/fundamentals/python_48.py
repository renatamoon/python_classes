# LAMBDA FUNCTIONS
"""Are used to take imputes and return outputs
The purpose of the lambda functions: pass more simplicity to codes"""

def divide(x, y):
    return x / y

# you get the lambda keyword and then you get the inputs/arguments and then you put the return of the function
# this lambda function does the same thing of the divide function above
devide = lambda x, y: x / y

# here's another way to use lambda passing the values for the requires arguments
# why the two brackets? cause first you wanna run the lambda code, then you wanna pass the arguments
print((lambda x, y: x / y)(15, 3))

# ------------------------------------
print("=-"*20)

# def avarage(sequence):
#     return sum(sequence) / len(sequence)

# instead of using the function above we can do the lambda case:
average = lambda sequence: sum(sequence) / len(sequence)

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Denise", "grades": (10, 78, 80, 90)},
    {"name": "Harry", "grades": (98, 90, 95, 99)},
    {"name": "Parvati", "grades": (100, 100, 95, 100)},
]

for student in students:
    print(average(student["grades"]))
