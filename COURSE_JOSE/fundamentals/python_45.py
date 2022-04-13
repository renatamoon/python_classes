# ARGUMENTS AND PARAMETERS

car = {
    "producer": "Ford",
    "model": "Fiesta",
    "mileage": 23000,
    "fuel_consumed": 460
}

mpg = car["mileage"] / car["fuel_consumed"]
name = f"{car['producer']} {car['model']}"

print(mpg) # 50.0
print(f"{name} does {mpg} miles per gallon") # Ford Fiesta does 50.0 miles per gallon

print("-="*20)

# instead of doing such a big code we can put it inside a function
# so refactoring will be:

def calculate_mgp():
    car_2 = {
        "producer": "Hyundai",
        "model": "HB20",
        "mileage": 120000,
        "fuel_consumed": 340
    }

    mpg = car_2["mileage"] / car_2["fuel_consumed"]
    name = f"{car_2['producer']} {car_2['model']}"

    print(f"{name} does {mpg} miles per gallon")

# to initialize a function and run the code:
calculate_mgp() # Hyundai HB20 does 352.94117647058823 miles per gallon

print("-="*20)
# now we're gonna pass parameters and attrs to the function, so it's not necessary to use only
# the same vars to follow the code

# we can the following way also:

# --------------- attributes and arguments

# ARGUMENT: is: value you pass in to the function
# PARAMETER: variable that accepts a value inside the function

cars = [
        {"producer": "Hyundai", "model": "Creta", "mileage": 20000, "fuel_consumed": 300},
        {"producer": "Chevrolet", "model": "Camaro", "mileage": 130000, "fuel_consumed": 320},
        {"producer": "Renault", "model": "Sandero", "mileage": 14000, "fuel_consumed": 550},
        {"producer": "Mercedes", "model": "S3", "mileage": 9000, "fuel_consumed": 450}
]


def calculate_mgp_new(car):  # function to calculate the miles per gallon
    mpg = car["mileage"] / car["fuel_consumed"]
    return mpg
    # if I put a return before the end of the code, all the peace of code after will not be executed

def car_name(car): # function to get the car name
    name = f"{car['producer']} {car['model']}"
    return name

def print_car_info(car): # function to get the car's info
    name = car_name(car)
    mpg = calculate_mgp_new(car)

    print(f"{name} does {mpg} miles per gallon")


for car in cars:
    print_car_info(car) # this will print all the cars in the list of cars

# return:
"""
Hyundai Creta does 66.66666666666667 miles per gallon
Chevrolet Camaro does 406.25 miles per gallon
Renault Sandero does 25.454545454545453 miles per gallon
Mercedes S3 does 20.0 miles per gallon """

print("-="*20)

# remeber that if you put return on the function before the end of the statement, it will never
# run cause it will always terminate ther function on the return.

def divide(x, y):
    if y == 0:
        return "You tried to devide by zero"
    else:
        return x / y

calc = divide(10, 2)
print(calc) # 5.0

calc2 = divide(5, 0)
print(calc2) # You tried to devide by zero
