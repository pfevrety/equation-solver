from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter
while True:
    try:
        text = input("expression > ")
        lexer = Lexer(text)
        tokens = lexer.generate_tokens()
        # print(list(tokens))  # [NUMBER.0: 1.0, PLUS.1, LITERAL.7 : 2]
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree:
            continue
        interpreter = Interpreter()
        print(interpreter.visit(tree))
        print(tree)
    except Exception as e:
        print(e)
