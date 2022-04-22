# MAGIC METHODS IN PYTHON

from smtplib import SMTPRecipientsRefused


class Animal:
    def __init__(self, name):
        self.name = name

animals = ["bear", "dog"]

print(animals.__class__) # <class 'list'>
print(len(animals)) # 2

print("=-"*20)

class Garage:
    def __init__(self):
        self.cars = []

    # to get the lenght of the list we need another dunder method
    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i): # get the first index
        return self.cars[i]

    def __repr__(self): # defining a reper - printing out the string to represent a string
        return f'<Garage {self.cars}>'

    def __str__(self): # 
        return f"Garage with {len(self)} cars"


ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("Focus")

print("Cars in the garages: ", len(ford))
print(ford.cars[0]) # fiesta
print(ford[0]) # the same things as Garage.__getitem__(ford, 0)

for car in ford:
    print(car)

print(ford)