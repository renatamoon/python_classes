# CLASS METHODS AND STATIC METHODS

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

# renata = Student('Rolf', 'MIT')

# renata.marks.append(76)
# renata.marks.append(98)

# print(renata.average())

# ----------
""" usually you use the class method when you want something to have access to the methods
of the class"""

class Foo:
    @classmethod
    def hi(cls): # the cls, same as self it's holding the value of the class itself
        print(cls.__name__) # this gives us the name of the class Foo
        
my_obj = Foo()
my_obj.hi()

# ----------
"""usually you use the static method when you want the method that doesn't use the current object 
or the class but it's somehow related to it """

class Bar:
    @staticmethod
    def hi():
        print("Hello, I don\'t take parameters.")

another_obj = Bar()
another_obj.hi()