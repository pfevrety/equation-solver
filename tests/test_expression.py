import unittest

from lexer import Lexer
from main import parse, simplify
from nodes import AddNode, MultiplyNode
from parser_ import Parser
from tokens import TokenType


class LexerTests(unittest.TestCase):
    def test_implicit_multiplication_and_functions(self):
        tokens = list(Lexer("2x + sin(x)").generate_tokens)
        self.assertEqual(tokens[0].type, TokenType.NUMBER)
        self.assertEqual(tokens[1].type, TokenType.MULTIPLY)
        self.assertIn(TokenType.FUNCTION, [token.type for token in tokens])

    def test_rejects_unbalanced_parentheses(self):
        with self.assertRaises(Exception):
            list(Lexer("(x + 1").generate_tokens)


class ParserTests(unittest.TestCase):
    def test_precedence_builds_multiply_under_addition(self):
        tree = parse("2 + 3x")
        self.assertIsInstance(tree, AddNode)
        self.assertIsInstance(tree.node_b, MultiplyNode)

    def test_function_call_is_in_ast(self):
        self.assertIn("sin", repr(parse("sin(x)")))


class AlgebraTests(unittest.TestCase):
    def test_polynomial_product_combines_like_terms(self):
        self.assertEqual(str(simplify("(x + 1)(x + 2)")), "2 + 3x + x^2")

    def test_derivative_of_polynomial(self):
        self.assertEqual(str(simplify("x*x + 3x", variable="x")), "2x + 3")

    def test_symbolic_function_chain_rule(self):
        self.assertEqual(str(simplify("sin(x)", variable="x")), "cos(x)")

    def test_derivative_of_log_uses_negative_power(self):
        self.assertEqual(str(simplify("ln(x)", variable="x")), "x^-1")

    def test_steps_capture_reductions(self):
        steps = []
        simplify("(x + 1)(x + 2)", steps=steps)
        self.assertTrue(any("x^2" in step for step in steps))


if __name__ == "__main__":
    unittest.main()
