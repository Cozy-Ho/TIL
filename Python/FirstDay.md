1장 파이썬 시작하기
===================
## 파이썬의 특징

1. 파이썬은 인간다운 언어이다.
- 다른 언어보다 직관적이다.
- 언어 구조가 간결하하여 공동 작업과 유지 보수가 아주 쉽고 편하다.
2. 개발 속도가 빠르다.
- **"Life is too short, You need Python."**

## 파이썬으로 할 수 있는 일

1. 시스템 유틸리티 제작
2. 웹 프로그래밍
3. 데이터베이스 프로그래밍
4. 데이터 분석, 사물 인터넷


2장 파이썬 프로그래밍의 기초, 자료형
====================================

# 숫자형

> 정수
  123, -345, 0

> 실수
  123.34, -1234.5, 3.4e10

> 복소수
  1+2j, -3j

> 8진수
  0o34, 0o25

> 16진수
  0x2A, 0xFF

- 제곱을 할때는 \**를 사용한다.
```{.Python}
    a = 2  
    b = 3  
    a**b = 8  
```
- 나머지를 반환하는 % 연산자.
`7 % 3 == 1`

- 나눗셈 후 소수점 아랫자리를 버리는 // 연산자.
`7 // 4 == 1`

# 문자열 자료형

- 문자열을 만들때는 아래 방법으로 만든다.

1. "Hello World"
2. 'Python is fun'
3. '''Life is too short, You need Python'''
4. """Hello World"""

- 문자열에 홑따옴표, 곁따옴표를 포함시키려면 \\(이스케이프 문자)를 사용한다.

- 문자열 가공하기
1. 문자열 인덱싱 -- a[0], a[1], a[-3]=뒤에서 3번쨰  ...
2. 문자열 슬라이싱  -- a[0:4] -> a 문자열 4번째 글자까지 자르기
3. 문자열 포매팅 -- "Hello %d World %s." %(10, Cozy-Ho) -> %d=정수, %s=문자열

## 문자열 관련 함수들

- count (문자 개수 세기)
- find, index (위치 알려주기)
- join (문자열 삽입)
- upper, lower (소문자,대문자로 변환)
- lstrip, rstrip (왼쪽, 오른쪽 공백 지우기)
- split (기준값으로 문자열 나누기)

# 리스트 자료형

- 리스트에 리스트가 포함될 수 있다.
```{.Python}
    a = [1, 2, 3, ['a', 'b', 'c']]  
    a[-1][0] == 'a'  
    a[-1][1] == 'b'  
    a[-1][2] == 'c'  
```
- 인덱싱과 슬라이싱은 문자열과 동일하다.
## 리스트 관련 함수들

- append (리스트에 요소 추가)
- sort (리스트 정렬)
- reverse (리스트 뒤집기)
- remove (리스트 요소 제거)
- pop (리스트 요소 끄집어내기)
- count (리스트에 포함된 요소의 개수 세기)

# 튜플 자료형

**리스트와 다르게 튜플의 항목값은 변화가 불가능하다.**
그 외에 인덱싱, 슬라이싱, 더하기, 곱하기(반복)등은 리스트와  동일하다.

# 딕셔너리 자료형

딕셔너리 자료형은 대응관계를 나타내는 '연관 배열' 이다.  
기본적인 딕셔너리의 모습은 다음과  같다.  
`{Key1:Value1, Key2:Value2, Key3:Value3 ...}`  
딕셔너리의 쌍을 추가할때는 다음과 같이 하면된다.  
```{.Python}
    a = {1:'a'}  
    a[2] = 'b'  
    a => {2: 'b', 1: 'a'}  
```
딕셔너리는  Key값을 입력하면 Value를 반환한다.  
**중복되는 Key값은 사용하면 안된다. 또 Key값에는 리스트를 쓸 수 없지만, 튜플은 가능하다.**

## 딕셔너리 관련 함수들

- keys (key 값들로 리스트 만들기)
- values (value 값들로 리스트 만들기)
- items (key, value쌍 얻기)
- clear (key, value쌍 모두 지우기)

# 집합 자료형
집합자료형은
1. 중복을 허용하지 않는다.
2. 순서가 없다.
예시를 보면  
```{.Python}
    s1 = set("Hello")  
    s1 => {'e', 'l', 'o', 'H'}  
```
set자료형은 순서가 없기때문에 인덱싱으로 값을 얻을 수 없다.

## 집합자료형 활용하기
- s1 & s2 (교집합 구하기)
- s1 | s2 (합집합 구하기)
- s1 - s2 (차집합 구하기)

## 집합 자료형 관련 함수들
- add (값 1개 추가하기)
- update (값 여러개 추가하기)
- remove (특정 값 제거하기)

# 자료형의 참과 거짓
자료형에도 참과 거짓이 있다.  
각각의 자료형 문자열, 리스트, 튜플, 딕셔너리, 숫자 등에 값이 비어있으면 거짓이된다.

# 자료형의 값을 저장하는 공간, 변수
파이썬에서는 C나 JAVA처럼 변수의 자료형을 함께 쓸 필요는 없다.~~(오 겁나좋군)~~  
두 변수의 값을 바꾸는 방법도 아주 간단하다.  
```{.Python}
    a=3  
    b=5  
    a, b = b, a  
    a==5  
    b==3  
```
정말 쉽다.
