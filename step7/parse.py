
class Parser:
	def __init__(self, tokens):
		self.tokens = tokens
		self.idx = 0
		self.token = self.tokens[self.idx]

	def factor(self):
		if self.token.type == 'INT' or self.token.type == 'FLT':
			return self.token
		elif self.token.value == '(':
			self.move()
			expression = self.expression()
			return expression

	def term(self):
		left_node = self.factor()
		self.move()
		while self.token.value == '*' or self.token.value == '/':
			operation = self.token
			self.move()
			right_node = self.factor()
			self.move()
			left_node = [left_node, operation, right_node]
		return left_node

	def expression(self):
		left_node = self.term()
		while self.token.value == '+' or self.token.value == '-':
			operation = self.token
			self.move()
			right_node = self.term()
			left_node = [left_node, operation, right_node]
		return left_node

	def variable(self):
		if self.token.type == 'VAR':
			return self.token

	def statement(self):                                  # функция statement(вычисление присваивания или выражения)
		if self.token.type == 'DECL':                       # если текущий токен == DECL (присваивание), то...
			self.move()                                       # 1) следующий токен
			left_node = self.variable()                       # 2) левая нода = имя переменной
			self.move()                                       # 3) следующий токен
			if self.token.value == '=':                       # 4) если текущий токен == "=", то...
				operation = self.token                          # ...1) операция = текущий токен (=)
				self.move()                                     # ...2) следующий токен
				right_node = self.expression()                  # ...3) правый токен = выражение  
				return [left_node, operation, right_node]       # вернуть полученную ноду (левая, операция, право)

		# если не было DECL, то проверим что перед нами INT, FLT или OP, вернем выражение 
		elif self.token.type == 'INT' or self.token.type == 'FLT' or self.token.type == 'OP':
			return self.expression()

	def parse(self):                                      # функция parse (начало парсинга)
		return self.statement()                             # вернуть выражение формата "присваивание"

	def move(self):
		self.idx = self.idx + 1
		if self.idx < len(self.tokens):
			self.token = self.tokens[self.idx]