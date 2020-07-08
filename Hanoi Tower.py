# 3 колышка с дисками разного диаметра на самом левом колышке, лежащими друг на друге строго по уменьшению диаметра
# необходимо переложить все диски на самый правый колышек, солюдая основное правило:
# нельзя класть диск большего диаметра на меньший диаметр
# написать функцию подсчёта количества ходов

def step_hanoi_tower(discs):
    """DOCSTRING: Function finds number of steps to remove all disks by counting steps with "2**n - 1" (n - number of steps)
    INPUT:
    OUTPUT: """
    return 2**discs - 1

print(step_hanoi_tower(0))
print(step_hanoi_tower(3))
print(step_hanoi_tower(5))
print(step_hanoi_tower(10))
print(step_hanoi_tower(20))
print(step_hanoi_tower(64))