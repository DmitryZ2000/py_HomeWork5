# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

from random import randint

candies = 2021
first_step = randint(1, 28)
print('Первый шаг',first_step)
candies -= first_step
print('Осталось конфет',candies)
second_step = candies % 29 
print('Второй шаг', second_step)
candies -= second_step
print('Осталось конфет', candies)
while candies > 0:
    candies -= randint(1, 28)
    print('Берет противник', )
    candies -= candies % 29
    print('Беру я', )

print('Осталось конфет', candies)
print('Я победил !!!!!!!!!!!!!!')