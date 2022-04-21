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


ford = Garage()
ford.cars.append("Fiesta")
ford.cars.append("Focus")

print("Cars in the garages: ", len(ford))
print(ford.cars[0]) # fiesta