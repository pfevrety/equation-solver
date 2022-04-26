from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

text = "1 + x + y + x + 0 + 2 + x + X + y + y + z" #input("calc > ")
lexer = Lexer(text)
tokens = tuple(lexer.generate_tokens)
# print("tokens", tokens)  # Done
parser = Parser(tokens)
tree = parser.parse()
# print("tree", tree)
interpreter = Interpreter()
value2 = interpreter.visit(tree)

print(value2)