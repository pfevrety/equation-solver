from tokens import Token, TokenType
from math import pi, e

WHITESPACE = ' \n\t'
DIGITS = '0123456789'
special_numbers = {"π": pi, "e": e}
constant = tuple(special_numbers.keys())


def format_and_verify_expression(expression):
	counter = 0
	parens_counter = 0
	operator = ("+", '-', '*', '/')
	expression_l = list(expression.replace(' ',''))
	expression_length = len(expression_l)

	while counter < expression_length:
		if expression_l[counter] == '(':
			parens_counter += 1
			if counter < expression_length - 1 and expression_l[counter + 1] == ')':
				raise Exception("Invalid expression")

			if counter > 0 and (expression_l[counter - 1].isdigit() or expression_l[counter - 1].isalpha()):
				expression_l.insert(counter, '*')
				expression_length += 1
				counter += 1

		elif expression_l[counter] == ')':
			parens_counter -= 1
			if parens_counter < 0:
				raise Exception("Parens issue")
			if counter < expression_length - 1:
				if expression_l[counter + 1].isdigit() or expression_l[counter + 1].isalpha() or \
						expression_l[counter + 1] == '(':
					expression_l.insert(counter + 1, '*')
					expression_length += 1

		elif expression_l[counter].isdigit() or expression_l[counter].isalpha():
			if counter < expression_length - 1 and expression_l[counter + 1].isalpha():
				expression_l.insert(counter + 1, '*')
				expression_length += 1
			if counter > 0 and expression_l[counter - 1].isalpha():
				expression_l.insert(counter, '*')
				expression_length += 1

		elif expression_l[counter] in operator:
			if (counter < expression_length - 1 and expression_l[counter + 1] == ')') or (
					counter > 0 and expression_l[counter - 1] == '('):
				raise Exception("Invalid expression")
		counter += 1

	if parens_counter != 0:
		raise Exception("Invalid parens")

	return expression_l

class Lexer:
	def __init__(self, text):
		self.text = iter(format_and_verify_expression(text))
		self.advance()

	def advance(self):
		try:
			self.current_char = next(self.text)
		except StopIteration:
			self.current_char = None

	@property
	def generate_tokens(self):
		while self.current_char is not None:
			if self.current_char in WHITESPACE:
				self.advance()
			elif self.current_char in constant:
				token = Token(TokenType.NUMBER, {'constant': special_numbers[self.current_char], 'variables': None})

				self.advance()
				yield token
			elif self.current_char == '.' or self.current_char in DIGITS:
				yield self.generate_number()
			elif self.current_char.isalpha():
				token = Token(TokenType.NUMBER, {'constant': 0.0, 'variables': [{'name': self.current_char, 'coef': 1, 'variable': {self.current_char: 1}}]})
				self.advance()
				yield token
			elif self.current_char == '+':
				self.advance()
				yield Token(TokenType.PLUS)
			elif self.current_char == '-':
				self.advance()
				yield Token(TokenType.MINUS)
			elif self.current_char == '*':
				self.advance()
				yield Token(TokenType.MULTIPLY)
			elif self.current_char == '/':
				self.advance()
				yield Token(TokenType.DIVIDE)
			elif self.current_char == '(':
				self.advance()
				yield Token(TokenType.LPAREN)
			elif self.current_char == ')':
				self.advance()
				yield Token(TokenType.RPAREN)
			else:
				raise Exception(f"Illegal character '{self.current_char}'")

	def generate_number(self):
		decimal_point_count = 0
		number_str = self.current_char
		self.advance()

		while self.current_char is not None and (self.current_char == '.' or self.current_char in DIGITS):
			if self.current_char == '.':
				decimal_point_count += 1
				if decimal_point_count > 1:
					break
			
			number_str += self.current_char
			self.advance()

		if number_str.startswith('.'):
			number_str = '0' + number_str
		if number_str.endswith('.'):
			number_str += '0'
		return Token(TokenType.NUMBER, {'constant': float(number_str), 'variables': None})
