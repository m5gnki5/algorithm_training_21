"""
Задача просит расчитать подъезд и этаж по номеру
квартиры. Подробнее по ссылке
https://contest.yandex.ru/contest/27393/problems/E/
"""
import math

def apts_per_storey(apt: int, hall: int, storey: int) ->int:
	return math.ceil(apt/storey)

"""
2		1		20	количество этажей 	(M)

3		11		89	номер квартиры 1 	(K¹)
-1		0		2	подъезд 1 			(P¹)
-1		1		3	этаж 1 				(N¹)

2		1		41	номер квартиры 2 	(K²)
2		1		1	подъезд 2 			(P²)
1		1		11	этаж 2 				(N²)
"""

house = list(map(int, input().split()))

if house[1] < house[-1]:
	apt1, n_of_storeys, apt2, hall2, storey2 = house
	if apt1 == apt2:
		print(f"{hall2} {storey2}")
	# elif :





else:
	print("-1 -1")
