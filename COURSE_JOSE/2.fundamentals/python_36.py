# FINDING PRIME NUMBERS WITH FOR LOOPS

for n in range(2, 10):
# here it will only iterate for every value between 2 till 10
    for x in range(2, n):
        # if the loop here doesn't break, then the number is a prime number.
        # if the loop break, then the number is not a prime number
        if n % x == 0:
            print(f"{n} equals to {x} = {n//x}. Not a prime number!")
            break
    else:
        print(f"{n} IS a prime number")
