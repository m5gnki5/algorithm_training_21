"""
Задача просит определить тип последовательности чисел 
на вводе из представленных шести. Подробнее по ссылке
https://contest.yandex.ru/contest/27472/problems/B/
"""

nums = []
while True:
	num = float(input())
	if num == -2*10e9:
	    break
	else:
		nums.append(num)

conds = []
for i in range(1,len(nums)):
    if nums[i-1] < nums[i]:
        conds.append(2)
    elif nums[i-1] == nums[i]:
    	conds.append(1)
    else:
        conds.append(0)





if sum(conds)==len(conds)*2:
	print("ASCENDING")
elif sum(conds)==len(conds):
	print("CONSTANT")
elif len(conds)< sum(conds) < len(conds)*2:
	print("WEAKLY ASCENDING")







# print("DESCENDING") # последовательность является строго убывающей
# print("WEAKLY DESCENDING") # последовательность является нестрого убывающей
# print("RANDOM") # последовательность не принадлежит ни к одному из вышеупомянутых типов
