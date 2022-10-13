# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота

import random
player = input('Введите имя игрока: ')
sweets = 117
queue = random.randint(0,1)
while sweets > 0:
    if queue == 0:
        x = int(input(f'Сколько конфет возьмет {player}: '))
        sweets -=x
        print(f'Осталось {sweets} конфет')
        queue = 1
        print('____Ход переходит к боту____')
    else:
        xb = random.randint(1,28)
        sweets -=xb
        print(f'Бот забрал {xb} конфет')
        print(f'Осталось {sweets} конфет')
        queue = 0
        print('____Ход переходит к человеку____')
if queue == 0:
    print(f'Упс,Бот одержал победу')
else:
   print(f'Поздравляю,{player} одержал победу')




    

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}.Осталось на столе {value} конфет.")


# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Введите количество конфет на столе: "))
# flag = randint(0, 2)  # флаг очередности
# if flag:
#     print(f"Первый ходит {player1}")
# else:
#     print(f"Первый ходит {player2}")

# counter1 = 0
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"Выиграл {player1}")
# else:
#     print(f"Выиграл {player2}")
