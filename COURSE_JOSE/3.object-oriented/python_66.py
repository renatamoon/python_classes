# IHERETANCE

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


class WorkingStudent:
    def __init__(self, name, school, salary):
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary
    
    def average(self):
        return sum(self.marks) / len(self.marks)


# rolf = WorkingStudent('Rolf', 'MIT', 15.50)
# print(rolf.salary)
# rolf.marks.append(56)
# print(rolf.marks)


# -------------------- using Iheretance here and refactoring the code

class WorkingStudent(Student): # here we're saying that the Working student is ihereting of Student.
    # then it takes all methods of it and atributes
    def __init__(self, name, school, salary):
        super().__init__(name, school) # here we're calling the class Student
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 32


# ---------------- here we're using both classes WorkingStudent and Student to take the objects
rolf = WorkingStudent('Rolf', 'MIT', 15.50)
print("Salary: ", rolf.salary)
rolf.marks.append(56)
rolf.marks.append(99)
print("Average Salary: ", rolf.average())
print("Weekly Salary: ", rolf.weekly_salary())

# ---------------- here we're only taking the Student objects

anna = Student('Anna', 'Oxford')
print("Name: ", anna.name)
