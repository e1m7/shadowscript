

class Parser:
	def __init__(self, tokens):
		self.tokens = tokens
		self.idx = 0
		self.token = self.tokens[self.idx]


	def factor(self):
		if self.token.type == 'INT' or self.token.type == 'FLT':
			return self.token


	def term(self):
		left_node = self.factor()                                       # левая нода = фактор
		self.move()                                                     # следующий токен
		while self.token.value == '*' or self.token.value == '/':       # цикл пока текущий токен == *|/
			operation = self.token                                        # 1) запоминаем операцию (*|/)
			self.move()                                                   # 2) следующий токен
			right_node = self.factor()                                    # 3) правая нода = фактор
			self.move()                                                   # 4) следующий токен
			left_node = [left_node, operation, right_node]                # 5) левая нода = [левая нода, операция, правая нода]
		return left_node                                                # вернуть левую ноду


	def expression(self):
		left_node = self.term()
		while self.token.value == '+' or self.token.value == '-':
			operation = self.token
			self.move()
			right_node = self.term()
			left_node = [left_node, operation, right_node]
		return left_node


	def parse(self):
		return self.expression()


	def move(self):
		self.idx = self.idx + 1
		if self.idx < len(self.tokens):
			self.token = self.tokens[self.idx]