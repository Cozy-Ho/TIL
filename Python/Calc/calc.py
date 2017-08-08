#-*- coding: utf-8 -*-
def calc(days,flag):
    '''
    s = 총 복무일
    a = 외출 시간
    b = 외박 시간
    c = 휴가 시간
    d = 총 영외활동 시간
    '''
    s = days*24
    a = int(days/7)*11
    b = int(days/61)*81
    if flag == 1:
        c = 277*2 + 179
    elif flag == 2:
        c = 277 + 179
    elif flag == 3:
        c = 179
    else:
        c = 0
    d = a+b+c
    return d

