# --------------- TUPLES IN PYTHON

"""Tuples are used when it cannot be changed, so if you want it to keep it unchanged, then use tuples,
otherwise a List if a better way to append or remove elements."""

# this is a good example of a tuple, but a way better to express it is to put brackets ()
short_tupple = "Rolf", "Bob"

# putting brackets on the tuple
short_tuple_correct = ("Rolf", "Bob")

# tupple inside a list
tupple_in_list = [("Rolf", "Bob")]

# the example bellow is not a tuple, just a string
not_a_tuple = "Rolf" 

"""How to append the value of a tuple"""
friends = ("Rolf", "Bob", "Anne")
# friends.append("Jen") # this is not going to work cause the tuple has not the attribute append

"""If you want to append an element to a tuple, you have to get the tuple and add + with the element"""

friends = friends + ("Jen",)
print("THE OUTPUT IS: ", friends) # THE OUTPUT IS:  ('Rolf', 'Bob', 'Anne', 'Jen')

