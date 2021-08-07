"""
Задача просит сравнить телефонный номер из первого ввода с тремя следующими
с учётом префиксов и доп.символов. Подробнее по ссылке
https://contest.yandex.ru/contest/27393/problems/C/
"""
# ввод — три телефонных номера
num_in_question = input()
first = input()
second = input()
third = input()

sym_list = ["+", "-", "(", ")"]

# цикл приводит номера к единому формату
if all([num_in_question, first, second, third]):
	nums = []
	for num in num_in_question, first, second, third:
		clean_num = []
		for sym in num:
			if sym not in sym_list:
				clean_num.append(sym)
		if len(clean_num) == 11 and (clean_num[0]=="7" or clean_num[0]=="8"):
			clean_num.pop(0)
		elif len(clean_num) == 7:
			clean_num.insert(0, "495")
		clean_num = "".join(clean_num)
		nums.append(clean_num)

# цикл сверяет первый чистый номер с остальными
for i in nums[1:]:
	if i == nums[0]:
		print("YES")
	else:
		print("NO")
