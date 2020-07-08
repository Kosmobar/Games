# 3 броска двух кубиков, после каждого броска сумма выпавших прибавляется к общей сумме
# при выпадении дуплета (одинаковый результат обоих кубиков в 1 броске) очки обнуляются и следущие броски не считаются
# написать функцию для 3 кортежей по два элемента в каждом

def calc_dice_scores(result_list):
    """DOCSTRING: Function sums 3 steps with 2 results in each
    INPUT: 2 results in 3 steps
    OUTPUT: total sum"""

    return sum(a + b for a, b in result_list) if not any(a == b for a, b in result_list) else 0

print(calc_dice_scores([(3,5), (6,2), (1,3)]))
print(calc_dice_scores([(3,3), (6,2), (1,3)]))
print(calc_dice_scores([(3,5), (6,2), (1,1)]))



# создать двумерный массив 3х3 (9 элементов), заполненные числами от 1 до 9
# функция должна возвращать False, если все числа встречаются только 1 раз, иначе True

def any_duplicates(result):
    """DOCSTRING: Function compares numbers in lists, if list has equal number = False, otherwise = True
        INPUT: 3 numbers in 3 lists
        OUTPUT: True / False"""
    result_x = [i for x in result for i in x]
    return any(result_x.count(i) != 1 for i in result_x)

print(any_duplicates([[1,2,3],[4,5,6],[7,8,9]]))
print(any_duplicates([[1,2,5],[4,5,6],[7,8,9]]))
print(any_duplicates([[1,2,3],[4,5,6],[7,7,9]]))
