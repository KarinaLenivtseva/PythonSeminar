# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

range = input("Enter your number: ")
sum = 0
range1 = None
for i in range:
    try:
        range1 = int(i)
    except:
        continue
    sum = sum + range1
print("Sum =", sum)