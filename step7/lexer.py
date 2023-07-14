
from tokens import *

class Lexer:
	digits = '0123456789'                          # цифры, которые обрабатываем
	letters = 'abcdefghijklmnopqrstuvwxyz'         # символы, которые можно в имени
	operations = '+-*/()='                         # операции в один символ
	stopwords = [' ']                              # стоп-слова (пропуски)
	declarations = ['make']                        # ключевые слова

	def __init__(self, text):
		self.text = text
		self.idx = 0
		self.tokens = []
		self.char = self.text[self.idx]
		self.token = None

	def tokenize(self):
		while self.idx < len(self.text):

			if self.char in Lexer.digits:
				self.token = self.extract_number()

			elif self.char in Lexer.operations:
				self.token = Operation(self.char)
				self.move()

			elif self.char in Lexer.stopwords:
				self.move()
				continue

			elif self.char in Lexer.letters:           # если текущий символ из имени
				word = self.extract_word()               # собираем слово, которое нам прислали
				if word in Lexer.declarations:           # если оно ключевое, то...
					self.token = Declarations(word)        # ...токен = определение(слова)
				else:                                    # если оно не ключевое, то...  
					self.token = Variable(word)            # ...токен = переменная(слово)

				
			self.tokens.append(self.token)
		return self.tokens

	def extract_number(self):
		number = ''
		isFloat = False
		while ((self.char in Lexer.digits or self.char == '.') and (self.idx < len(self.text))):
			if self.char == '.':
				isFloat = True
			number = number + self.char
			self.move()
		return Integer(number) if not isFloat else Float(number)

	def extract_word(self):
		word = ''
		while self.char in Lexer.letters and self.idx < len(self.text):
			word = word + self.char
			self.move()
		return word


	def move(self):
		self.idx = self.idx + 1
		if self.idx < len(self.text):
			self.char = self.text[self.idx]

