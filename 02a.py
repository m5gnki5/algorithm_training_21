"""
Задача просит ответить, отсортирована ли по возрастанию
последовательность чисел на вводе. Подробнее по ссылке
https://contest.yandex.ru/contest/27472/problems/A/
"""

nums = list(map(int, input().split()))
conds = []

for i in range(1,len(nums)):
    if nums[i-1] < nums[i]:
        conds.append(True)
    else:
        conds.append(False)

print("YES" if all(conds) else "NO")
