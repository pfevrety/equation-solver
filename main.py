######## IMPORT ##########
from lexer import Lexer
from parser_ import Parser
from interpreter import Interpreter

######## GET EQUATIONS #########
print('Equation du premier degré.')
equation = "(5 + 6) * 7 * 7 + 48 = (5 * (2*3)) * 36" ##list(str(input("Entrez votre équation >")).replace(' ', ''))
print(f"L'équation entré est > {equation}")
possible_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "x", "=", "+", "-", "/", "*", " ", ".", "(", ")"]

count = 0
equation_part1 = str()
equation_part2 = str()

if "=" not in equation:
    print("Manque le signe '='")
    quit()

for i in equation:
    if i not in possible_characters:
        print(i)
        print("Charactère mauvais")
        quit()

    if i == "=":
        if count == 0:
            print("Erreur dans l'expression de l'ééquation")
            quit()
        else:
            equation_part1 = equation[:count]
            equation_part2 = equation[(count + 1 - (len(equation)) ):]
            print(f"La premiere partie de l'équation est > {equation_part1} // {''.join(equation_part1)}" )
            print(f"La deuxieme partie de l'équation est > {equation_part2} // {''.join(equation_part2)}" )

    count += 1

print("L'équation est valide démarage de la phase de résolution:")

lexer = Lexer(str(''.join(equation_part1)))
tokens = lexer.generate_tokens()
parser = Parser(tokens)
tree = parser.parse()
interpreter = Interpreter()
value = interpreter.visit(tree)

lexer2 = Lexer(str(''.join(equation_part2)))
tokens2 = lexer2.generate_tokens()
parser2 = Parser(tokens2)
tree2 = parser2.parse()

interpreter = Interpreter()
value2 = interpreter.visit(tree2)
print(f'{value} = {value2}')