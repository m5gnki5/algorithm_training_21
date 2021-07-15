"""
Задача просит подтвердить, возможно ли построить
треугольник со сторонами, равными значениям на вводе.
Я не знал правила суммы сторон, пока не погуглил :(
Подробнее по ссылке
https://contest.yandex.ru/contest/27393/problems/B/
"""

a = int(input())
b = int(input())
c = int(input())
sides = [a, b, c]

if len([s for s in sides if s >= 0]) == 3:
	if all(sides):
		if (a + b > c) & (c + a > b) & (b + c > a):
			print("YES")
		else:
			print("NO")
	else:
		print("NO")
else:
	print("NO")
