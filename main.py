from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

text = "x + 19 + y - 21 + x - y - y" #input("calc > ")
lexer = Lexer(text)
tokens = tuple(lexer.generate_tokens)
print("tokens", tokens)  # Done
parser = Parser(tokens)
tree = parser.parse()
print("tree", tree)
interpreter = Interpreter()
value = interpreter.visit(tree)
print(value)
