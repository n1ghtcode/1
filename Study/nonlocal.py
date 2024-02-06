#Когда определяешь функцию внутри функции, чтобы пользоваться переменной из основной функции используется nonlocal
import time

def func():
	x = 0
	print('func: x = ', x)

	def func_1():
		nonlocal x
		print('x in func_1 = ', x)
		x = 1
	func_1()
	print('change?: ', x)
	return x #функция возвращает значение х

q = func()
print(q)
time.sleep(3)
