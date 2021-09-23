from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

while True:
    # try:
    text = input("expression > ")
    lexer = Lexer(text)
    tokens = lexer.generate_tokens()
    # print(list(tokens))  # [NUMBER.0: 1.0, PLUS.1, LITERAL.7 : 2]
    parser = Parser(tokens)
    tree = parser.parse()

    if not tree:
        continue
    interpreter = Interpreter()
    print(tree)
    print("Prioritées opératoires: " + str(tree))
    print(interpreter.visit(tree))
    # print(f"Resultats:\n\ta: 0,\n\tb: {r[0]},\n\tc: {r[2]}")




    # except Exception as e:
    #     print(e)
