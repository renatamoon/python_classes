# LISTS IN PYTHON

friend1 = "Rolf"
friend2 = "Bob"
friend3 = "Anne"

print(friend1, friend2, friend3)

print("=-"*20)

"""We use it so we are allowed to input a lot of values inside a data. Instead of using the
a lot of vars, we use it like this: """

friends = ["Rolf", "Bob", "Anne"]

print("LIST OUTPUT: ", friends[0])
print("THE LENGH OF THE LIST IS:", len(friends))

print("=-"*20)

friends_list = [["Rolf", 24], ["Bob", 20], ["Anne", 25]]

print("ACCESS VALUE: ", friends_list[0]) # ACCESS VALUE:  ['Rolf', 24]
print("ACCESS VALUE: ", friends_list[0][0]) # ACCESS VALUE:  Rolf
print("ACCESS VALUE: ", friends_list[1][1]) # ACCESS VALUE:  20

print("=-"*20)
# how to do long lists and how to separete it

friends_long_list = [
    ["Anne", 25],
    ["Jennifer", 31],
    ["Luana", 22],
    ["Maria", 21],
    ["Stella", 32],
]

print("=-"*20)
# adding names to the list:

friends_simple_list = ["Rolf", "Bob", "Anne"]
friends_simple_list.append("Jen") # adding a name into to the friends lists

print("THE LIST OUTPUT IS:", friends_simple_list) # THE LIST OUTPUT IS: ['Rolf', 'Bob', 'Anne', 'Jen']

friends_simple_list.remove("Bob")
print("THE LIST OUTPUT NOW IS:", friends_simple_list) # THE LIST OUTPUT NOW IS: ['Rolf', 'Anne', 'Jen']