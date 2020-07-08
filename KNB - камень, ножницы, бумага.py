# создать бесконечный цикл игры в Камень-Ножницы-Бумага
# со случайнм выбором К/Н/Б
# вывести общий счёт побед

import random

continue_choice = True

comp_win = 0
player_win = 0

while continue_choice:
    player_input = input('Выберите камень, ножницы или бумагу: [К/Н/Б]  ').lower()

    if player_input not in ['к', 'н', 'б']:
        print('Ошибка ввода')
        continue

    ops = ['к', 'н', 'б']
    comp_random = random.choice(ops)
    if comp_random == ops[0]:
        print(f'Компьютер выбрал Камень')

    elif comp_random == ops[1]:
        print(f'Компьютер выбрал Ножницы')

    elif comp_random == ops[2]:
        print(f'Компьютер выбрал Бумагу')

    win_comb = [('к', 'н'), ('н', 'б'), ('б', 'к')]

    if (player_input, comp_random) in win_comb:
        print('Поздравляем! Победил ИГРОК!')
        player_win += 1

    elif player_input == comp_random:
        print('НИЧЬЯ! Попробуйте еще раз!')

    else:
        print('Победил КОМПЬЮТЕР!')
        comp_win += 1

    total_score = (comp_win, player_win)
    print(f'Счёт {total_score}\n'
          f'Компьютер выиграл {comp_win} раз\n'
          f'Игрок выиграл {player_win} раз\n')