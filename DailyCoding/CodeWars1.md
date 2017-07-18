CodeWars_1
===========
# Question
Given the triangle of consecutive odd numbers:
```
              1
            3   5
          7   9  11
        13  15 17  19
      21  23  25 27  29
    ...
```
Calculate the row sums of this triangle from the row index(starting at index 1) e.g.:
```
row_sum_odd_numbers(1); # 1
ruw_sum_odd_numbers(2); # 3 + 5 = 8
```
>피라미드의 층을 입력하면 그 층의 값들의 합을 구하라는 문제이다.  

## My Solution
```{.Python}
MAX = 1000000
def row_sum_odd_numbers(n):
	
	index = 0
	sum = 0
	
	#피라미드의 전체 리스트를 P_list에 넣는다.
	
	P_list = [num*2-1 for num in range(1, MAX)]
	#피라미드 각 층이 'n'일때 n층  왼쪽 끝 값의 인덱스는 '1+2+3+ ...+ (n-2) + (n-1)' 이다.
	for i in range(0,n):
		index += i

	#피라미드의 n층 인덱스 개수는 n개 이므로..
	for j in P_list[index : (index+n)]:
		sum += j
	return sum
```

## acaccia's Solution
```
def row_sum_odd_numbers(n):
	return n**3
```
하하..  
3+5 = 4+4 = 2**3  
7+9+11 = 8+9+10 = 9+9+9 = 3**3  
~~이거보자마자 머리얻어맞은것 같았다.~~  
나의 삽질은 어디까지...ㅠㅠ 왜 이생각을 못했지??  
바보인증 ㅠㅠ

