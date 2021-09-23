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

        for i, number in list(enumerate(self.value)):
            if i == 0:
                tmp.append(str(number))
            elif i == 1:
                tmp.append(f'{str(number)}x')
            else:
                tmp.append(f'{str(number)}x^{i}')

        return ' + '.join(tmp)

    def type(self):
        return "LITERAL"
