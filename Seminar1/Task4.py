#Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
##Функции

#def f(x):
#    if x ==1:
#        return 'Целое'
#    elif x == 2.3:
#        return 23
#    else:
#        return
    
#arg = 2
#print(f(arg))
#print(type(f(arg)))

import math
x1 = float(input('Введите координаты X1. \n x1 = '))
x2 = float(input('Введите координаты X2. \n x1 = '))
y1 = float(input('Введите координаты Y1. \n y1 = '))
y2 = float(input('Введите координаты Y2. \n y2 = '))
distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
print(distance)