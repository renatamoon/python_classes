""" ---------- HOW DATA CLASSESS WORK

Python data classes are - as you'd expect - in particular suitable to model classes that 
represent data, and as such they offer easy mechanisms to initialize, print, order, sort 
and compare data.

Note that although I'm using a sort_index attribute, strictly speaking that's not needed 
in this case, because a data class uses a tuple of its attributes in the class definition 
as the default for sorting. I'm not a fan of this kind of hidden behavior, so I prefer to 
do it explicitly (using something that is called sort_index in this case). Another advantage
of using a separate field, is that you can do more complicated ordering, using for example
a weighted combination of age and strength.

"""
from dataclasses import dataclass

# instead of doing a normal class with constructor and passing the attrs we can do the following way

class Person:
    name: str
    job: str
    age: int
    
    
    def __init__(self, name, job, age):
        self.name = name
        self.job = job
        self.age = age
        

person1 = Person("Geralt", "witcher", 30)
person2 = Person("Yennefer", "Sorceress", 25)
person3 = Person("Yennefer", "Sorceress", 25)

# print(id(person2)) # 140550521716352
# print(id(person3)) # 140550521716544
# print(person1) # <__main__.Person object at 0x7fd477eb7e20> False

# print(person3 == person2)


# ------------- using dataclasses: In this case we don't need the initializer (__init__) cause
# the dataclass already does it for us. It's important that we provide the attrs of Dog Animal,
# cause the dataclass knows the type of data it is dealing with

@dataclass(order=True) # in case you wanna compare data it's required order=True
class Dog:
    name: str
    breed: str
    age: int
    

animal1 = Dog("Harry", "Labrador", 12)
animal2 = Dog("Justin", "Golden", 5)
animal3 = Dog("Selena", "Bulldog", 2)

print(id(animal1)) # 140458151013488
print(id(animal2)) # 140458150614688
print(animal3) # Dog(name='Selena', breed='Bulldog', age=2)
print(animal3 == animal2) # False
print(animal1>animal2)