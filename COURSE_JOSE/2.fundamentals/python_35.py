# THE ELSE KEYWORD WITH LOOPS

cars = ["ok", "ok", "ok", "ok", "ok", "ok"]

all_successful = True

for status in cars:
    if status == "faulty":
        print(f"This car is {status}. STOPPING THE PRODUCTION LINE")
        # here's when you want to skip the falty car
        break
    print(f"This car is {status}. Shipping the car to the customer!")
else:
    print("ALL CARS BUILD SUCCESSFULLY. NO FAULTY CAR!")
