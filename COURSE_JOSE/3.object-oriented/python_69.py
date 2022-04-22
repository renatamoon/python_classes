# CLASS AND STATIC METHODS EXAMPLES

class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self) -> str:
        return f'<FixedFloat {self.amount:.2f}>'

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)


number = FixedFloat(18.5746)
print(number)

new_number = number.from_sum(12.456, 0.567)
print(new_number)


class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = 'EUR'

    def __repr__(self) -> str:
        return f'<Euro {self.symbol}{self.amount:.2f}>'

money = Euro.from_sum(23.576, 9.890)
print(money)