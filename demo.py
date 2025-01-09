class persian_hex:
	def __init__(self, number: int):
		self.number = number
		# جایگزین پیشوند شانزدهی در فارسی
		self.x_equivalent = 'ش'

		# جایگزین واج‌های شانزدهی
		self.aliases = {10: 'پ',
11: 'چ',
12: 'ژ',
13: 'ف',
14: 'گ',
15: 'ل'}


	def show(self, number = None, is_first = True):
		'''شماره دریافتی را به پایه شانزده نشان بده'''
		if not number:
			number = self.number
		if is_first:
			print(0)
			print(self.x_equivalent)
		for i in divmod(number, 16):
			if i > 15:
				return self.show(i, False)
			elif i in self.aliases:
				print(self.aliases[i])
			else:
				print(i)


# متن نمایشی هنگام دریافت ورودی
prompt = 'شماره وارد کنید: '
persian_hex(int(input(prompt))).show()
