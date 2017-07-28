CodeWars_4
===========
# Question
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.  
```
move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
```

>입력받은 문자열을 가공하는 문제이다.  
>'0'은 오른쪽으로 정렬해서 return하면 된다.

## My Solution
```
def move_zeros(array):
    a=[]
    b=[]
    for li in list(array):
        if li == 0:
            if str(li) == str(False):
                a.append(li)
            else:
                b.append(li)
        else:
            a.append(li)
    return a+b
```

## riytakayal's Solution
```
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
```
와..! 감탄이 절로나오는 코드다!  
return을 세련되게 했다. 나처럼 리스트를 여러개만들 필요도 없었다. ㅠㅠ  
