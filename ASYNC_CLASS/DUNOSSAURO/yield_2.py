
with open("potato.txt", 'w') as file:
    file.write("""
    I gotta tell you what I'm feeling inside
    I could lie to myself, but it's true
    There's no denying when I look in your eyes
    Girl I'm out of my head over you
    And I lived so long believing all love is blind
    But everything about you is telling me this time
    """)

tab = open("potato.txt")

print(tab) # <_io.TextIOWrapper name='potato.txt' mode='r' encoding='UTF-8'>

print(next(tab))

g = open("potato.txt").read()
print(g)

g = open("potato.txt").readlines

print("-="*20)

map(lambda x: x, [1,2,3])

m = map(lambda x: x, [1,2,3])

print("this is the generator: ", next(m)) # 1
print("this is the generator: ", next(m)) # 2
print("this is the generator: ", next(m)) # 3
# print("this is the generator: ", next(m)) # StopIteration -  because the generator goes until 3


# ------------- subgeradores

print("=-"*20)

def odd(r):
    yield from (n for n in range(r) if n % 2 == 1)


def subchapters():
    yield 1.1
    yield 1.2
    yield 1.3

def chapters():
    yield 1
    yield from subchapters()
    yield 2


c = chapters()

print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))


print("=-"*20)
print("YIELD FROM")


# how to iterate with generators under a function
def my_generator():
    yield from [1,2,3,4,5]


def without_from():
    for value in [1,2,3,4,5]:
        yield value

