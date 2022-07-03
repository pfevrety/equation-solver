from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter



text = "+2x+5x +2+ x+xxx" #input("calc > ")
lexer = Lexer(text[1:])
tokens = tuple(lexer.generate_tokens)
#print("tokens", tokens)  # Done
parser = Parser(tokens)
tree = parser.parse()
print("tree", tree)
interpreter = Interpreter()
value2 = interpreter.visit(tree)
print(value2)
value2.render()


def tout_faire(text):
    lexer = Lexer(text)
    tokens = tuple(lexer.generate_tokens)
    parser = Parser(tokens)
    tree = parser.parse()
    interpreter = Interpreter()
    return interpreter.visit(tree)



def test():
    tests = {
        '1 + (2 + 3)': '6',
        '(1 + 2 + 3) + 9.2': '15.2',
        '(1.1+2) + (2 + 3)': '8.1',
        '(1.1+x) + t + (2 + x + 3)': '6.1 + 2.0x + t',
        '(x+2) + (2 + 3) + v': '7 + x + v',
        '- 9.02 - x + 1.1 - x + x + x + x + y - t + x + o -o + x - x - x- x - x': '-7.92 - x + y - t',
        "-(x -(2)) + 2 - (t)": '4 - x - t',
        '2 * x * 1 * 2': '4.0x',
        "12 + xxxxy*(y + x + z) + 2 * y - x": "12 + y^2x^4 + x^5y + zyx^4 + 2.0y - x"
    }

    test_passed = 0
    test_failed = 0
    counter = 0
    for test in tests.keys():
        if str(tout_faire(test)) == tests[test]:
            test_passed += 1
        else:
            test_failed += 1
            print(f"{tests[test]} == {str(tout_faire(test))}")
        counter += 1

    
            
    print(f"Test passed: {test_passed}, Test failed: {test_failed}")


