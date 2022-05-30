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

my_range_obj = range(10)
print("RANGE: ", my_range_obj)  # isn't a generator that allows you to iterate - RANGE:  range(0, 10)
print(list(generator))


# exercise - generator
def prime_generator(bound):
    for n in range(2, bound):  # n starts from 2 to bound
        for x in range(2, n):  # check if there is a number x (1<x<n) that can divide n
            if n % x == 0:  # as long as we can find any such x, then n is not prime
                break
        else:  # if no such x is found after exhausting all 1<x<n
            yield n  # generate this prime


class PrimeGenerator:
    def __init__(self, stop):
        self.stop = stop
        self.start = 2

    def __next__(self):
        for n in range(self.start, self.stop):  # always search from current start (inclusive) to stop (exclusive)
            for x in range(2, n):
                if n % x == 0:  # not prime
                    break
            else:  # n is prime, because we've gone through the entire loop without having a non-prime situation
                self.start = n + 1  # next time we need to start from n + 1, otherwise we will be trapped on n
                return n  # return n for this round
        raise StopIteration()  # this is what tells Python we've reached the end of the generator
