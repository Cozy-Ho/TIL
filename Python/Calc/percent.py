#-*- coding: utf-8 -*-
from subprocess import call
class Info:
    def __init__(self, army_type, in_date):
        self.army_type = army_type
        self.in_date = in_date

    def print_info(self):
        print('Army_type: ', self.army_type)
        print('in_date: ', self.in_date)

def set_info():
    army_type = raw_input("육군?의경?해군?공군?공익?: ")
    in_date = raw_input("입대일: ")
    info = Info(army_type, in_date)
    return info

def print_menu():
    print('***************************')
    print('1. 전역일 계산하기')
    print('2. 얼마나 밖에있지?')
    print('3. 종료')
    print('***************************')
    menu = input('메뉴선택: ')
    return int(menu)

def run():
    while 1:
        menu = print_menu()
        if menu == 1:
            info = set_info()
        elif menu == 2:
            call(['python','main.py'])
        elif menu == 3:
            break

if __name__=="__main__":
    run()

