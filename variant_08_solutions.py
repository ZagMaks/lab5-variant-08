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

def save_results_to_file():
    with open("results_variant_08.txt", "w", encoding="utf-8") as file:
        file.write(f"Корінь: {str(x)}\n")
        file.write("Результати обчислень:\n")
        for i in range(len(s)):
            file.write(f"{str(i+1):<10}{s[i]:.6f}\n")

if __name__=="__main__":
    a,b = -1,1
    e = 0.0005
    x,i,s = solve_iteration(lambda r: (math.sin(r**2)+1)/6,a,b,e)    
    print("корінь рівняння:", x)
    print("кількість ітерацій:", i)
    print("список-протокол обчислень:", s)
    save_results_to_file()