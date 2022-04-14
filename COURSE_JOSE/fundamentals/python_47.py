# DEFAULT VALUES FOR PARAMETERS

"""Here I am passing a default value for Y (which is 3). Then when I pass the paramaters, It will only be
necessary the missing argument."""

from xml.etree.ElementInclude import default_loader


def add(x, y=3):
    total = x + y
    return total

print("Total is: ", add(5))

"""named arguments: passing a parameter as the way bellow: which you can put the named argument
and then pass the value as equals. Then it's not necessary to put the Y param cause it's already passed"""

print("Total is: ", add(x=3))

"""You can also add the 2 named params"""

print("Total is: ", add(x=3, y=2))

"""WARNING: here's an example of what cannot be done: put a non-named argument without the name on it. This will
cause an error: If the first argument has a name, then the sequel argument must have a name.
THE OPPOSITE CAN BE DONE, the first argument can have a non-named argument, but the second one also
can have it."""

# print("Total is: ", add(x=5, 2)) # SyntaxError: positional argument follows keyword argument

print("=-"*20)

default_v = 3

def sum(z, v=default_v):
    total = z + v
    print(total)

sum(2)