"""
Задача просит подтвердить, возможно ли построить треугольник со сторонами,
равными значениям на вводе. Подробнее по ссылке
https://contest.yandex.ru/contest/27393/problems/B/
"""
# ввод — три натуральных числа
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
