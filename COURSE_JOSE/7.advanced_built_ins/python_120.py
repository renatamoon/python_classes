# generators

# instead of doing a counter you can do a yield:
def hundred_numbers():
    nums = []
    i = 0

    while i < 100:
        nums.append(i)
        i += 1
    return nums


print(hundred_numbers())


# doing the yield generator
def hundred_numbers_with_yield():
    i = 0

    while i < 100:
        yield i
        i += 1


generator = hundred_numbers_with_yield()
print(next(generator))  # printing the first generator which is 1
print(next(generator))  # printing the second number of the generator which is 2
