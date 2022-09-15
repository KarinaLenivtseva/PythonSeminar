# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.


from Task1 import Element
from Task1 import EnterCheckNumber

print("Enter the amout of elements of the list::")
n2 = EnterCheckNumber()
list2 = []
Element(list2, n2)
print(list2)
list2_new = []
while len(list2) != 0:
    if len(list2) == 1:
        list2_new.append(list2[0]**2)
        break
    else:
        a2 = list2.pop(0)
        b2 = list2.pop()
        list2_new.append(a2*b2)
print(list2_new)