# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

# Чтобы выиграть первому игроку надо сначала брать 20 конфет, а последующими ходами уравновешивать 2хода=29
# import random, math
# b = abs(int(input('Определение хода первого игрока. Сколько игроков играет?')))
# a = [random.randint(1,2) for _ in range(b-1)]
# print('Первым ходит игрок №' , (a))
# # n=a
# summa=2021
# # def player1():
# print ('1 Ход, ходит игрок №',(a))
# count=1
# while summa>0:
#     if a==2:
#         k=1
#     else:
#         k=2
#     play= int(input('Игрок забирает конфеты в количестве  '))
#     if play<29 or summa<28:
#         summa-=play
#         count+=1
#         # break
#     print((count),'Ход, осталось конфет', (summa))
#     print ('Ходит игрок №',(int(k)))
# print('Победил игрок № ')
# Игра с ботом
import random
vsego = 100
max = 28
count = 0
с = 0
a = vsego % (max+1)
print("Всего конфет ", vsego)
# print(a)
print(f'Бот взял {a} конфет')
vsego = vsego - a
count = count+1
while (vsego > 0):
    # print ('возьмите не более 28 конфет: ')
    print("Осталось", vsego, "кофет")
    b = int(input('возьмите не более 28 конфет: '))
    if (b > 28):
        print("возьмите меньше конфет")
    elif (b == 28):
        # бот должен разбить 28
        vsego = vsego - b
        print("Осталось", vsego, "кофет")
        count += 1
        c = random.randint(1, 28)
        # print (c)
        print(f'Бот взял {c} конфет')
        vsego = vsego - c
        count += 1
    elif (b < 29):
        # бот должен дополнить ход игрока до 28
        vsego = vsego - b
        count += 1
    elif (vsego < 0):
        c = 28 - b
        print(f'Бот взял {c} конфет')
        vsego = vsego - c
        count += 1
print("Всего ходов",count)
if (count % 2 == 0):
    print('выиграл игрок 2')
else:
    print('выиграл игрок 1')
