
from tokens import Integer, Float


class Interpreter:
	def __init__(self, tree, base):
		self.tree = tree
		self.data = base


	def read_INT(self, value):
		return int(value)


	def read_FLT(self, value):
		return float(value)


	def read_VAR(self, id):
		variable = self.data.read(id)
		variable_type = variable.type
		return getattr(self, 'read_' + variable_type)(variable.value)


	def compute_bin(self, left, op, right):
		left_type = 'VAR' if str(left.type).startswith('VAR') else str(left.type)
		right_type = 'VAR' if str(right.type).startswith('VAR') else str(right.type)

		if op.value == '=':
			left.type = "VAR(" + right_type + ")"
			self.data.write(left, right)
			return self.data.read_all() 

		left = getattr(self, "read_" + left_type)(left.value)
		right = getattr(self, "read_" + right_type)(right.value)

		if op.value == '+': 
			output = left + right
		elif op.value == '-': 
			output = left - right
		elif op.value == '*': 
			output = left * right
		elif op.value == '/': 
			output = left / right
		elif op.value == '>': 
			output = 1 if left > right else 0
		elif op.value == '>=': 
			output = 1 if left >= right else 0
		elif op.value == '<': 
			output = 1 if left < right else 0
		elif op.value == '<=': 
			output = 1 if left <= right else 0
		elif op.value == '?=': 
			output = 1 if left == right else 0
		elif op.value == 'and': 
			output = 1 if left and right else 0
		elif op.value == 'or': 
			output = 1 if left or right else 0

		if left_type == 'INT' and right_type == 'INT':
			return Integer(output) 
		else:
			return Float(output)


	def compute_unary(self, operator, operand):
		operand_type = 'VAR' if str(operand.type).startswith('VAR') else str(operand.type)
		operand = getattr(self, "read_" + operand_type)(operand.value)

		if operator.value == '+':
			return +operand
		elif operator.value == '-':
			return -operand
		elif operator.value == 'not':
			return 1 if not operand else 0


	def interpret(self, tree=None):
		if tree is None: 
			tree = self.tree

		if isinstance(tree, list) and len(tree) == 2:
			expression = tree[1]
			if isinstance(expression, list):
				expression = self.interpret(expression)
			return self.compute_unary(tree[0], expression)

		elif not isinstance(tree, list):
			return tree

		else:
			left_node = tree[0]
			if isinstance(left_node, list):
				left_node = self.interpret(left_node)
			operator = tree[1]
			right_node = tree[2]
			if isinstance(right_node, list):
				right_node = self.interpret(right_node)
			return self.compute_bin(left_node, operator, right_node)