CodeWars_3
==========
# Question
Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible, containing distinct letters,  

each taken only once - coming from s1 or s2. #Examples:  
```
a = "xyaabbbccccdefww" b = "xxxxyyyyabklmopq" longest(a, b) -> "abcdefklmopqwxy"
a = "abcdefghijklmnopqrstuvwxyz" longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
```

>최대 2개의 문자열을 주면 문자열두개를 합쳐서 중복을 제거한 후,  
>알파벳 순서로 리턴하라는 문제이다.

## My Solution
```{.Python}
def longest(s1, s2):
	a = set(s1+s2)
	b = list(a)
	b.sort()
	return ''.join(b)
```

>집합 자료형 `set()`을 이용하면 중복을 쉽게 제거할수 있다는 것을 이용하였다.  
>중복을 제거한 후 리스트로 만들어 정렬, `join()`함수를 통해 문자열로 만들었다.  

## biskinis's Solution
```
def longest(s1, s2):
	return ''.join(sorted(set(s1) | set(s2)))
```

이걸 한줄에 다 표현할수 있구나..  
내코드 다이어트좀 해야겠다.  

