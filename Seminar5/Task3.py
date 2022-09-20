# Создайте программу для игры в ""Крестики-нолики"".

table_example = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
table = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def print_table(t:list):
    print(t[0] + ' | ' + t[1] + ' | ' + t[2])
    print('----------')
    print(t[3] + ' | ' + t[4] + ' | ' + t[5])
    print('----------')
    print(t[6] + ' | ' + t[7] + ' | ' + t[8])

def check_game(sum, t:list):
    if sum == t[0] and sum == t[1] and sum == t[2]:
        return 1
    elif sum == t[3] and sum == t[4] and sum == t[5]:
        return 1
    elif sum == t[6] and sum == t[7] and sum == t[8]:
        return 1
    elif sum == t[0] and sum == t[3] and sum == t[6]:
        return 1
    elif sum == t[1] and sum == t[4] and sum == t[7]:
        return 1
    elif sum == t[2] and sum == t[5] and sum == t[8]:
        return 1
    elif sum == t[0] and sum == t[4] and sum == t[8]:
        return 1
    elif sum == t[2] and sum == t[4] and sum == t[6]:
        return 1
    elif t[0] != ' ' and t[1] != ' ' and t[2] != ' ' and t[3] != ' ' and t[4] != ' ' and t[5] != ' ' and t[6] != ' ' and t[7] != ' ' and t[8] != ' ' :
        return 2
    else:
        return 0

def check_index():
    while True:
        try:
            n = int(input())
            if (1 <= n <= 9):
                break
        except:
            print('Ввведите корректные данные!')
    return n

print('При вводе данных, куда будет ставиться значки, запомните индексы игры: ')
print_table(table_example)
print()
print("Игрок 1 ходит первым и играет - 'x' ")
print("Игрок 2 ходит вторым и играет - '+' ")
print()
while True:
    print_table(table)
    print('Игрок 1, введи индекс куда поставить - "x" ')
    while True:
        c1 = check_index() - 1
        if table[c1] == ' ' :
            table[c1] = 'x'
            break
        else:
            print('Введите индекс по адресу которого нет символа!')
    print_table(table)
    v = check_game('x', table)
    if v == 1:
        print('Игрок 1 выиграл!')
        break
    if v == 2:
        print('Ничья!')
        break
    print('Игрок 2, введи индекс куда поставить - "0" ')
    while True:
        c2 = check_index() - 1
        if table[c2] == ' ':
            table[c2] = '0'
            break
        else:
            print('Введите индекс по адресу которого нет символа!')
    print_table(table)
    v = check_game('0', table)
    if v == 1:
        print('Игрок 2 выиграл!')
        break
    if v == 2:
        print('Ничья!')
        break