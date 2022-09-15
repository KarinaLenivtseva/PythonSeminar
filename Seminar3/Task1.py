# Задайте список из нескольких чисел. 
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

import random
import math

def EnterCheckNumber():
    while True:
        try:
            n = int(input())
            break
        except:
            continue
    return n

def Element(some_list, n):
    for i in range(n):
        some_list.append(random.randint(0,30))

print("Enter the amout of elements of the list:")
n1 = EnterCheckNumber()
list1 = []
Element(list1, n1)
print(list1)
Sum = 0
for i in range(len(list1)):
    if i%2 != 0:
        Sum += list1[i]
print('Sum is', Sum)