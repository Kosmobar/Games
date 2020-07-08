# Игра Баше - разновидность игры Ним
# 2 игрока из кучки, содержащей N предметов, по очереди берут не менее 1 и не более М предметов.
# Проигравшим считается тот, кому нечего брать, то есть не может сделать ход.

print('Добро пожаловать в игру Баше!\n\n'
      'Правила игры:\n'
      '- 2 игрока по очереди берут из кучки не менее 1 и не более установленного количества предметов;\n'
      '- количество предметов в кучке ограничено;\n'
      '- проигравшим считается тот, кому нечего брать.\n\n')
while True:
    player_1 = input('Введите имя игрока, который будет ходить первым:  ')
    player_2 = input('Введите имя второго игрока:  ')
    max_n = int(input('Укажите итоговое количество предметов в игре:  '))
    max_x = int(input('Сколько предметов можно взять за 1 ход:  '))
    while max_n > 0:
            step_1 = int(input(f'{player_1}, сделайте ход: '))
            if step_1 > max_x or step_1 < 1:
                print(f'{player_1}, нелья брать меньше 1 и больше {max_x} предметов!')
                continue
            else:
                max_n -= step_1
                print(f'Осталось {max_n} предметов\n')
                if max_n <= 0:
                    print(f'{player_1} победил!\n')
                    break
                else:
                    step_2 = int(input(f'{player_2}, сделайте ход: '))
                    if step_2 > max_x or step_2 < 1:
                        print(f'{player_2}, нелья брать меньше 1 и больше {max_x} предметов!')
                        continue
                    else:
                        max_n -= step_2
                        print(f'Осталось {max_n} предметов\n')
                        if max_n <= 0:
                            print(f'{player_2} победил!\n')
                            break
                        else:
                            continue
    while True:
        continue_ask = input('Новая партия? [ Y / N ]  \n').lower()
        if continue_ask == ('y'):
            break
        elif continue_ask == ('n'):
            continue
        else:
            continue