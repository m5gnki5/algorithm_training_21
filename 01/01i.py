"""
Задача просит решить, пройдет ли кирпич (дан в трёх измерениях) в проём стены
(дан в двух измерениях) любым из способов. Подрорбнее по ссылке 
https://contest.yandex.ru/contest/27393/problems/I/
"""
# измерения керпича
a = int(input())
b = int(input())
c = int(input())

# измерения отверстия
d = int(input())
e = int(input())

def sort2(first: int, second: int) -> tuple:
    if first < second:
        return (first, second)
    return (second, first)

if all([a, b, c, d, e]):
# пузырьковый метод сортировки измерений кирпича
# даже не буду притворяться, что узнал сам, спасибо Густокашину за разбор
    a, b = sort2(a, b)
    b, c = sort2(b, c)
    a, b = sort2(a, b)
# сортировка измерений отверстия
    d, e = sort2(d, e)

    if (a <= d) & (b <= e):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
