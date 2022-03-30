# ADVANCED SET OPERATIONS

art_friends = {"Rolf", "Anne", "Jen"}
science_friends = {"Jen", "Charlie"}

art_but_not_science = art_friends.difference(science_friends)
science_but_not_art = science_friends.difference(art_friends)

print("OUTPUT: ", art_but_not_science) # OUTPUT:  {'Rolf', 'Anne'}
print("OUTPUT: ", science_but_not_art) # OUTPUT:  {'Charlie'}

print("=-"*20)

"""members that are not in both sets"""

not_in_both = art_friends.symmetric_difference(science_friends)
print("OUTPUT: ", not_in_both) # OUTPUT:  {'Anne', 'Rolf', 'Charlie'}

print("=-"*20)

"""members that are in both sets"""

art_and_science = art_friends.intersection(science_friends)
print("OUTPUT: ", art_and_science) # OUTPUT:  {'Jen'}

print("=-"*20)

"""UNITING BOTH SETS"""

all_friends = art_friends.union(science_friends)
print("OUTPUT: ", all_friends) # OUTPUT:  {'Charlie', 'Jen', 'Rolf', 'Anne'}
