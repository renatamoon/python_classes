# SETS in PYTHON
# the difference between sets and lists/tuples is that sets don't hold order and don't have
# duplicated elements

art_friends = {"Rolf", "Anne"}

science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")

print("the art friends: ", art_friends)

art_friends.remove("Jen")

print("the art friends now: ", art_friends)

# the most usefull examples of why using sets if because they do not duplicate the items
# and also we can check what elements are in this set, or in the other set.