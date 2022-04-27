from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

text = "-(x -(2)) + 2 - (t)" #input("calc > ")
lexer = Lexer(text)
tokens = tuple(lexer.generate_tokens)
#print("tokens", tokens)  # Done
parser = Parser(tokens)
tree = parser.parse()
#print("tree", tree)
interpreter = Interpreter()
value2 = interpreter.visit(tree)

def tout_faire(text):
    lexer = Lexer(text)
    tokens = tuple(lexer.generate_tokens)
    parser = Parser(tokens)
    tree = parser.parse()
    interpreter = Interpreter()
    return interpreter.visit(tree)


def test():
    test1 = '1 + (2 + 3)'
    print(test1, '=', tout_faire(test1), '== 6')
    
    test2 = '(1 + 2 + 3) + 9.2'
    print(test2, '=', tout_faire(test2), '== 15.2')
    
    test3 = '(1.1+2) + (2 + 3)'
    print(test3, '=', tout_faire(test3), '== 8.1')

    test4 = '(1.1+2) + x'
    print(test4 , '=', tout_faire(test4), '== 3.1 + x')

    test5 = '(1.1+x) + t + (2 + x + 3)'
    print(test5, '=', tout_faire(test5), '== 6.1 + 2x + t')

    test6 = '(x+2) + (2 + 3) + v'
    print(test6, '=', tout_faire(test6), '== 7 + x + v')

    test7 = '- 9.02 - x + 1.1 - x + x + x + x + y - t + x + o -o + x - x - x- x - x'
    print(test7, '=', tout_faire(test7), '== -7.92 - x + y - t')

    test8 = "-(x -(2)) + 2 - (t)"
    print(test8, '=', tout_faire(test8), '== 4 - x - t')


test()