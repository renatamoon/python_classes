# BREAK AND CONTINUE

cars = ["ok", "ok", "ok", "faulty", "ok", "ok"]

# adding a break to stop the production 
for status in cars:
    if status == "faulty":
        print(f"This car is {status}. Stopping the production line to get the car OK")
        # the production will breka cause there is a faulty car
        break
    else:
        print(f"This car is {status}. Shipping the car to the customer!")

print("=-"*20)

# Now if we want only to skip the fauty car and then continue with the production
# we can use the "continue" so it will skip:

for status in cars:
    if status == "faulty":
        print(f"This car is {status}. SKIPPING")
        # here's when you want to skip the falty car
        continue
    print(f"This car is {status}. Shipping the car to the customer!")
