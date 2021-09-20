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
        if self.value[0] != None and self.value[1] != None:
            return f"{self.value[1]}x + {self.value[0]}"
        if self.value[1] != None:
            return f"{self.value[1]}x"
        if self.value[0] != None:
            return f"{self.value[0]}"

        return f"{self.value}"

    def type(self):
        return "LITERAL"