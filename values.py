from dataclasses import dataclass


@dataclass
class Number:
    value: float

    def __repr__(self):
        return f"{self.value}"

    def type(self):
        return "NUMBER"

# create literal class


@dataclass
class Literal:
    value: list

    def __repr__(self):

        tmp = []

        print(self.value)
        for i, number in list(enumerate(self.value)):
            if i == 0 and number != None:
                tmp.append(str(number))
            elif i == 1 and number != None:
                tmp.append(f'{str(number)}x')
            elif number != None:
                tmp.append(f'{str(number)}x^{i}')

        return ' + '.join(tmp)

    def type(self):
        return "LITERAL"
