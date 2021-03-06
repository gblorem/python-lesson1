# -*- coding: utf-8 -*-

'''2. Пользователь вводит время в секундах.
Переведите время в часы, минуты и секунды и
выведите в формате чч:мм:сс. Используйте
форматирование строк.'''

while True:

	# Исключения
	# В данном случае мы отлавливаем ValueError и завершаем цикл при неверном вводе
	try:
		seconds = int(input('Введите время в секундах:\n> '))
	except ValueError:
		print('Вы ввели неверный символ\nПерезапустите программу и введите целочисленное число\nЗавершение работы программы...')
		break
	else:
		'''Нашёл интересную функцию divmod(),
		которая выполняет только одно деление
		для получения как частного, так и остатка'''
		minutes, seconds = divmod(seconds, 60)
		hours, minutes = divmod(minutes, 60)

		print('Секунды в формате чч:мм:сс')
		print('{:02d}:{:02d}:{:02d}'.format(hours, minutes, seconds)) # {:02d} означает целое число, слева заполненное нулями до 2 цифр.