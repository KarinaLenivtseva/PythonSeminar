# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

from Task1 import EnterCheckNumber

def EnterCheckNumber():
    while True:
        try:
            n = int(input())
            break
        except:
            continue
    return n

def NegoFib(n):
    ListFib = []
    ListNegoFib = []
    for i in range(0,n):
        if i == 0:
            ListFib.append(0)
        elif 1 <= i <= 2:
            ListFib.append(1)
            if i == 1:
                ListNegoFib.append(1)
            if i == 2:
                ListNegoFib.append(-1)
        else:
            ListFib.append(ListFib[i-2]+ListFib[i-1])
            ListNegoFib.append(((-1)**(i+1))*ListFib[-1])

    res = ListFib.copy()
    while len(ListNegoFib) != 0:
        a = ListNegoFib.pop(0)
        res.insert(0, a)
    return res

print("Введите N:")
n = EnterCheckNumber()
list = NegoFib(n)
print(list)