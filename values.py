from dataclasses import dataclass

@dataclass
class Number:
    value: float

    def __repr__(self):
        return f"{self.value}"