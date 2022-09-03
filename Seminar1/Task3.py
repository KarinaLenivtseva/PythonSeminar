#Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).
print("Задача 3. \nНапишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).", end=" ")

InputCoordinate = int(input ("\n Enter the number of the quarter: "))
if InputCoordinate == 0:
    print("Ноль не подходит. Введите число не равное нулю")
if InputCoordinate == 1:
    print("x > 0 \ny > 0")
if InputCoordinate == 2:
    print("x < 0 \ny > 0")
if InputCoordinate == 3:
    print("x < 0 \ny < 0")
if InputCoordinate == 4:
    print("x > 0 \ny < 0")