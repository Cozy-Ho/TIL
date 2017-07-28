CodeWars_6
==========
# Question

You have an array of numbers.  
Your task is to sort ascending odd numbers but even numbers must be on their places.  

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.  

Example  
```
sortArray([5,3,2,8,1,4]) == [1,3,2,8,5,4]
```
>주어진 숫자배열을 규칙에맞게 가공하여 리턴하면된다.  
>짝수항은 그대로두고 홀수항만 순서대로 정렬하면 되는문제다.

# My Solution
```
def sort_array(arr):
  for i in range(0, len(arr)):
    for j in range(0, len(arr)):
      if arr[i]%2 == 1 and arr[j]%2 == 1 and arr[i] < arr[j]:
        tmp = arr[i]
        arr[i] = arr[j]
        arr[j] = tmp
  return arr
```
학교 C언어 수업때 했었던 정렬방법이 생각나서 시도해봤다.  
뭔가 줄일 수 있을거같은데...ㅠ  

# PilgrimShadow's Solution
```
def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse = True)
  return [x if x%2==0 else odds.pop() for x in arr]
```
오오오.. 홀수항을 따로 저장하고 정렬한뒤, 리스트를 만들어 나가다가 짝수가아닐때!! pop 시키는구나.. 똑똑하군!  
이러면 하나하나 값을 교환해 주는것보다 훨신빠르겠다!
