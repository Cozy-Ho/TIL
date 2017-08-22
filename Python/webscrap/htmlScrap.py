# -*- coding: utf-8 -*-
import bs4
exampleFile = open('example.html')
exampleSoup = bs4.BeautifulSoup(exampleFile.read())

# 예제 HTML example.html에서 id=author인 모든 엘리먼트의 리스트를 받는다.
elems = exampleSoup.select('#author')

# 받은 리스트에 객체수를 출력한다.
print(len(elems))

# getText()함수는 엘리먼트의 텍스트 또는 내부 HTML을 돌려준다.
print(elems[0].getText())

# 엘리먼트를 str()함수로 전달하면 시작및 닫는테그, 그리고 엘리먼트의 텍스트로 이루어진 문자열을 돌려받는다.
print(str(elems[0]))

# attrs는 요소의 속성인 'id'를 키로, 속성값인 'author'를 값으로 한 사전이다.
print(elems[0].attrs)

pElems = exampleSoup.select('p')

print(str(pElems[0]))
print(pElems[0].getText())
print(str(pElems[1]))
print(pElems[1].getText())
