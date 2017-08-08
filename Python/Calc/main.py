#-*- coding: utf-8 -*-
from calc import calc
from calc_print import flags
import time
def l_print():
    print('남은 복무일을 입력하세요.')
    try:
        days = input()
    except NameError:
        print('숫자만 입력하세요.')
        return
    except UnboundLocalError:
        print('숫자만 입력하세요.')
        return
    except SyntaxError:
        print('숫자만 입력하세요.')
        return
    d = calc(days,flags())
    print('당신은 남은 총 복무일 %s일, %s시간 중, %s시간을 사회에서 보내게됩니다.\n축하합니다.' %(days, (days*24), d))
    time.sleep(1)

#if __name__=="__main__":
l_print()

