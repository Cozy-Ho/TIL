#-*- coding: utf-8 -*-
from subprocess import call
from datetime import date, datetime, timedelta
class Info:
    def __init__(self, army_type, in_date):
        self.army_type = army_type
        self.in_date = in_date

    def print_info(self):
        print('Army_type: ', self.army_type)
        print('in_date: ', self.in_date)

def set_info():
    army_type = input("1.육군 2.의경 3.해군 4.공군 5.공익 : ")
    date = raw_input("입대일(YYYYMMDD): ")
    date = list(date)
    year = date[:4]
    month = date[4:6]
    day = date[6:]
    d = datetime.datetime(year,month,day)
    in_date = d.days
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

def calc_info(info):
    now_date = datetime.date.today()
    if info.army_type == 1 or info.army_type == 2:
        t_date = now_date - info.in_date
        print('현재 %s%% 복무 하셨습니다.' %(t_date.days/639*100))
    elif info.army_type == 3:
        t_date = now_date - info.in_date
        print('현재 %s%% 복무 하셨습니다.' %(t_date.days/700*100))
    elif info.army_type == 4 or info.army_type == 5:
        t_date =  now_date - info.in_date
        print('현재 %s%% 복무 하셨습니다.' %(t_date.days/731*100))
    else:
        print('Index에 있는 숫자를 입력하세요.')

def run():
    while 1:
        menu = print_menu()
        if menu == 1:
            info = set_info()
            calc_info(info)
        elif menu == 2:
            call(['python','main.py'])
        elif menu == 3:
            break

if __name__=="__main__":
    run()

