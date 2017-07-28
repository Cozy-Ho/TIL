CodeWars_7
==========
# Question
Write simple .camelcase method (`camel_case` function in PHP) for strings.  
All words must have their first letter capitalized without spaces.  

For instance:  
```
camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
```
>PHP의 `camel_case`함수처럼 단어의 첫 글자를 대문자로 변환하라는 문제이다.

# My Solution
```
def camel_case(string):
  a = list(string)
  for i in range(0,len(a)):
    if i==0 or a[i-1]==' ':
      a[i] = a[i].upper()
  return ''.join(a).replace(' ','')
```
입력받은 문자열을 리스트로만들고 첫 글자와 이전 인덱스가 공백문자이면 대문자로 바꾸는방법을 사용했다.  

# anter69's Solution
```
def camel_case(string):
  return string.title().replace(" ","")
```
흠.. title()함수를 처음봤다..  
근데 이렇게하면 Pass는 하지만 예외가 있다!!  
예를들어 입력값이 `string = "camel's case' word"` 이면 위 함수로는 `Camel'SCase'Word'`가 된다!
