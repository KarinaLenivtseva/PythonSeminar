#Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

s = 'Съешь ещё этих мягабвких французских булок, абв да выпей чаю'
data = ' '.join(list(filter(lambda x: not 'абв' in x, s.split(' '))))
print(data)