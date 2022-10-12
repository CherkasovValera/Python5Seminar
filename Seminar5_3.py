# Создайте программу для игры в ""Крестики-нолики"".

def gamer1():#ходит ноликами
    str1 = '_|_|_'
    str2 = '_|_|_'
    str3 = ' | | '
    print(str1, str2, str3, sep='\n')
    a= int(input('Ходит игрок №1, введите номер строки от 1 до 3: '))
    i = int(input('Введите номер столбца от 1 до 3: '))
    if a == 1:
        for b in range(0,b):
            str1=list.replace(i*2,"0")
            if a == 2:
                for b in range(0,b):
                    str2=list.replace(i*2,"0")
                    if a == 3:
                        for b in range(0,b):
                            str3=list.replace(i*2,"0")
    print(str1, str2, str3, sep='\n')
print (gamer1())
