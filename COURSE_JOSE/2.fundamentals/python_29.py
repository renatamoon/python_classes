# FOR LOOPS

friends = ["Rolf", "Jen", "Anne"]
"""
for friend in friends:
    print(friend) """

print("=-"*20)

elements = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for element in elements:
#     print(element)

for i in range(5, 10):
    print(i)

print("=-"*20)

students = [
    {"name": "Rolf Smith", "grade": 90},
    {"name": "Renata Monteiro", "grade": 78},
    {"name": "Renato Romeo", "grade": 80},
]

for student in students:
    name = student["name"]
    grade = student["grade"]
    print(f"{name} has a grade of {grade}")

# OUTPUTS
#Rolf Smith has a grade of 90
# Renata Monteiro has a grade of 78
# Renato Romeo has a grade of 80