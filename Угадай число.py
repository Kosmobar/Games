# создать бесконечный цикл игры на угадывание слуайного числа
# в диапазоне от 1 до 50 с возможностью использования 6 попыток
# вывести общий счёт побед

import random

player_win = 0
comp_win = 0
try_num = 0

while True:
    random_x = random.randint(1, 50)

    if try_num < 6:
        while try_num < 6:
            player_num = int(input(f'Введите число от 1 до 50:  '))
            try_num += 1

            if player_num < random_x:
                print(f'Число {player_num} меньше, чем Х')

            if player_num > random_x:
                print(f'Число {player_num} больше, чем Х')

            if player_num == random_x:
                print(f'Поздравляем!!! {player_num} - это то самое число!\n')
                player_win += 1
                break

            if player_num != random_x and try_num == 6:
                print(f'Число {random_x} не угадано! Попробуй еще!\n')
                comp_win += 1

        print(f'Общий счёт: {comp_win, player_win}\n'
              f'Компьютер выиграл {comp_win} раз.\n'
              f'Игрок выиграл {player_win} раз.\n')
    else:
        try_num = 0
        continue