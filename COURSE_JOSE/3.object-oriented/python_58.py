"""OBJECT ORIENTED PROGRAMMING
An object stores datas an also functions. Something that a simple dictionary doesn't do.
So, if I want to put a function inside a dictionary, this won't be possible.

That's why we'll use Object Oriented Programming. So we can use objects that is way more
maleable than a dictionary.

- Objects are data storages that can have a lot of attrs and also methods.

"""

my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99],
    'average': 1 # function here
}

def average_grade(student):
    return sum(student["grades"]) / len(student['grades'])

print("The average grade is: ", average_grade(my_student))
print("-="*20)

# -----------------------------------------------------------
"""What an object looks like? First we need to define it by using a class:"""

class Student:
    # dunder functions that have constructors that can receive attributes
    def __init__(self, new_name, new_grades):
        self.name = new_name
        self.grades = new_grades

    # this is a method that the Class Object will do
    def average(self):
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf', [67, 50, 87, 90])
student_two = Student('Jose', [98, 87, 82, 99])

# --- student 1
print("The Student Name: ", student_one.name)
print("The Grades: ", student_one.grades)
print("The Average Grade: ", student_one.average())

print("=-"*20)
# ---- student 2
print("The Student Name: ", student_two.name)
print("The Grades: ", student_two.grades)
print("The Average Grade: ", student_two.average())