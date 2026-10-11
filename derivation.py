"""Symbolic differentiation rules for expression AST nodes."""

from nodes import (AddNode, DivideNode, FunctionNode, MinusNode, MultiplyNode,
                   NumberNode, PlusNode, SubtractNode)


def _number(value):
    return NumberNode({"constant": value, "variables": []})


def _product(left, right):
    return MultiplyNode(left, right)


def derive(node, variable):
    """Return the derivative AST with respect to a one-letter variable."""
    if isinstance(node, NumberNode):
        terms = []
        for term in node.value.get("variables") or []:
            powers = term["variable"].copy()
            power = powers.get(variable, 0)
            if power:
                coefficient = term["coef"] * power
                if power == 1:
                    del powers[variable]
                else:
                    powers[variable] -= 1
                terms.append({"name": "".join(sorted(powers)), "coef": coefficient, "variable": powers})
        return NumberNode({"constant": 0, "variables": terms})
    if isinstance(node, (PlusNode, MinusNode)):
        derivative = derive(node.node, variable)
        return PlusNode(derivative) if isinstance(node, PlusNode) else MinusNode(derivative)
    if isinstance(node, AddNode):
        return AddNode(derive(node.node_a, variable), derive(node.node_b, variable))
    if isinstance(node, SubtractNode):
        return SubtractNode(derive(node.node_a, variable), derive(node.node_b, variable))
    if isinstance(node, MultiplyNode):
        return AddNode(_product(derive(node.node_a, variable), node.node_b),
                       _product(node.node_a, derive(node.node_b, variable)))
    if isinstance(node, DivideNode):
        top = SubtractNode(_product(derive(node.node_a, variable), node.node_b),
                           _product(node.node_a, derive(node.node_b, variable)))
        bottom = _product(node.node_b, node.node_b)
        return DivideNode(top, bottom)
    if isinstance(node, FunctionNode):
        argument, inner = node.argument, derive(node.argument, variable)
        if node.name == "sin":
            outer = FunctionNode("cos", argument)
        elif node.name == "cos":
            outer = MinusNode(FunctionNode("sin", argument))
        elif node.name == "tan":
            tangent = FunctionNode("tan", argument)
            outer = AddNode(_number(1), _product(tangent, tangent))
        elif node.name == "exp":
            outer = FunctionNode("exp", argument)
        elif node.name in ("log", "ln"):
            outer = DivideNode(_number(1), argument)
        elif node.name == "sqrt":
            outer = DivideNode(_number(1), _product(_number(2), FunctionNode("sqrt", argument)))
        else:
            raise ValueError(f"No symbolic derivative rule for {node.name}")
        return _product(outer, inner)
    raise TypeError(f"No derivative rule for {type(node).__name__}")
