# Задайте список из вещественных чисел. 
# Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

import math
list = [4.07, 5.1, 8.2444, 6.98]
list_new = []
for i in list:
    list_new.append(round((i-math.floor(i)), 10))
print(list_new)

print(f'Difference = {round(max(list_new)-min(list_new), 10)}')

listnew = []
for i in list:
    listnew.append(str(i).split(".")[1])
max_len = len(max(listnew, key=len))
for i in range(len(listnew)):
    listnew[i] = int(listnew[i].ljust(max_len, "0"))
dif = int(str(max(listnew)-min(listnew)).rstrip("0"))

print("Dif =", dif)