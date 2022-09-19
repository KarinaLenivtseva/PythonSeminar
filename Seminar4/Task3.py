# Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from Task2 import EnterCheckNumber
import random
print('Ввведите число элементов последовательности: ')
N = EnterCheckNumber()
nums = []
for i in range(0,N):
    nums.append(random.randint(1,4))
print("List: ", nums)
nums_new = []
for i in nums:
    if i not in nums_new:
        nums_new.append(i)
print("Result: ", nums_new)