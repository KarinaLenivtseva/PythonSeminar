# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на позициях a и b.

N = int(input("Enter N "))
NN = list()
for i in range(-N,N+1):
    NN.append(i)
print(NN)

a = int(input("Enter first sum element: "))
b = int(input("Enter second sum element: "))
indexes = [a, b]
for i in range(len(indexes)):
    indexes[i] = int(indexes[i])
indexes.sort()
res = 1
for i in indexes:
    try:
        res = res * NN[i]
        print(f'res = {res} * {NN[i]}, where i = {i}')
    except:
        print(f'i = {i}, not found')
        continue
print("Result is ", res)