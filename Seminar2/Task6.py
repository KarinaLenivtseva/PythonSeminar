# Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другой.

sentence = str(input('Введите строку: '))
ind = 1
count = 0
sentence_2 = str(input('Введите вторую строку: '))
while ind != -1:
    ind = sentence.find(sentence_2)
    if ind >= 0:
        count += 1
    sentence = sentence[ind+1:]
print (count)