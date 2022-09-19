# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и 
# записать в файл многочлен степени k.

def EnterCheckNumber():
    while True:
        try:
            n = int(input())
            break
        except:
            continue
    return n

import random

print("k = ")
k4 = EnterCheckNumber()
for i in range(k4, -1, -1):
    file = open('file.txt', 'a', encoding='utf-8')
    if i == k4:
        k = random.randint(1,100)
        file.write(f'{k} * x^{i} ')
    if k4 > i > 1:
        k = random.randint(0, 100)
        if k != 0:
            file.write(f'+ {k} * x^{i} ')
    if i == 1:
        if k != 0:
            file.write(f'+ {k} * x ')
    if i == 0:
        k = random.randint(0, 100)
        if k != 0:
            file.write(f'+ {k} = 0')
        if k == 0:
            file.write(f'= 0')
    file.close()
