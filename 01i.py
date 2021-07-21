"""
Задача просит решить, пройдет ли кирпич (дан в трёх 
измерениях) в проём стены (дан в двух измерениях) 
любым из способов. Подрорбнее по сссылке 
https://contest.yandex.ru/contest/27393/problems/I/
"""
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

def sort_nums(first, second):
    if first < second:
        return (first, second)
    return (second, first)

if all([a, b, c, d, e]):
    a, b = sort_nums(a, b)
    b, c = sort_nums(b, c)
    a, b = sort_nums(a, b)
    d, e = sort_nums(d, e)

    if (a <= d) & (b <= e):
        print("YES")
    else:
        print("NO")
else:
    print("NO")
