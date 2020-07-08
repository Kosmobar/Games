#p1 и p2 участвуют в дуэли, написать функцию "кто быстрее выстрелил"
# вывести победителя p1 / p2 или ничью
# whos_first(
#   "    Bang  "
#   "      Bang"
# ) >>> p1


def whos_first(p1, p2):
    '''DOCSTRING: Function finds winner by first shoot: index position "B" in string
    INPUT: any space + Bang
    OUTPUT: print winner '''

    diff = p1.find('B') - p2.find('B')
    if diff < 0:
        return 'p1'
    elif diff > 0:
        return 'p2'
    else:
        return 'НИЧЬЯ'

print(whos_first('  Bang    ', '   Bang   '))
print(whos_first('      Bang', '  Bang    '))
print(whos_first('  Bang', '  Bang    '))

help(whos_first)
