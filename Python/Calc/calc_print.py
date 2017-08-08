#-*- coding: utf-8 -*-
def flags():
    print('휴가를 다녀오셨습니까?\nY/N')
    index = raw_input()
    if index == 'n' or index == 'N':
        flag = 1
    else:
        print('몇차 휴가까지 다녀오셨습니까?\n1/2/3')
        index = input()
        if index == 1:
            flag = 2
        elif index == 2:
            flag = 3
        elif index == 3:
            flag = 4
    return flag

