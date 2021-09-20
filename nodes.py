from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return f'{self.value}'

# literal node


@dataclass
class LiteralNode:
    value: list

    def __repr__(self):
        if self.value[0] == None:
            return f'{self.value[1]}x'
        else:
            return f'({self.value[0]} + {self.value[1]}x)'


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a} + {self.node_b})'


@dataclass
class SubstractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a} - {self.node_b})'

# multiply node


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a} * {self.node_b})'

# divide node


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return f'({self.node_a} / {self.node_b})'


@dataclass
class PlusNode:
    value: float

    def __repr__(self):
        return f'(+{self.value})'


@dataclass
class MinusNode:
    value: float

    def __repr__(self):
        return f'(-{self.value})'
