#! -*- coding: utf-8 -*-
import requests

# requests.get 을 통해 웹 페이지에있는 텍스트를 다운로드 한다.
res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')

# res.raise_for_status()함수는 다운로드시 오류가일어나면 예외를 뱉는다.
# requests.get() 함수를 호출할때는 항상 raise_for_status()함수를 함께 호출하자.
try:
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' %(exc))

# 웹 페이지에서 읽어들인 파일을 이진파일로 저장하여(유니코드 인코딩을 유지하기위해) 활용성을 높인다.
playFile = open('RomeoAndJuliet.txt', 'wb')
for chunk in res.iter_content(10000):
    playFile.write(chunk)
playFile.close()

