# FILTER FUNCTION - call for any file or program that requires 2 parameters

def starts_with_r(friend):
    return friend.startswith("R")


friends = ["Rolf", "Jose", "Randy", "Anna", "Mary"]

# start_with_r = filter(starts_with_r, friends)  # arg 1: function that return true or false
#
# print(next(start_with_r))  # Randy
# print(next(start_with_r))  # Rolf
# # print(next(start_with_r))  # StopIteration
#
# print(list(start_with_r))  # list of the names that starts with R


def my_custom_filter(func, iterable):
    for i in iterable:
        if func(i):
            yield i


start_with_r = my_custom_filter(lambda friend: friend.startswith("R"), friends)

another_starts_with_r = (f for f in friends if f.startswith("R"))
