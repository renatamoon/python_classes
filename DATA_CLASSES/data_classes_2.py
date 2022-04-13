from audioop import add
import random
import string

def generate_id() -> str:
    return "".join(random.choices(string.ascii_uppercase, k=12))


class Person:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        

def main() -> None:
    person = Person(name="Jon", address="Rua Lobo Antonio, 20")
    print(person) # <__main__.Person object at 0x7f5fc6334790>


if __name__ == "__main__":
    main()
