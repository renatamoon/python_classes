# Live 151 - Yield e Funções geradoras

""" Yield significa gerar/produzir algo. Simplificar o ssitema de callbacks.

"""

def generator_function():
    yield 1

# print(generation_function())
# <generator object generation_function at 0x7f5046a04b30> - retorna um objeto
# um gerador é uma coisa que vc pode iterar sobre.

generator = generator_function()

"""

for value in generator:
    print("this is the value: ", value)
    # print = this is the value:  1 """

# para produzir o proximo item na iteração, sem a necessidade de "for", podemos usar a função next()

print("FIRST GENERATOR", next(generator))
# return = 1

# print(next(generator))
"""return = StopIteration - there's no way to generate another value - the ideia here is that this is yield values are
consumables, there's no way to access the next value or previews values."""

print("=-"*20)

def second_generator_function():
    yield 1
    yield 2
    yield 3


generator_2 = second_generator_function()

# Stop Condition - the function next calls the next generated value on the generated function that this function
# produce.

print("Result 1: ", next(generator_2)) # Result 1:  1
print("Result 2: ", next(generator_2)) # Result 2:  2
print("Result 3: ", next(generator_2)) # Result 3:  3
# print("Result 4: ", next(generator_2)) # Result 4: StopIteration


print("=-"*20)

def gen():
    yield "Renata"
    yield "Python"

generator_3 = gen()

print("the first generated value is: ", next(generator_3))
print("the second generated value is: ", next(generator_3))

# there's no way to return to the previews value, only the next one until the stop condition


print("=-"*20)

def generator_function_print():
    print("start here")
    print("before --- 1")
    yield 1
    print('before --- 1')
    print("after --- 2")
    yield 2
    print('after --- 2')
    print("end of the function")

generator_4 = generator_function_print()
print("The generated value is: ", next(generator_4)) # The generated value is:  1
print("The next generated value is: ", next(generator_4)) # The next generated value is:  2

print("=-"*20)

for value in generator_4:
    print("The value is: ", value)


print("=-"*20)

# odd = odd
def odd():
    value = 1

    while True:
        yield value
        value += 2

result = odd()

print("the odd value is: ", next(result))
print("the next odd value is: ", next(result))

# we're producing the values when the function is called.

print("=-"*20)

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