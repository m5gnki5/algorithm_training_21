"""
Задача просит рассчитать параметры прямоугольника (стола) минимальной площади,
на котором уместятся два прямоугольника заданных длины и ширины (два 
ноутбука). Если  вариантов несколько, вывести один. Подробнее по ссылке
https://contest.yandex.ru/contest/27393/problems/F/
"""
def key_with_max_val(d: dict) -> int:
	v = list(d.values())
	k = list(d.keys())
	return k[v.index(max(v))]

def sort2(first: int, second: int) -> tuple:
    if first > second:
        return (first, second)
    return (second, first)

# длина и ширина первого ноутбука, длина и ширина второго
dims = list(map(int, input().split()))

a, b, c, d = dims
a, b = sort2(a, b)
c, d = sort2(c, d)

if a < c and a*b < c*d:
	a, b, c, d = c, d, a, b
if a > c and b > c:
	print(a+d, b)
elif a < c and b < c:
	print(b+d, c)
elif a > c and b < c:
	print(b+d, a)
else:
# остаётся особый случай: когда площадь двух ноутбуков равна площади стола
	friquency = {}
	for dim in set(dims):
		for i in range(len(dims)):
			if dim not in friquency:
				friquency[dim] = 0
			if dim == dims[i]:
				friquency[dim] += 1
	joint_dim = key_with_max_val(friquency)
	print(joint_dim, sum(dims)-joint_dim*2)
