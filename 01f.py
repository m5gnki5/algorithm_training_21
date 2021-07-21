"""
Задача просит рассчитать параметры прямоугольника (стола) минимальной площади,
на котором уместятся два прямоугольника заданных длины и ширины (два 
ноутбука). Если  вариантов несколько, вывести один. Подробнее по ссылке
https://contest.yandex.ru/contest/27393/problems/F/
"""

# длина и ширина первого ноутбука, длина и ширина второго
dims = list(map(int, input().split()))

laptop_1 = dims[0] * dims[1]	
laptop_2 = dims[2] * dims[3]

# определяю, есть ли общая сторона для "сшивания",
# (т.е. ноутбуки займут весь прямоугольник)
common_sides = []
for dim in dims:
	if (laptop_1 + laptop_2) % dim == 0:
		common_sides.append(dim)

print(common_sides)

# если есть общая сторона, вывести размеры стола 
if common_sides:
	common_sides = list(set(common_sides))
	common_sides[0] *= 2
	print(*common_sides)
# else:
