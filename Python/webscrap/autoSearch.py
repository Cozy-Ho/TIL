# -*- coding: utf-8 -*-
#! python3

# 명령행 단위에서 키워드를 입력시 자동으로 구글검색창에 검색후 결과를 출력하는 프로그램.

import requests, sys, webbrowser, bs4

puts = raw_input("검색어: ")

print('Googling...')

res = requests.get('http://google.com/search?q=' + puts)
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem : %s' %(exc))

soup = bs4.BeautifulSoup(res.text)

# select('.r a')는 r 클래스의 모든 a 엘리먼트를 선택하라는 선택자 이다.
linkElems = soup.select('.r a')

# 검색한 결과중 최소 5개를 브라우저의 탭으로 띄우라는 명령.
numOpen = min(5, len(linkElems))

for i in range(numOpen):
    webbrowser.open('http://google.com' + linkElems[i].get('href'))

