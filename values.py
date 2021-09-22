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

    a = value[0]
    b = value[1]
    c = value[0]

    def __repr__(self):
        a = self.value[0]
        b = self.value[1]
        c = self.value[0]

        if a != None and b != None and c != None:
            return f"{a} + {b}x + {c}x^2"
        if b != None and c != None:
            return f"{b}x + {c}x^2"
        if c != None:
            return f"{c}x^2"
        if a != None and b != None:
            return f"{b}x + {a}"
        if b != None:
            return f"{b}x"
        if a != None:
            return f"{b}"

        return f"{a}"

    def type(self):
        return "LITERAL"
