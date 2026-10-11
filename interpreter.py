import math

from values import Number, Variables
from operation import addition, substraction, multiplication


class Interpreter:
    def __init__(self, steps=None):
        self.steps = steps if steps is not None else []

    def visit(self, node):
        name = type(node).__name__
        if name == "NumberNode":
            variables = [Variables(item['coef'], item['variable']) for item in node.value['variables'] or []]
            return Number(node.value['constant'], variables)
        if name == "PlusNode":
            return self.visit(node.node)
        if name == "MinusNode":
            value = self.visit(node.node)
            return Number(-value.constant, [Variables(-v.coef, v.variables) for v in value.variables])
        if name == "FunctionNode":
            argument = self.visit(node.argument)
            if argument.variables:
                atom = f"@{node.name}({argument})"
                return Number(0, [Variables(1, {atom: 1})])
            functions = {"sin": math.sin, "cos": math.cos, "tan": math.tan,
                         "sqrt": math.sqrt, "log": math.log, "ln": math.log,
                         "exp": math.exp, "abs": abs}
            return Number(functions[node.name](argument.constant), [])

        left, right = self.visit(node.node_a), self.visit(node.node_b)
        if name == "AddNode":
            result = addition.linear(left, right)
        elif name == "SubtractNode":
            result = substraction.linear(left, right)
        elif name == "MultiplyNode":
            result = multiplication.linear(left, right)
        elif name == "DivideNode":
            result = self._divide(left, right)
        else:
            raise TypeError(f"Unsupported syntax node: {name}")
        self.steps.append(f"{node} = {result}")
        return result

    @staticmethod
    def _divide(left, right):
        if right.constant == 0 and not right.variables:
            raise ValueError("Division by zero")
        if not right.variables:
            return Number(left.constant / right.constant,
                          [Variables(v.coef / right.constant, v.variables) for v in left.variables])
        if right.constant or len(right.variables) != 1:
            raise ValueError("Division is supported only by a non-zero constant or a single monomial")
        divisor = right.variables[0]
        terms = []
        if left.constant:
            terms.append(Variables(left.constant / divisor.coef,
                                   {name: -power for name, power in divisor.variables.items()}))
        for term in left.variables:
            powers = term.variables.copy()
            for name, power in divisor.variables.items():
                powers[name] = powers.get(name, 0) - power
            terms.append(Variables(term.coef / divisor.coef, powers))
        return Number(0, terms)
