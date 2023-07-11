

class Lexer:                                     # класс лексер
	digits = '0123456789'                          # список всех цифр для чисел
	operations = '+-*/'                            # список всех вариантов операций
	stopwords = [' ']                              # список стоп-слов

	def __init__(self, text):                      # инициализация нового лексера
		self.text = text                             # текст, который прислал пользователь
		self.idx = 0                                 # индекс символа, который рассматриваем
		self.tokens = []                             # список всех найденных токенов в строке
		self.char = self.text[self.idx]              # текущий символ, который анализируем
		self.token = None                            # текущий токен, который собираем

	def tokenize(self):                            # функция tokenize (определение токенов в строке) 
		while self.idx < len(self.text):             # пока индекс текущего символа в пределах строки
			if self.char in Lexer.digits:              # если(1) текущий символ среди списка цифр, то...
				self.token = self.extract_number()       # ...токен = достать числовой токен
			elif self.char in Lexer.operations:        # если(2) текущий символ среди операций, то...
				self.token = Operation(self.char)        # ...токен = операция для текущего символа
				self.move()                              # ...взять новый символ
			elif self.char in Lexer.stopwords:         # если(3) текущий символ среди стоп-слов, то...
				self.move()                              # ...взять новый символ
				continue                                 # ...перейти на следующую итерацию цикла
			self.tokens.append(self.token)             # добавить найденный токен к списку токенов
		return self.tokens                           # вернуть список токенов, полученный из строки

	def extract_number(self):                      # функция extract_number (собрать число)
		number = ''                                  # изначально число = пустая строка
		isFloat = False                              # изначально число не вещественное

		# пока (текущий символ среди `0123456789` или `.`) и (индекс текущего символа в пределах строки)
		while ((self.char in Lexer.digits or self.char == '.') and (self.idx < len(self.text))):
			if self.char == '.':                       # (1)если текущий символ == точке, то...
				isFloat = True                           # ...число будет вещественное
			number = number + self.char                # (2)число = число + текущий символ
			self.move()                                # (3)взять новый символ строки

		#	вернуть из функции токен Integer, если число простое, Float, если число вещественное
		return Integer(number) if not isFloat else Float(number)

	def move(self):                                # функция move (взять новый символ строки)
		self.idx = self.idx + 1                      # увеличить значение в атрибуте `idx` на 1
		if self.idx < len(self.text):                # если значение idx в пределах строки, то...
			self.char = self.text[self.idx]            # ...считать текущий символ в атрибут `char`


class Token:
	def __init__(self, type, value):
		self.type = type
		self.value = value

	def __repr__(self):
		return self.value


class Integer(Token):
	def __init__(self, value):
		super().__init__('INT', value)


class Float(Token):
	def __init__(self, value):
		super().__init__('FLT', value)


class Operation(Token):
	def __init__(self, value):
		super().__init__('OP', value)
