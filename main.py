"""Command-line entry point for the expression simplifier."""

import argparse

from interpreter import Interpreter
from lexer import Lexer
from parser_ import Parser
from derivation import derive


def parse(expression):
    tokens = tuple(Lexer(expression).generate_tokens)
    tree = Parser(tokens).parse()
    if tree is None:
        raise ValueError("Expression cannot be empty")
    return tree


def simplify(expression, variable=None, steps=None):
    """Parse and simplify an expression, optionally differentiating it."""
    tree = parse(expression)
    if variable:
        if len(variable) != 1 or not variable.isalpha():
            raise ValueError("The differentiation variable must be one letter")
        tree = derive(tree, variable)
    return Interpreter(steps).visit(tree)


def main():
    parser = argparse.ArgumentParser(description="Simplify arithmetic and polynomial expressions.")
    parser.add_argument("expression", nargs="?", help='Expression, for example: "2x + 3x - 4"')
    parser.add_argument("--derive", metavar="VARIABLE", help="Differentiate with respect to a variable, e.g. --derive x")
    parser.add_argument("--steps", action="store_true", help="Print intermediate simplification steps")
    args = parser.parse_args()
    expression = args.expression
    if expression is None:
        try:
            expression = input("expression> ")
        except EOFError:
            return 0
    try:
        steps = [] if args.steps else None
        result = simplify(expression, args.derive, steps)
        if args.derive:
            print(f"d/d{args.derive} ({expression}) = {result}")
        else:
            print(result)
        if args.steps:
            print("Steps:")
            for step in steps:
                print(f"  {step}")
    except (ValueError, ZeroDivisionError) as error:
        parser.error(str(error))
    except Exception as error:
        parser.error(f"Invalid expression: {error}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
