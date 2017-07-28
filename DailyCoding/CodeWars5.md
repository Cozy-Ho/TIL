CodeWars_5
==========
# Question

Write a function that takes in a string of one or more words, and returns the same string,  
but with all five or more letter words reversed (Just like the name of this Kata).  
Strings passed in will consist of only letters and spaces.  
Spaces will be included only when more than one word is present.  

Examples:  
```
spinWords( "Hey fellow warriors" ) # returns "Hey wollef sroirraw"
spinWords( "This is a test" ) # returns "This is a test"
spinWords( "This is another test" ) # returns "This is rehtona test"
```
>문자열이 주어지면 공백을 기준으로 한 단어가 5글자 이상이면 뒤집어서 출력하는 문제이다.

## My Solution
```
def spin_words(sentence):
  a = sentence.split()
  for li in range(0,len(a)):
    if len(a[li]) > 4:
      a[li] = a[li][::-1]
  return ' '.join(a)
```

문자열을 공백을 기준으로 나누고 나눈 문자열의 길이를 체크하여 5글자 이상이면 문자열포멧 `[::]`을 이용해서 reverse시킨다.  
그 후 join을 이용해 다시 합쳐준다.  

## MiraliN's Solution
```
def spin_words(sentence):
  return ' '.join([x[::-1] if len(x) >=5 else x for x in sentence.split(" ")])
```
...후.. 이 방법으로 풀어보려고 몇번 시도해봤지만 실패했었는데 이렇게 푼 사람을보니 반가웠다.
~~조금더 열심히!!~~
