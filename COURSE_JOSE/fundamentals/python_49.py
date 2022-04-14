# FIRST CLASS FUNCTIONS
"""just like strings and integers we can assign into variables and pass 
into arguments to other function"""

def greet():
    print("Hello")

hello = greet

hello() # here's what the assingment is ... we can pass the function into any var and the
# execute it

# ----------------------------

# def average(seq):
#     return sum(seq) / len(seq)

# in lambda function
avg = lambda seq: sum(seq) / len(seq)
total = lambda seq: sum(seq)
top = lambda seq: max(seq)

# doing a map to associate what the users inputs with the operations above
operations = {
    "average": avg,
    "total": total,
    "top": top
}

students = [
    {"name": "Rolf", "grades": (67, 90, 95, 100)},
    {"name": "Denise", "grades": (10, 78, 80, 90)},
    {"name": "Harry", "grades": (98, 90, 95, 99)},
    {"name": "Parvati", "grades": (100, 100, 95, 100)},
]

for student in students:
    name = student["name"]
    grades = student["grades"]

    print(f"Student: {name}")
    operation = input("Enter 'average', 'total', or 'top': ").lower()

    operation_function = operations[operation]
    print(operation_function(grades))
