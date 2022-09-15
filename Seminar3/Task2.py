# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from Task1 import Element
from Task1 import EnterCheckNumber

print("Enter the amout of elements of the list::")
n = EnterCheckNumber()
list = []
Element(list, n)
print(list)
list_new = []
while len(list) != 0:
    if len(list) == 1:
        list_new.append(list[0]**2)
        break
    else:
        a = list.pop(0)
        b = list.pop()
        list_new.append(a*b)
print(list_new)