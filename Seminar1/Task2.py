#Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 
# и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
print("Задача 2. \nНапишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится", end=" ")

FirstPoint = int(input("\nEnter coordinates x: "))
SecondPoint = int(input("Enter coordinates y: "))
if FirstPoint == 0 or SecondPoint == 0:
    print("Ноль не подходит. Введите число не равное нулю")
if FirstPoint > 0 and SecondPoint > 0:
    print("Точки принадлежат первой четверти")
if FirstPoint < 0 and SecondPoint > 0:
    print("Точки принадлежат второй четверти")
if FirstPoint < 0 and SecondPoint < 0:
    print("Точки принадлежат третьей четверти")
if FirstPoint > 0 and SecondPoint < 0:
    print("Точки принадлежат четвертой четверти")