"""
Задача просит найти корни уравнения с корнем.
Подробнее по ссылке
https://contest.yandex.ru/contest/27393/problems/D/
"""
a = int(input())
b = int(input())
c = int(input())

if a == 0:
	if b**0.5 == c:
		print("MANY SOLUTIONS")
	else:
		print("NO SOLUTION")
else:
	if c >= 0:
		x = (c**2 - b) / a
		if round(x) == x:
			print(int(x))
		else:
			print("NO SOLUTION")
	else:
		print("NO SOLUTION")
