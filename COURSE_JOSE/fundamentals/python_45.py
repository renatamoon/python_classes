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


def calculate_mgp_new(car, intro): 
    mpg = car["mileage"] / car["fuel_consumed"]
    name = f"{car['producer']} {car['model']}"

    print(f"{name} does {mpg} miles per gallon")


for car in cars:
    calculate_mgp_new(car, "New Car") # this will print all the cars in the list of cars
