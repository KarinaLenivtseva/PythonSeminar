# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

while True:
    print("Enter your number: ")
    try:
        N = int(input("Enter number "))
        break
    except:
        continue
F = []
for i in range(1, N+1):
    if i == 1:
        F = [1]
        continue
    F.append(F[i-2]*i)
print(F)