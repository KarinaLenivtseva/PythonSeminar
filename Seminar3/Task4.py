# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

while True:
    print("Enter a number u need to convert to a binary. To exit the program, enter any other than a set number")
    n = input("N = ")
    try:
        n = int(n)
    except:
        print("The cycle is finished")
        break
    nbinary = bin(n)
    print(f'Number: {n}, binary value: {nbinary}')