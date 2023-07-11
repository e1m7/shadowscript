

class Parser:                                                    # класс парсер
	def __init__(self, tokens):                                    # иницилизация нового парсера токенами
		self.tokens = tokens                                         # токены, которые получил парсер
		self.idx = 0                                                 # индекс текущего токена
		self.token = self.tokens[self.idx]                           # текущий токен

	def factor(self):                                              # фактор (либо целое число, либо вещественное число)
		if self.token.type == 'INT' or self.token.type == 'FLT':     # если тип токена == INT|FLT, то...
			return self.token                                          # ...вернуть токен

	def term(self):                                                # термин (фактор *|/ фактор)
		left_node = self.factor()                                    # левая нода = фактор
		self.move()                                                  # следующий токен
		output = left_node                                           # результат = левая нода 
		if self.token.value == '*' or self.token.value == '/':       # если значение текущего токена == *|/, то...
			operation = self.token                                     # 1) сохраним операцию
			self.move()                                                # 2) следующий токен
			right_node = self.factor()                                 # 3) правая нода = фактор
			self.move()                                                # 4) следующий токен
			output = [left_node, operation, right_node]                # 5) результат = [левая нода, операция, правая нода]
		return output                                                # вернуть результат

	def expression(self):                                          # выражение (термин +|- термин)
		left_node = self.term()                                      # левая нода = термин
		output = left_node                                           # результат = левая нода 
		if self.token.value == '+' or self.token.value == '-':       # если значение текущего токена == +|-, то... 
			operation = self.token                                     # 1) сохраним операцию
			self.move()                                                # 2) следующий токен
			right_node = self.term()                                   # 3) правая нода = термин
			output = [left_node, operation, right_node]                # 4) результат = [левая нода, операция, правая нода]
		return output                                                # вернуть результат

	def parse(self):                                               # распарсить список токенов (превратить в дерево)
		return self.expression()                                     # вернуть вычисленное выражение

	def move(self):                                                # функция move (новый токен)
		self.idx = self.idx + 1                                      # увеличить индекс токена
		if self.idx < len(self.tokens):                              # если индекс в пределах списка токенов, то...
			self.token = self.tokens[self.idx]                         # прочитать текущий токент из списка