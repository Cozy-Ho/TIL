# -*- coding: utf-8 -*-
#! python 3

#가위바위보 게임.
import random

def computer():
    choice = ['가위', '바위', '보']
    com = random.choice(choice)
    return com

def user():
    usr = raw_input('가위 바위 보!: ')
    return usr

def run():
    a = computer()
    b = user()
    if a == b:
        print('비겼습니다!!')
    elif a == '가위':
        if b == '보':
            print('졌습니다ㅠㅠ')
        elif b == '바위':
            print('이겼습니다!')
    elif a == '바위':
        if b == '보':
            print('이겼습니다!')
        elif b == '가위':
            print('졌습니다ㅠㅠ')
    elif a == '보':
        if b == '가위':
            print('이겼습니다!')
        elif b == '바위':
            print('졌습니다ㅠㅠ')

if __name__ == '__main__':
    for i in range(0,10):
        run()

