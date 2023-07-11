

class Interpreter:
	def __init__(self, tree):
		self.tree = tree

	def compute_bin(self, left, op, right):
		if left.type == 'INT': 
			left = int(left.value) 
		elif left.type == 'FLT': 
			left = float(left.value)

		if right.type == 'INT': 
			right = int(right.value) 
		elif right.type == 'FLT': 
			right = float(right.value)

		if op.value == '+': return left + right
		if op.value == '-': return left - right
		if op.value == '*': return left * right
		if op.value == '/': return left / right


	def interpret(self):                               # функция interpret (вычислить дерево)
		left = self.tree[0]                              # 1) 0-ой элемент дерева
		operator = self.tree[1]                          # 2) 1-ый элемент дерева
		right = self.tree[2]                             # 3) 2-ой элемент дерева
		return self.compute_bin(left, operator, right)   # вернуть результат (+, -, *, /)