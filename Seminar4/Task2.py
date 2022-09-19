#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
def EnterCheckNumber():
    while True:
        try:
            n = int(input())
            break
        except:
            continue
    return n
def Simple(N):
    if N == 1:
        nums = [1]
    if N == 2:
        nums = [1,2]
    if N >= 3:
        nums = [1,2,3]
        for i in range(4,N+1):
            trigger = True
            for j in range(1,i+1):
                if (i % j == 0) and (j<i) and j>1:
                    trigger = False
                    break
            if trigger:
                nums.append(i)
    return nums
print('N = ')
N2 = EnterCheckNumber()
SimpleNums2 = Simple(N2)
SimpleDiv = []
for i in SimpleNums2:
    if (N2 % i == 0):
        SimpleDiv.append(i)
print(f"Простые множители для N = {N2}: {SimpleDiv}")