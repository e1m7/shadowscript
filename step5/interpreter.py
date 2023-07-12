
from tokens import Integer, Float

class Interpreter:                                             # класс интерпретатор
	def __init__(self, tree):                                    # инициализация интерпретатора
		self.tree = tree                                           # дерево операций

	def read_INT(self, value):                                   # функция для конвертации значения токена в INT
		return int(value)                                          # вернуть int(значения)

	def read_FLT(self, value):                                   # функция для конвертации значения токена в FLOAT
		return float(value)                                        # вернуть float(значение)

	def compute_bin(self, left, op, right):                      # функция compute_bin(левая часть, операция, правая часть) 
		left_type = left.type                                      # тип левого токена
		right_type = right.type                                    # тип правого токена

		left = getattr(self, "read_" + left_type)(left.value)      # значение левого токена
		right = getattr(self, "read_" + right_type)(right.value)   # значение правого токена

		if op.value == '+': output = left + right                  # операция +
		if op.value == '-': output = left - right                  # операция -
		if op.value == '*': output = left * right                  # операция *
		if op.value == '/': output = left / right                  # операция /

		if left_type == 'INT' and right_type == 'INT':             # если тип левой и правой части == INT, то...
			return Integer(output)                                   # ...вернуть токен Integer(результат)
		else:                                                      # если тип левой или правой части == FLOAT, то...
			return Float(output)                                     # ...вернуть токен Float(результат)

	def interpret(self, tree=None):                              # функция interpret(либо None, либо поддерево)
		if tree is None:                                           # если ничего не прислали, то...
			tree = self.tree                                         # ...tree = корневое дерево

		left_node = tree[0]                                        # левая нода = 0-ой элемент списка
		if isinstance(left_node, list):                            # если левая нода == поддерево, то... 
			left_node = self.interpret(left_node)                    # ...вычисляем ее interpret(левая нода)

		operator = tree[1]                                         # оператор = 1-ый элемент списка

		right_node = tree[2]                                       # правая нода = 2-ой элемент списка
		if isinstance(right_node, list):                           # если правая нода == поддерево, то...
			right_node = self.interpret(right_node)                  # ...вычисляем ее interpret(правая нода)

		return self.compute_bin(left_node, operator, right_node)   # вернуть операцию для левой и правой ноды 