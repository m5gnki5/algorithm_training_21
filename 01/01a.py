"""
Задача просит написать кондиционер с двумя параметрами:
1) температура — текущая и желаемая
2) режим работы из четырёх доступных.
Подробнее по ссылке https://contest.yandex.ru/contest/27393/problems/A/
"""
# ввод-1 — два числа: текущая температура, желаемая температура  
temp = list(map(int, input().split()))
assert len(temp) == 2, "Input must consist of two numbers"
a, b = temp

# ввод-2 — команда из указанных в списке `conds`
conds = ["freeze", "heat", "auto", "fan"]
cond = input()
assert cond in conds, "Unknown command, try again"


if cond != "fan":
    if cond != "auto":
        if a == b:
            print(a)
        elif a < b:
            if cond == "freeze":
                print(a)
            else:
                print(b)
        elif a > b:
            if cond == "heat":
                print(a)
            else:
                print(b)
    else:
        print(b)
else:
    print(a)
