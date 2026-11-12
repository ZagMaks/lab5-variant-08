"""
Лабораторна робота: Варіант 8
Студент: Загородній Максим
Група: EIP30
"""
import math
def target_function(x):
    x = (math.sin(x**2)+1)/6
    return x


def solve_iteration(func,a,b,e):
    ans = [a,b]
    q = 0.5
    while abs(ans[-1]-ans[-2]) >= ((1-q)/q) * e:
        ans.append(func(ans[-1]))
    ans = ans[1:]
    return ans[-1], len(ans), ans