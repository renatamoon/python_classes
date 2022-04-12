# ENUMERATE FUNCTION

friends = ["Rolf", "Bob", "Jen", "Anne"]
"""
counter = 0

for friend in friends:
    print(counter)
    print(friend)

    counter += 1 """

# print =
# 1
# Bob
# 2
# Jen
# 3
# Anne

# the enumerate function do the exactly same thing. But without attr a variable and with a lot more
# performance

for counter, friend in enumerate(friends):
    print(counter)
    print(friend)

print(list(enumerate(friends))) # [(0, 'Rolf'), (1, 'Bob'), (2, 'Jen'), (3, 'Anne')]

# if you want to also use zip to enumerate, you can.

print(list(zip([0, 1, 2], friends))) # [(0, 'Rolf'), (1, 'Bob'), (2, 'Jen')]